
# Placental Guidance: Trophoblast Gene Activity Distinguishes Early Onset Preeclampsia After Accounting for Delivery Timing

OpenBio 2026 Datathon, Track 1: Maternal-Fetal Cell Communication in Preeclampsia

## Team

| Name | Role |
|---|---|
| Iris Lawson-Ryan | Equal contributor |
| Anthie Ntakas-Poulos | Equal contributor |
| Nicole Zac Soligno | Equal contributor |
| Emily Larkins | Equal contributor |

All team members contributed to choosing the research question, running the analysis, interpreting results and reviewing every deliverable.

## Research Question

How much of the difference in gene activity between preeclampsia (PE) and control placentas could be explained by when delivery happened? (Starter question 6)

## Data Used

- [x] GSE203507 bulk RNA-seq (required)
- [x] Zeisel/Admati gene browser, for at least three genes (required): FLT1, ENG, LEP
- [ ] Admati/Skarbianskis single-cell pseudobulk files (optional): not used
- [ ] Other public data: none

## How to Run

1. The data package is in [`track-01/data`](https://github.com/Harvard-Undergraduate-OpenBio/openbio-datathon-2026/tree/main/track-01/data) of the datathon repository. On Colab, the first notebook cell downloads it automatically.
2. Install packages by following [Track 1 Setup](https://github.com/Harvard-Undergraduate-OpenBio/openbio-datathon-2026/blob/main/track-01/1-setup.md). On Colab, the first cell installs PyDESeq2.
3. Open `submissions/placental_guidance/notebooks/placental_guidance_track01_workflow.ipynb` and choose **Runtime > Restart session and run all**. The full run takes about 5 minutes.

Reproducibility details:

- Notebook or script files: `notebooks/placental_guidance_track01_workflow.ipynb`
- Where we ran it: Google Colab (Python 3, PyDESeq2)
- Random seeds: none needed; PyDESeq2 and PCA give the same results on every run
- Expected results after a full run: 369, 273 and 188 genes passing in Runs A, B and C

## Files

| Path | Contents |
|---|---|
| `notebooks/` | The analysis notebook |
| `figures/` | Exported graphs, including `headline.png` |
| `docs/article.md` | Science communication article, following the [HUDP article guide](https://github.com/Harvard-Undergraduate-OpenBio/openbio-datathon-2026/blob/main/docs/article-guide.md) |
| `docs/analysis-plan.md` | The comparison, model and thresholds we chose |
| `docs/hypothesis-card.md` | Our hypothesis and how to test it |

## Key Findings

We compared 15 PE placentas with non PE placentas in three ways, using the same cutoffs each time (adjusted p value < 0.05 and at least a 2 fold change):

| Run | Samples | Covariates | Purpose | Genes passing |
|---|---|---|---|---|
| A: naive | All 30 (15 PE vs 15 non PE) | None | Baseline result, ignoring delivery timing | 369 |
| B: adjusted | All 30 (15 PE vs 15 non PE) | Gestational age, fetal sex | Same samples, statistically accounting for delivery timing and sex | 273 |
| C: ≤ 34 weeks | 25 (15 PE vs 10 non PE) | Gestational age, fetal sex | Removes the 5 term controls so both groups were delivered at similar times | 188 |

The number of genes that differed between PE and non PE placentas fell by about half once delivery timing was accounted for (369 to 188). Genes lower in PE dropped the most (113 to 32), compared with genes higher in PE (256 to 156). FLT1, ENG and LEP, which are known to be involved in preeclampsia, remained significantly higher in PE in Run C.

For the gene browser, we chose genes that were significant in Run C and had high read depth.


The browser showed LEP almost only in syncytiotrophoblast and FLT1 mainly in trophoblast cells, while ENG appeared in several cell types. We also tried SERPINA3, the gene with the largest increase in PE, but it could not be displayed in the browser. Marker genes for each cell type barely changed between groups.

**Our hypothesis:** In early onset preeclampsia, once delivery timing is accounted for, placental trophoblast cells (particularly the syncytiotrophoblast) are present in approximately normal proportions but increase the expression of genes encoding factors known to inhibit blood vessel growth (FLT1, ENG) and the hormone leptin (LEP). Many genes that initially appeared decreased in preeclampsia instead reflect earlier delivery.

## Limitations

Our groups are small (only 5 preterm and 5 term controls), and no PE sample was delivered after 34 weeks, so timing cannot be fully separated from disease. Bulk tissue mixes many cell types, so we cannot tell which cell made each RNA; the marker table and gene browser are supporting context only. Tissue was collected at delivery, so it reflects late pregnancy rather than the events that start preeclampsia, and RNA levels do not show protein levels or prove that these genes cause disease.

| Confounder | Why it matters | How we addressed it |
|---|---|---|
| **Delivery timing (gestational age)** | No PE sample was delivered after 34 weeks, while some controls were. Placental gene activity may change with gestational age | Added gestational age as a covariate (Run B) and restricted to samples delivered at ≤ 34 weeks (Run C) |
| **Fetal sex** | The placenta is fetal tissue, so sex differences could affect gene activity| Added fetal sex as a covariate (Runs B and C)|
| **Fetal growth restriction (FGR)** | 7 PE samples also have FGR, and 5 FGR samples without PE are among the controls | Not adjusted, because it is part of how groups are defined; reported as a limitation |
| **Cell mix** | Bulk RNA mixes many cell types, so a change could mean more of a cell type rather than changed cells | Checked all marker genes per cell type; used the gene browser for cell type context |
| **Flagged samples** | Some samples have quality flags in the metadata | All samples were kept as released|
| **Small groups** | Only 5 preterm and 5 term controls | Reported as a limitation; focused on genes that held up across all three runs |

## Presentation

Presentation Path: submissions/placental_guidance/docs/Placental Guidance Track 01_presentation.pdf

## References

### Datasets
1. Ackerman WE, Buhimschi IA, Buhimschi CS, et al. Molecular subphenotyping using placental transcriptomics in early-onset preeclampsia and fetal growth restriction. NCBI GEO GSE203507. https://www.ncbi.nlm.nih.gov/geo/query/acc.cgi?acc=GSE203507
2. Zeisel lab placenta PE gene browser. https://storage.googleapis.com/www_zeisellab/PE_web/pe_web_test_v1.html

### Tools
3. Muzellec B, Teleńczuk M, Cabeli V, Andreux M. PyDESeq2: a python package for bulk RNA-seq differential expression analysis. Bioinformatics. 2023;39(9):btad547. https://doi.org/10.1093/bioinformatics/btad547
4. Love MI, Huber W, Anders S. Moderated estimation of fold change and dispersion for RNA-seq data with DESeq2. Genome Biol. 2014;15(12):550. https://doi.org/10.1186/s13059-014-0550-8

Literature cited for interpretation is listed in `docs/hypothesis-card.md`.

## AI Disclosure

We used Claude as an assistant during this project, to help with code structure, explaining methods and results, finding literature, and drafting and editing documents. All analysis choices, interpretations and final text were reviewed and decided by our team, and all cited papers were checked by the team.


