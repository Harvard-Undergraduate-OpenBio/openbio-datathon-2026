Trophoblast Gene Expression Distinguishes Early-Onset Preeclampsia After Accounting for Delivery Timing

Several placental genes, including FLT1, ENG, and LEP, remained more highly expressed in early-onset preeclampsia after adjusting for gestational age and fetal sex, with little evidence of major changes in cell composition.

By Emily Larkins, Iris Lawson-Ryan, Anthie Ntakas-Poulos, and Nicole Zac Soligno


Figure 1

Figure 1. Differential expression in placentas delivered at or before 34 weeks. Each point is one gene, comparing PE (n = 15) with non-PE (n = 10) placentas after adjusting for gestational age at delivery and fetal sex. Red points (188 genes) meet both thresholds: adjusted p-value below 0.05 and an absolute log2 fold change of at least 1. The dashed line marks an adjusted p-value of 0.05.

Introduction

Preeclampsia is a pregnancy complication marked by high blood pressure that can affect multiple organs and is thought to originate in the placenta. It can become dangerous for both the pregnant person and baby, sometimes requiring early delivery. Delivering the baby and placenta is currently the only way to stop the condition from progressing.

Early delivery creates a challenge for researchers studying the placenta. Because the placenta changes throughout pregnancy, differences in gene expression between pregnancies with and without preeclampsia may reflect the condition itself or simply when delivery occurred. We asked how much of the difference in placental gene expression remains after accounting for delivery timing, and which placental cells may be associated with the genes that remain different. We hypothesized that trophoblast cells, particularly the syncytiotrophoblast, increase expression of preeclampsia-associated genes without a major change in their relative proportions.

The Data and Our Methods

We analyzed bulk RNA sequencing data from 30 human villous placental samples in GSE203507 (Ackerman et al., 2023). Fifteen samples came from pregnancies with early-onset preeclampsia (PE): 8 with PE alone (EOPE) and 7 with both PE and fetal growth restriction (EOPE+FGR), meaning the baby did not grow as expected. The 15 non-PE samples included 5 with FGR, 5 with idiopathic preterm birth (iPTB), and 5 with term birth (TB). Each sample represented a different pregnancy.

Bulk RNA sequencing measures gene expression by examining the RNA molecules produced in a tissue, but it cannot identify which cell type produced each transcript. We tested for differential expression, with p-values adjusted for multiple testing. We performed three comparisons:

an unadjusted analysis
an analysis adjusted for gestational age at delivery and fetal sex
an analysis restricted to deliveries at or before 34 weeks and adjusted for both factors

We also used the Zeisel Lab placental gene-expression browser, based on an independent single-cell study by Admati et al. (2023), to explore which placental cell types express selected genes. Our small sample size and differences in delivery timing limit how completely we can separate disease-related changes from other differences between pregnancies.

What We Found

We first identified 369 genes with significantly different expression between PE and non-PE placentas: 256 had higher expression and 113 had lower expression in PE. We defined significant differences as an adjusted p-value below 0.05 and an absolute log2 fold change of at least 1, equivalent to a twofold or greater difference in expression.

However, all 15 PE samples were delivered between 26 and 34 weeks, while the five term non-PE samples were delivered at approximately 39 weeks. Since placental gene expression changes throughout pregnancy, delivery timing could contribute to some of the differences we observed.

After adjusting for gestational age at delivery and fetal sex, 273 genes were differentially expressed. When we restricted the analysis to deliveries at or before 34 weeks and adjusted for the same factors, 188 genes were differentially expressed. This restricted comparison included 25 samples because the five term non-PE samples were excluded. Its non-PE samples were themselves delivered early for other reasons, such as spontaneous preterm labor or FGR, so they are not a fully healthy comparison group.

Despite the decrease, 163 genes (44% of the original 369) remained significant across all three comparisons. Another 139 genes (38%) were no longer significant in either adjusted comparison. The decrease was particularly pronounced among genes with lower expression in PE: in the restricted comparison, their number fell from 113 to 32, a 72% reduction, while genes with higher expression fell from 256 to 156, a 39% reduction. This suggests that some initial differences, particularly among genes with lower expression, may reflect delivery timing or other differences between the groups. However, the comparisons cannot establish that timing alone explains these changes.

Figure 2

Figure 2. Expression of the 20 most significant genes in placentas delivered at or before 34 weeks. Boxes show expression (log2 counts per million) in non-PE (blue, n = 10) and PE (red, n = 15) placentas. Values are shown before adjustment for gestational age and fetal sex. Most genes, including FLT1, ENG, and LEP, were more highly expressed in PE; a few, such as TFDP2, GYLTL1B, and DOCK8, were lower.

We also used principal component analysis (PCA) to examine overall gene-expression patterns across samples. PCA summarizes the largest sources of variation in a dataset. Each point represents one placenta, and points closer together have more similar overall expression patterns. The first two components explained 33% of the variation (21% and 12%, respectively).

Samples partly separated by clinical group along the first component: most PE samples fell to the right, while term and preterm non-PE samples fell to the left (Figure 3). Notably, preterm non-PE samples grouped with term samples rather than with PE samples of similar gestational age (Figure 4). This suggests that the main expression pattern associated with PE is not explained by delivery timing alone. FGR samples tended to fall lower on the second component. The groups still overlapped, so overall expression patterns do not fully separate PE from non-PE placentas.

Figure 3

Figure 3. Overall placental gene-expression patterns by clinical group. PCA of all 30 samples. Each point is one placenta, and points closer together have more similar expression. EOPE, early-onset preeclampsia; EOPE+FGR, preeclampsia with fetal growth restriction; FGR, fetal growth restriction without preeclampsia; iPTB, idiopathic preterm birth; TB, term birth.

Figure 4

Figure 4. Overall placental gene-expression patterns by gestational age at delivery. The same PCA as Figure 3, colored by gestational age at delivery in weeks.

Three genes remained notably more highly expressed in PE in the restricted comparison: FLT1 (approximately 5-fold), ENG (approximately 4-fold), and LEP (approximately 20-fold). A fold change describes how many times higher or lower a gene’s expression is between groups; for example, a 5-fold increase means expression was approximately five times as high in PE placentas.

FLT1 and ENG encode receptors whose soluble forms, soluble FLT1 and soluble endoglin, block signals that promote blood vessel growth. Increases in both are consistent with previous research linking these soluble forms to preeclampsia. Our gene-level analysis did not distinguish the soluble form of FLT1 from the membrane-bound form. LEP encodes the hormone leptin, and its substantial increase suggests that altered placental hormone production may also be involved. LEP expression varied widely among non-PE placentas but was consistently high in PE placentas, so the size of this fold change partly reflects a few non-PE samples with very low expression. RNA expression alone does not establish how much protein is produced or released.

We next examined whether differences in cell composition might explain the results. Of 36 genes commonly used as markers for placental cell types, only CGA, a syncytiotrophoblast marker, met our significance criteria. Because CGA encodes part of a placental hormone that is often increased in PE, its change may reflect increased gene activity rather than more syncytiotrophoblast. Median marker changes across all cell types were small, ranging from −0.21 to +0.48 in log2 fold change. The largest corresponds to about a 1.4-fold difference. Together, these results provide little evidence of a major shift in cell composition, although smaller changes cannot be excluded.

To explore where the genes of interest are expressed, we consulted the independent single-cell reference. FLT1 was primarily associated with trophoblast cells, and LEP appeared almost exclusively in the syncytiotrophoblast, the outer placental layer that directly contacts maternal blood. ENG was detected more broadly, including in endothelial cells as well as trophoblasts.

Figure 5

Figure 5. FLT1, ENG, and LEP expression across placental cell types in an independent single-cell dataset. (A) Expression in individual cells, grouped by cell type. (B) Expression shown on cell-type clusters. Adapted from the Zeisel Lab placental gene-expression browser (Admati et al., 2023).

Together, these findings are consistent with the possibility that trophoblast cells contribute to the increased expression of genes associated with preeclampsia, rather than the results being driven primarily by a major change in cell proportions. However, the single-cell reference comes from a separate study and cannot establish which cells produced the RNA in our samples.

Unanswered Questions

Our analysis cannot determine whether increased gene expression occurred within individual cells or partly reflects differences between cell populations. We also found that SERPINA3 had approximately 35-fold higher expression in PE placentas in the restricted comparison, but could not assign it to a cell type because it was minimally detected in the single-cell data. Because SERPINA3 expression was very low in non-PE placentas, this large fold change should be interpreted cautiously. Whether increased RNA levels lead to changes in protein production, secretion, or signaling also remains unknown.

Other factors may have influenced our results. Fetal sex was unevenly distributed between groups (10 female and 5 male PE samples, compared with 5 female and 10 male non-PE samples), so we included it as an adjustment factor. FGR was also present in 7 PE samples and 5 non-PE samples. Additionally, three samples had discrepancies between their clinical labels and recorded blood pressure: S12 was labeled PE despite a recorded blood pressure below the diagnostic cutoff, while S04 and S15 were labeled non-PE despite elevated blood pressure. In the PCA, S04 grouped with PE samples. We retained these samples as originally reported in the dataset.

Conclusions, Limitations and Next Steps

Our findings suggest that delivery timing influences which placental gene-expression differences are associated with preeclampsia. However, FLT1, ENG, and LEP remained more highly expressed in PE placentas, while cell-type marker analysis showed little evidence of major changes in cell composition. These results are consistent with our hypothesis that trophoblast cells, particularly the syncytiotrophoblast, may increase expression of genes associated with early-onset preeclampsia without a major change in their relative proportions.

The study included only 30 samples. Because early-onset PE requires delivery at or before 34 weeks, no PE samples were delivered later, while the term non-PE samples were delivered at approximately 39 weeks. This left no PE samples at comparable gestational ages and limits our ability to separate the effects of preeclampsia from delivery timing. Placentas were also collected at delivery, so their gene expression may not reflect earlier events that contributed to the condition. Our results show associations, not proof of cause. The independent single-cell browser provides supporting context, not validation of the cell-specific changes in our samples.

Future work could:

Estimate cell-type proportions in our samples directly, using the Admati et al. single-cell data as a reference for computational deconvolution
Test FLT1, ENG, and LEP expression within syncytiotrophoblast cells using the available single-cell pseudobulk data
Repeat the analysis in a larger cohort with more gestational-age-matched preterm pregnancies

If leptin is produced by the same altered syncytiotrophoblast population, it could also be investigated as an additional blood biomarker. This would be a possible diagnostic application, not a proposed treatment.

Data and Code

Code repository: OpenBio Datathon 2026

Data sources:

Ackerman et al. (2023). Placental RNA sequencing dataset, GSE203507.
Admati et al. (2023). Placental single-cell RNA sequencing dataset (CC BY 4.0).
Zeisel Lab placental gene-expression browser.
Acknowledgements

Thank you to the organizers and speakers of the 2026 OpenBio Datathon for their support and for providing the data and structure of this project.
