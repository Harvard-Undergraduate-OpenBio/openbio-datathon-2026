# Hypothesis Card

## Title
Trophoblast Gene Activity Distinguishes Early Onset Preeclampsia After Accounting for Delivery Timing

## Clinical/Biological Problem
Preeclampsia is a pregnancy disorder marked by high maternal blood pressure and is thought to originate in the placenta. Because delivery is the only cure, preeclampsia placentas are typically delivered early and compared with placentas from later deliveries. As a result, differences in gene activity may reflect delivery timing rather than disease. This hypothesis addresses how much of the preeclampsia signal remains after accounting for delivery timing, and which placental cells carry it.

**Supporting data:** When we limited the comparison to samples delivered at or before 34 weeks, all 15 PE samples remained, and 5 non-PE samples were removed. This means every PE sample was delivered at or before 34 weeks, while some controls were delivered later.

## Dataset(s) and Relevant Cells
We analyzed bulk RNA sequencing data from 30 villous placental samples (GSE203507; Ackerman et al., 2023) and used the Zeisel/Admati single-cell gene browser (Admati et al., 2023) for cell type context. The primary cell type of interest is the syncytiotrophoblast, the outer layer of the placenta that is in direct contact with maternal blood.

**Supporting data:** 15 PE samples were compared with 15 non-PE samples (Runs A and B) and with 10 non-PE samples delivered at or before 34 weeks (Run C).

## Observed Result
The number of genes that differed between PE and non-PE placentas fell by about half once delivery timing was accounted for. Genes lower in PE dropped the most. The genes that remained in our strictest comparison included established placental factors associated with preeclampsia.

**Supporting data:**
- Genes meeting our cutoffs (padj < 0.05, |log2FC| ≥ 1): 369 with no adjustment, 273 after adjusting for gestational age and fetal sex, and 188 when restricted to samples delivered at or before 34 weeks.
- Genes lower in PE fell from 113 to 65 to 32 (a 72% decrease), while genes higher in PE fell from 256 to 208 to 156 (a 39% decrease).
- In Run C, ENG (log2FC 1.95, padj 5.8e-11), FLT1 (log2FC 2.43, padj 4.7e-05) and LEP (log2FC 4.29, padj 7.6e-05) were higher in PE, approximately 4, 5 and 20-fold, respectively.

## Proposed Mechanism
We hypothesize that in early-onset preeclampsia, once delivery timing is accounted for, placental trophoblast cells (particularly the syncytiotrophoblast) are present in approximately normal proportions but increase the expression of genes encoding factors known to inhibit blood vessel growth (FLT1, ENG) and the hormone leptin (LEP). Many genes that initially appeared decreased in preeclampsia instead reflect earlier delivery.

**Supporting data:**
- Only 1 of 36 cell type marker genes met our cutoffs in Run C (CGA, a syncytiotrophoblast marker, log2FC 1.04, padj 0.026), and median marker changes for every cell type were small (log2FC between −0.21 and +0.48). This suggests no major shift in cell composition.
- In the gene browser, LEP appeared almost exclusively in syncytiotrophoblast and FLT1 mainly in trophoblast cells, consistent with these cells being the source. ENG appeared in several cell types.

## Why the Result Is Biologically Plausible
Placental soluble FLT1 (sFlt1) and soluble endoglin (sEng, from ENG) are elevated in preeclampsia and induce hypertension in animal models (Maynard et al., 2003; Venkatesha et al., 2006). FLT1 dysregulation has been observed specifically in the syncytium in early, but not late, preeclampsia (Admati et al., 2023). An independent multiomics study that also adjusted for fetal sex and gestational age identified FLT1 and LEP within its placental disease signature (Piekos et al., 2025).

**Supporting data:** These established genes remained significant in Run C, our comparison of placentas delivered at similar times.

## Alternative Explanations/Confounders
- **Delivery timing:** Addressed through statistical adjustment (Run B) and a comparison limited to deliveries at or before 34 weeks (Run C). Adjustment cannot fully model the later control samples, since no PE samples were delivered after 34 weeks.
- **Fetal sex:** The placenta is fetal tissue, so we included fetal sex as a covariate in Runs B and C.
- **Fetal growth restriction (FGR):** Some PE samples also had FGR, and FGR samples without PE were included among the controls.
- **Cell composition:** Each cell type is represented by only a few marker genes, so small shifts in cell proportions cannot be excluded.
- **Flagged samples:** All samples were kept as released; none were removed or corrected.

## Proposed Validation Experiment or Follow-up Analysis

**Computational:** Test FLT1, ENG, and LEP within syncytiotrophoblast using the provided single-cell pseudobulk data, and replicate this analysis in a larger cohort with more gestational age-matched preterm controls.

## Potential Intervention Relevance
The maternal blood sFlt1:PlGF ratio is already used to predict preeclampsia in women with suspected disease (Zeisler et al., 2016). If leptin is produced by the same altered syncytiotrophoblast, it could be evaluated as an additional blood biomarker. This represents a potential diagnostic application rather than a therapeutic target.

## Confidence Level and Limitations
**Confidence: Medium.** Key genes remained significant after accounting for delivery timing and agree with published findings. However, several limitations apply:
- Sample sizes are small, particularly in Run C (10 non-PE samples).
- Placental tissue was collected at delivery, so it reflects late pregnancy rather than the earlier events that may start preeclampsia.
- Bulk RNA sequencing cannot determine which cell type produced each transcript; the marker and browser analyses provide supporting context only.
- The gene browser is derived from a different study population and does not constitute validation.
- RNA expression does not establish protein levels, secretion, signaling between cells, or a causal role in disease.
- SERPINA3, which was approximately 35 fold higher in PE in Run C, could not be assigned to a cell type because it could not be displayed in the gene browser.

## References

### Datasets
1. Ackerman WE, Buhimschi IA, Buhimschi CS, et al. Molecular subphenotyping using placental transcriptomics in early-onset preeclampsia and fetal growth restriction. NCBI GEO GSE203507. https://www.ncbi.nlm.nih.gov/geo/query/acc.cgi?acc=GSE203507
2. Zeisel lab placenta PE gene browser. https://storage.googleapis.com/www_zeisellab/PE_web/pe_web_test_v1.html

### Literature
3. Ackerman, W. E., 4th, Buhimschi, C. S., Brown, T. L., Zhao, G., Summerfield, T. L., & Buhimschi, I. A. (2023). Transcriptomics-Based Subphenotyping of the Human Placenta Enabled by Weighted Correlation Network Analysis in Early-Onset Preeclampsia With and Without Fetal Growth Restriction. Hypertension (Dallas, Tex. : 1979), 80(6), 1363–1374. https://doi.org/10.1161/HYPERTENSIONAHA.122.20807
4. Admati, I., Skarbianskis, N., Hochgerner, H., Ophir, O., Weiner, Z., Yagel, S., Solt, I., & Zeisel, A. (2023). Two distinct molecular faces of preeclampsia revealed by single-cell transcriptomics. Med (New York, N.Y.), 4(10), 687–709.e7. https://doi.org/10.1016/j.medj.2023.07.005
5. Maynard, S. E., Min, J. Y., Merchan, J., Lim, K. H., Li, J., Mondal, S., Libermann, T. A., Morgan, J. P., Sellke, F. W., Stillman, I. E., Epstein, F. H., Sukhatme, V. P., & Karumanchi, S. A. (2003). Excess placental soluble fms-like tyrosine kinase 1 (sFlt1) may contribute to endothelial dysfunction, hypertension, and proteinuria in preeclampsia. The Journal of clinical investigation, 111(5), 649–658. https://doi.org/10.1172/JCI17189
6. Venkatesha, S., Toporsian, M., Lam, C., Hanai, J., Mammoto, T., Kim, Y. M., Bdolah, Y., Lim, K. H., Yuan, H. T., Libermann, T. A., Stillman, I. E., Roberts, D., D'Amore, P. A., Epstein, F. H., Sellke, F. W., Romero, R., Sukhatme, V. P., Letarte, M., & Karumanchi, S. A. (2006). Soluble endoglin contributes to the pathogenesis of preeclampsia. Nature Medicine, 12(6), 642–649. https://doi.org/10.1038/nm1429
7. Piekos, S.N., Barak, O., Baumgartner, A. et al. Placental network differences among obstetric syndromes identified with an integrated multiomics approach. Commun Biol 8, 1239 (2025). https://doi.org/10.1038/s42003-025-08631-6
8. Zeisler, H., Llurba, E., Chantraine, F., Vatish, M., Staff, A. C., Sennström, M., Olovsson, M., Brennecke, S. P., Stepan, H., Allegranza, D., Dilba, P., Schoedl, M., Hund, M., & Verlohren, S. (2016). Predictive Value of the sFlt-1:PlGF Ratio in Women with Suspected Preeclampsia. The New England journal of medicine, 374(1), 13–22. https://doi.org/10.1056/NEJMoa1414838

### Tools
9. Muzellec, B., Teleńczuk, M., Cabeli, V., & Andreux, M. (2023). PyDESeq2: a Python package for bulk RNA-seq differential expression analysis. Bioinformatics (Oxford, England), 39(9), btad547. https://doi.org/10.1093/bioinformatics/btad547
10. Love, M. I., Huber, W., & Anders, S. (2014). Moderated estimation of fold change and dispersion for RNA-seq data with DESeq2. Genome biology, 15(12), 550. https://doi.org/10.1186/s13059-014-0550-8
