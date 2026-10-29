# Track 01 Participant Guide

**Maternal-Fetal Cell Communication in Preeclampsia**

[![Download Guide](https://img.shields.io/badge/Data-Download_Guide-0fe995?style=flat-square)](../../data/track-01/README.md)
[![Starter Questions](https://img.shields.io/badge/Docs-Starter_Questions-13deba?style=flat-square)](research-questions.md)
[![Python Starter](https://img.shields.io/badge/Code-Python_Starter-0fe995?style=flat-square)](../../notebooks/track-1/track01_starter.ipynb)
[![R Starter](https://img.shields.io/badge/Code-R_Starter-13deba?style=flat-square)](../../notebooks/track-1/track01_starter.Rmd)

This track looks at how gene activity in the placenta differs between pregnancies with preeclampsia and control pregnancies. Your team will identify those differences, then use reference data to understand which placental cell types may be involved.

The data arrive prepared and documented. Choosing comparisons and interpreting the results is up to you.

## What You Will Use

| Resource | Role |
|---|---|
| GSE203507 bulk RNA-seq (villous tissue) | Required core dataset for all teams |
| Zeisel/Admati gene browser | Interpretation layer, required for at least three genes |
| Admati/Skarbianskis single-cell data | Optional extension, prepared as pseudobulk |
| GSE198373 | Reference only, linked |
| HCA fetal-maternal interface | Reference only, linked |
| HCA spatial multiomics trophoblast atlas | Reference only, linked |

See the [download guide](../../data/track-01/README.md) for every file and link.

### Core Data

GSE203507 contains 30 samples of villous tissue from the placenta. It is bulk RNA sequencing, which measures gene activity across a whole tissue sample rather than in individual cells.

The count matrix shows how many RNA reads were counted for each gene in each sample. The metadata file describes each pregnancy, including preeclampsia status and clinical details such as gestational age. Missing values are marked `NA` and never filled in.

### Optional Single-Cell Extension

The Admati/Skarbianskis dataset gives a more detailed view of the placenta: 86,752 labeled cells from 26 donors. We combined counts within each donor and cell type, so you work with a smaller table while each donor remains one independent biological sample. Multiple sequencing libraries from the same person do not count as separate patients.

The early-onset comparison in this extension is exploratory. It has three control donors against ten preeclampsia donors.

### Interpretation Resources

The gene browser and reference atlases show where genes are active and which genes mark broad cell types. Most are linked rather than downloaded. A small [marker table](../../data/track-01/interpretation/track01_marker_matrix.csv) helps you connect findings to placental cell types, and the [browser guide](../../data/track-01/interpretation/zeisel_browser_guide.md) explains how to use the browser and what to do if it is down.

## Starter Questions

Pick one or more of these, or adapt them. Full list with notes: [starter questions](research-questions.md).

1. What makes a placenta affected by preeclampsia look different at the genetic level?
2. Does preeclampsia leave the same genetic footprint in every pregnancy?
3. Which placental cells show the biggest differences between preeclampsia and control pregnancies?
4. Is preeclampsia associated with a different mix of placental cells, or different behavior from the same cells?
5. What can the placenta tell us about the connection between preeclampsia and restricted fetal growth?
6. How much of the difference between preeclampsia and control samples could be explained by when delivery happened?
7. Do early-onset and late-onset preeclampsia tell different biological stories?
8. What might gene activity reveal about communication between placental cells in preeclampsia?
9. Do the genes that differ in preeclampsia normally work across the placenta, or are they concentrated in specific cell types?
10. What can a map of healthy early pregnancy help us understand about the changes seen in preeclampsia?

## Getting Started

1. Download and verify the data package using the [download guide](../../data/track-01/README.md).
2. Set up an environment.

   ```bash
   conda env create -f environment/environment.yml
   conda activate openbio-datathon-2026
   jupyter lab
   ```

   R users can open `notebooks/track-1/track01_starter.Rmd` in RStudio and install DESeq2, ggplot2 and pheatmap.
3. Run a starter notebook from top to bottom. It loads the files and checks them. It does not choose a comparison, set thresholds or produce results.
4. Read `track01_data_dictionary.md` before choosing a comparison.
5. Choose your question and comparison, then document every analysis decision.
6. Look up at least three of your genes in the Zeisel/Admati gene browser.

## Ground Rules

- There is no answer key. We do not provide comparisons, top gene lists, pathway results, chosen outliers or a biological story.
- Broad cell-class labels are supplied. You decide how much confidence to place in them.
- Treat the donor as the unit of replication. Cells and libraries from one person are not independent samples.
- Keep `NA` values as missing. Report any value flagged in the data dictionary rather than correcting it silently.
- Bulk differences may reflect a change in cell mix rather than a change within cells. Placental tissue collected at delivery reflects late pregnancy, not earlier events.
- Use the released package. Do not rebuild the competition dataset from raw sources.

## Submit

[![Submission Template](https://img.shields.io/badge/Template-Final_Submission-0fe995?style=flat-square)](../../templates/final-submission.md)
[![Hypothesis Card](https://img.shields.io/badge/Template-Hypothesis_Card-13deba?style=flat-square)](../../templates/hypothesis-card.md)
[![Rubric](https://img.shields.io/badge/Docs-Submission_Rubric-0fe995?style=flat-square)](../submission-rubric.md)
[![Submission Instructions](https://img.shields.io/badge/Docs-Submission_Instructions-13deba?style=flat-square)](../../submissions/README.md)

Follow the [submission instructions](../../submissions/README.md) and cite every dataset and tool you use ([citations](citations.md)).
