# Track 01 Participant Guide

**Maternal-Fetal Cell Communication in Preeclampsia**

[![Data Package](https://img.shields.io/badge/Data-Track_01_Package-0fe995?style=flat-square)](../../data/track-01/README.md)
[![Python Starter](https://img.shields.io/badge/Code-Python_Starter-13deba?style=flat-square)](../../notebooks/track-1/track01_starter.ipynb)
[![R Starter](https://img.shields.io/badge/Code-R_Starter-0fe995?style=flat-square)](../../notebooks/track-1/track01_starter.Rmd)
[![Data Catalog](https://img.shields.io/badge/Docs-Data_Catalog-13deba?style=flat-square)](data-catalog.md)

Investigate placental gene-expression differences in preeclampsia and use single-cell references to ask which cells may carry the affected programs. Track 01 uses a bulk RNA-seq core, with an optional single-cell extension.

## Before You Start

The HDAG data package has not been released. Its files are intentionally blank; the starter notebooks can open now, but analysis must wait for the prepared data.

| Resource | Role | Availability |
|---|---|---|
| Villous-tissue counts and sample metadata | Required bulk analysis | Pending HDAG |
| Zeisel gene browser | Required gene localization | External resource |
| Reference gene list | Orientation, not an answer key | In the repository |
| Donor-by-cell-type pseudobulk | Optional extension | Pending HDAG |

You do not need to download sequencing reads or raw Cell Ranger files. Use the prepared release once it is available; do not assemble a replacement competition dataset.

## Setup

For Python, create the repository environment and launch Jupyter from the repository root:

```bash
conda env create -f environment/environment.yml
conda activate openbio-datathon-2026
jupyter lab
```

Open `notebooks/track-1/track01_starter.ipynb` and run it from top to bottom. Keep the repository folder structure so its relative data paths work.

For R, open `notebooks/track-1/track01_starter.Rmd` in RStudio. Install DESeq2 for the analysis scaffold. Its plotting chunks require ggplot2 and pheatmap; a verified Track 01 R environment is not yet supplied.

## Analysis Workflow

| Stage | Your task |
|---|---|
| Load | Import the released count matrix and sample sheet. Read the accompanying dictionary. |
| Check | Verify sample alignment and nonnegative integer counts. Record missing metadata rather than imputing it. |
| Explore | Inspect sample-level QC and overall structure. Explain any exclusions instead of choosing them to strengthen a result. |
| Compare | Choose an organizer-approved contrast and justify the comparison. Consider gestational age and control type. |
| Test | Run differential expression. Document the model and report multiple-testing-adjusted results. |
| Interpret | Conduct one pathway-level analysis using a documented gene-set version. Explain your selection criteria. |
| Localize | Examine three to six selected genes in the Zeisel browser. Record the cell classes and relevant caveats. |
| Propose | State one testable hypothesis and a follow-up experiment. Explain what the analysis cannot establish. |

The R starter contains an unevaluated DESeq2 skeleton. The Python starter supports exploration; it is not a complete differential-expression pipeline. Neither starter provides a finished result.

### Approved Contrasts

<!-- Intentionally blank pending organizer approval and HDAG metadata. -->

## Gene Localization

[![Browser Guide](https://img.shields.io/badge/Docs-Browser_Guide-0fe995?style=flat-square)](zeisel-browser-guide.md)
[![Zeisel Browser](https://img.shields.io/badge/Tool-Zeisel_Browser-13deba?style=flat-square)](https://storage.googleapis.com/www_zeisellab/PE_web/pe_web_test_v1.html)

Use the browser to support cell-localization hypotheses, not to validate differential expression. If it is unavailable, consult the broad marker table and the linked reference atlases; marker overlap alone is not evidence that your selected gene is expressed in a particular cell class.

## Reference Datasets

[![Admati Raw Deposit](https://img.shields.io/badge/Source-Admati_Raw_Deposit-0fe995?style=flat-square)](https://figshare.com/articles/dataset/Placenta_PE_single_cell_RNAseq_cellranger_files_raw_data_Admati_Skarbianskis_et_al_/23628471)
[![GSE198373](https://img.shields.io/badge/Reference-GSE198373-13deba?style=flat-square)](https://www.ncbi.nlm.nih.gov/geo/query/acc.cgi?acc=GSE198373)
[![HCA Interface](https://img.shields.io/badge/Reference-HCA_Interface-0fe995?style=flat-square)](https://explore.data.humancellatlas.org/projects/f83165c5-e2ea-4d15-a5cf-33f3550bffde)
[![HCA Spatial Atlas](https://img.shields.io/badge/Reference-HCA_Spatial_Atlas-13deba?style=flat-square)](https://explore.data.humancellatlas.org/projects/aecfd908-674c-4d4e-b36e-0c1ceab02245)

These resources support interpretation; they are not interchangeable disease-control cohorts. Check tissue context and pregnancy stage before making a cross-study comparison.

## Optional Extension

Use donor-by-cell-type pseudobulk only after the organizer-prepared extension is released. Donors, not individual cells, are the biological replicates.

A curated single-cell extension may also be offered later. Do not assume that an annotated object is currently available or required for the core analysis.

## Submit

[![Submission Template](https://img.shields.io/badge/Template-Final_Submission-0fe995?style=flat-square)](../../templates/final-submission.md)
[![Hypothesis Card](https://img.shields.io/badge/Template-Hypothesis_Card-13deba?style=flat-square)](../../templates/hypothesis-card.md)
[![Rubric](https://img.shields.io/badge/Docs-Submission_Rubric-0fe995?style=flat-square)](../submission-rubric.md)
[![Submission Instructions](https://img.shields.io/badge/Docs-Submission_Instructions-13deba?style=flat-square)](../../submissions/README.md)

| Deliverable | Include |
|---|---|
| Reproducible notebook or script | Data version, environment details, and documented analysis choices |
| Results package | Differential-expression results and pathway output, with two to four figures |
| Interpretation memo | One to two pages covering the comparison and limitations, plus a completed hypothesis card |
| Presentation | A five-minute explanation of the question and evidence supporting your hypothesis |

Judging considers biological rationale, reproducibility, analytical quality, hypothesis quality, and communication. Cite the datasets and tools used in your submission.

## Boundaries

Bulk expression differences may reflect changing cell proportions rather than within-cell changes. Expression-based communication hypotheses do not establish receptor activation or causality.

There is no required gene list or predetermined biological conclusion. Explain uncertainty and keep observations separate from proposed mechanisms.

## HDAG Release Details

### Package Version and Freeze Date

<!-- Intentionally blank pending HDAG release. -->

### Metadata and Data Dictionary

<!-- Intentionally blank pending HDAG release. -->

### Validation and Checksums

<!-- Intentionally blank pending HDAG release. -->
