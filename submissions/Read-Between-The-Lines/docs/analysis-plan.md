# Analysis Plan

## Research Question

How much of the difference in villous-tissue gene activity between early-onset preeclampsia and control placentas could be explained by when delivery happened? (Starter question 6.)

## Datasets

| Dataset ID | Role | Why This Dataset |
|---|---|---|
| GSE203507 (villous tissue, bulk RNA-seq) | Main analysis | Has both preterm and term non-preeclampsia controls, so disease and delivery timing can be separated |
| Zeisel/Admati gene browser | Required cell-type lookup | Shows which placental cell types express each gene |
| Marker table (`track01_marker_matrix.csv`) | Cell-mix check | Shows whether marker genes of a cell type shift |

## Methods

1. **Data loading and checks.** 30 samples appear in both tables, counts are non-negative whole numbers, and there are no duplicates. Each placenta is one pregnancy, so the unit of replication is the pregnancy. Gene filter: at least 10 reads in at least 5 samples (15,835 of 26,485 genes kept).
2. **Comparison and why we chose it.** The main comparison is preeclampsia (EOPE + EOPE+FGR, n=15) vs preterm controls (iPTB, n=5), because both groups were delivered in similar weeks (30.2 vs 31.5 on average). We also compared preeclampsia vs term controls (TB, n=5) and preterm vs term controls. Growth-restriction-only samples (5) appear in plots but not in tests. These three comparisons follow the design of starter question 6.
3. **Statistical model and thresholds.** PyDESeq2 0.5.4. Main cutoffs: padj < 0.05 and |log2FC| >= 1 (2-fold).
   - The main comparison is a two-group model (472 genes). A three-group model (522 genes for preeclampsia vs preterm) is used for the cross-control comparisons and as the reference list for the robustness checks.
   - A 20-draw equal-size 5-vs-5 test compares preeclampsia vs preterm, random splits of the 10 controls, and preterm vs term.
   - Each gene's difference vs term controls is split into a disease part and a timing part.
   - Robustness checks: a no-covariate refit, then adding delivery week, fetal sex or growth restriction, and dropping S01 and S12.
   - *Added after seeing results, as sensitivity checks:* the |log2FC| >= 0.5 cutoff, the 20-draw power check, the covariate runs, and dropping S01 and S12.
4. **Gene browser lookups.** FLT1, ENG, PAPPA2, LEP, HLA-G. We record cell types and specificity only, because the browser's star legend is not explained.
5. **Optional extension analyses.** None. We did not use the pseudobulk files.
6. **Interpretation and figures.** We do not claim causation. We use terms such as "associated with" and "looks driven by".

## Confounders and Controls

- **Gestational age:** matched by design with preterm controls (about a 1.3-week gap), then checked with a delivery-week covariate. Term controls (about 39 weeks) share no range with other groups, so a covariate across them is not used.
- **Growth restriction:** 7 of 15 cases have it and no control does. Checked with a covariate.
- **Fetal sex:** checked with a covariate.
- **Outliers and flags:** S01 (PCA outlier, second-lowest read depth) and S12 (flagged `pe_without_bp_ge_140_90`) stay in the main analysis and are dropped together in a sensitivity run. S26's day value (38.7) is kept as released (39.0 weeks).
- **Preterm control quality:** spontaneous preterm births are not healthy placentas, so they are an imperfect control.
- **Bulk tissue:** cannot separate a change in cell mix from a change within cells.

## Expected Figures

1. Delivery week by group, and PCA colored by group and by delivery week
2. Volcano plot of preeclampsia vs preterm controls
3. Power check of 5-vs-5 draws, to compare how many genes differ in equal-size tests
4. FLT1 and HLA-G by delivery week, with the headline figure
5. Fold change vs term controls against fold change vs preterm controls, to show which differences persist when controls are matched on delivery time
