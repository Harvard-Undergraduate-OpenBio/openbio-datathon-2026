# Analysis Plan

## Research Question

Our question is starter question 6: How much of the difference in gene activity between preeclampsia (PE) and control placentas could be explained by when delivery happened?

Preeclampsia often forces early delivery. In this dataset, all 15 PE samples were delivered between 26 and 34 weeks, while all 5 term controls were delivered at about 39 weeks. Because the placenta changes a lot late in pregnancy, some differences that look like preeclampsia may instead reflect earlier delivery. We aim to separate the two and identify which gene differences remain.

## Datasets

| Dataset ID | Role | Why This Dataset |
|---|---|---|
| GSE203507 (bulk RNA-seq, 30 villous placenta samples with clinical metadata) | Required core | Provides gene counts and delivery timing for each sample, so we can test which genes differ between PE and controls with and without accounting for delivery timing |
| Zeisel/Admati gene browser | Required interpretation | Shows which placental cell types use a gene and whether that differs in PE, so we can suggest which cells carry our results |

## Methods

### 1. Data loading and checks
We loaded `track01_counts_vt.csv` (26,485 genes × 30 samples) and `track01_metadata_vt.csv` (30 samples). We confirmed that all 30 samples appear in both tables, counts are whole nonnegative numbers, and there are no duplicate genes or samples. Each sample comes from a different pregnancy (donors S01 to S30), so each donor counts once.

Missing values were kept as missing: blood pressure and birthweight fields are missing for the 5 term controls. Flagged samples were kept and reported rather than corrected: S12 (labeled PE, blood pressure below the cutoff) and S04 and S15 (labeled non PE, high blood pressure).

We then explored the samples with PCA, coloring by clinical group, gestational age, control type, FGR status, fetal sex and maternal age.

### 2. Comparison and why we chose it
All runs compare PE vs non PE using the `pe_status` column. We chose all three comparisons before running any test:

| Run | Samples | Covariates | Purpose |
|---|---|---|---|
| A: naive | All 30 (15 PE vs 15 non PE) | None | Baseline result, ignoring delivery timing |
| B: adjusted | All 30 (15 PE vs 15 non PE) | Gestational age, fetal sex | Same samples, statistically accounting for delivery timing and sex |
| C: ≤ 34 weeks | 25 (15 PE vs 10 non PE) | Gestational age, fetal sex | Removes the 5 term controls so both groups were delivered at similar times |

A comparison of samples delivered after 34 weeks was not possible because no PE sample was delivered after 34 weeks. Comparing how many genes remain across Runs A, B and C answers our question.

Runs were defined in the notebook as:

    runs = {
        "A_naive":    {"covariates": [], "rows": metadata["ga_delivery_weeks"] > 0},
        "B_adjusted": {"covariates": ["ga_delivery_weeks", "fetal_sex"], "rows": metadata["ga_delivery_weeks"] > 0},
        "C_ga34":     {"covariates": ["ga_delivery_weeks", "fetal_sex"], "rows": metadata["ga_delivery_weeks"] <= 34},
    }

### 3. Statistical model and thresholds
We used PyDESeq2, which adjusts for sequencing depth and tests each gene for a difference between PE and non PE. Design formulas were `~pe_status` (Run A) and `~ga_delivery_weeks + fetal_sex + pe_status` (Runs B and C).

A gene counted as differentially expressed if it had:
- **Adjusted p-value (padj) < 0.05:** about 5% of called genes may be false positives, the standard choice when testing thousands of genes.
- **|log2 fold change| ≥ 1:** at least 2 times higher or lower in PE, so we focus on changes large enough to interpret biologically.

The same thresholds were used for all three runs so gene counts can be compared directly. We also checked how counts changed with a looser fold change cutoff (|log2FC| ≥ 0.5). We then compared gene lists across runs to find genes that passed in all three (robust genes) and genes that disappeared once timing was accounted for (timing genes).

### 4. Gene browser lookups (at least three genes)
We looked up **FLT1, ENG and LEP**. We chose them because they:
- passed our cutoffs in all three runs,
- have high read depth (baseMean in the thousands or higher), so results are reliable,
- are known to be involved in preeclampsia.

For each gene, we recorded which cell types use it most, how specific it is, and whether the browser shows a PE vs control difference. We also tried SERPINA3, the gene with the largest increase in PE, but it could not be displayed in the browser.

Before the browser, we checked the organizers' marker gene table (36 markers across 9 cell types) using Run C, to see whether whole cell types appeared more or less common in PE.

### 5. Optional extension analyses
We did not do single cell analysis.

### 6. Interpretation and figures
- We report how many genes passed in each run and how many held up across all three runs.
- We separate observations (for example, "FLT1 is higher in PE in all three runs") from interpretation (for example, "consistent with trophoblast cells behaving differently").
- We use the marker table and browser as supporting context, not proof, and use "consistent with" or "suggests" rather than "proves."

## Confounders and Controls

| Confounder | Why it matters | How we addressed it |
|---|---|---|
| **Delivery timing (gestational age)** | All PE samples delivered at 26 to 34 weeks; term controls at about 39 weeks. The placenta changes a lot in late pregnancy | Added gestational age as a covariate (Run B) and restricted to samples delivered at ≤ 34 weeks (Run C) |
| **Fetal sex** | The placenta is fetal tissue, and sex is unbalanced: PE 10 female / 5 male; non PE 5 female / 10 male | Added fetal sex as a covariate (Runs B and C) |
| **Fetal growth restriction (FGR)** | 7 PE samples also have FGR, and 5 FGR samples without PE are among the controls | Not adjusted, because it is part of how groups are defined; reported as a limitation |
| **Flagged samples** | S12, S04 and S15 have blood pressure values that do not match their labels | Kept as released and reported |
| **Small groups** | Only 5 preterm and 5 term controls | Reported as a limitation; focused on genes that held up across all three runs |

## Expected Figures

1. PCA colored by clinical groups (do PE samples separate from controls?)
2. PCA colored by gestational age at delivery (does delivery timing drive the same pattern?)
3. Volcano plots for Runs A, B and C (how the number of significant genes shrinks as timing is accounted for)
4. Headline visual



## References

### Datasets
1. Ackerman WE, Buhimschi IA, Buhimschi CS, et al. Molecular subphenotyping using placental transcriptomics in early-onset preeclampsia and fetal growth restriction. NCBI GEO GSE203507. https://www.ncbi.nlm.nih.gov/geo/query/acc.cgi?acc=GSE203507
2. Zeisel lab placenta PE gene browser. https://storage.googleapis.com/www_zeisellab/PE_web/pe_web_test_v1.html

### Tools
4. Muzellec B, Teleńczuk M, Cabeli V, Andreux M. PyDESeq2: a python package for bulk RNA-seq differential expression analysis. Bioinformatics. 2023;39(9):btad547. https://doi.org/10.1093/bioinformatics/btad547
5. Love MI, Huber W, Anders S. Moderated estimation of fold change and dispersion for RNA-seq data with DESeq2. Genome Biol. 2014;15(12):550. https://doi.org/10.1186/s13059-014-0550-8


