# Track 1: Data Catalog

## Dataset Manifest

[![Primary Dataset](https://img.shields.io/badge/Role-Primary-0fe995?style=flat-square)](https://figshare.com/articles/dataset/Placenta_PE_single_cell_RNAseq_cellranger_files_raw_data_Admati_Skarbianskis_et_al_/23628471)
[![HCA Reference](https://img.shields.io/badge/Role-Reference-13deba?style=flat-square)](https://explore.data.humancellatlas.org/projects/f83165c5-e2ea-4d15-a5cf-33ff3550bffde)
[![GEO Extension](https://img.shields.io/badge/Role-Extension-0fe995?style=flat-square)](https://www.ncbi.nlm.nih.gov/geo/query/acc.cgi?acc=GSE192693)

| Dataset ID | Role | Source Title | Source URL | Access Level | Format | Raw/Processed | Species | Tissue | Disease Context | Donor Count | Cell Count (approx.) | License | Distribution Policy | Citation | Notes |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| PE_PLACENTA_ADMATI_2023 | Required primary | Placenta PE single-cell RNA-seq | https://figshare.com/articles/dataset/Placenta_PE_single_cell_RNAseq_cellranger_files_raw_data_Admati_Skarbianskis_et_al_/23628471 | Public direct download | mtx, tsv | Raw (Cell Ranger) | Human | Placenta | PE and matched controls | TBD | TBD | TBD | Link-only + OpenBio-derived processed artifact | Admati, Skarbianskis et al. 2023 | 1.19 GB; provide processed starter object |
| HCA_FETAL_MATERNAL_INTERFACE | Required reference | First-trimester fetal-maternal interface atlas | https://explore.data.humancellatlas.org/projects/f83165c5-e2ea-4d15-a5cf-33ff3550bffde | Public (HCA) | h5ad | Processed | Human | Placenta, decidua, maternal blood | Healthy reference | 16 | ~70,000 | HCA Data Release Policy / CC BY 4.0 | Link-only | Vento-Tormo et al. 2018 | Early-pregnancy atlas; not direct disease-matched comparison |
| HCA_SPATIAL_TROPHOBLAST | Optional advanced | Spatial multiomics trophoblast atlas | https://explore.data.humancellatlas.org/projects/aecfd908-674c-4d4e-b36e-0c1ceab02245 | Public (HCA) | h5ad, spatial | Processed | Human | Placenta, decidua | Healthy reference | 34 | ~325,700 | HCA Data Release Policy / CC BY 4.0 | Link-only | Refer to HCA project page | Includes spatial/multiomic files; technically heavier |
| GSE192693 | Optional extension | Maternal PBMC scRNA-seq in PE and controls | https://www.ncbi.nlm.nih.gov/geo/query/acc.cgi?acc=GSE192693 | Public (GEO) | Raw + processed | Both | Human | PBMC | PE and controls | TBD | ~80,429 | GEO data use terms | Link-only | Refer to GEO accession | T cells, B cells, NK cells, monocytes; stretch question for placenta-PBMC link |
| GSE87692 | Background/methodological | Trophoblast-endometrial communication study | https://www.ncbi.nlm.nih.gov/geo/query/acc.cgi?acc=GSE87692 | Public (GEO) | Raw + processed | Both | Human | Trophoblast, endometrium | Communication study | TBD | TBD | GEO data use terms | Link-only | Refer to GEO accession | Historical benchmark; verify before required use |
| GSE198373 | Optional reference | Regionally distinct trophoblast placenta atlas | https://www.ncbi.nlm.nih.gov/geo/query/acc.cgi?acc=GSE198373 | Public (GEO) | mtx, tsv | Processed | Human | Placenta villi, basal plate, smooth chorion | Healthy reference | 4 | TBD | GEO data use terms | Link-only | Marsh et al. 2022 | Regional atlas of trophoblast across villous and smooth chorion regions |

## Access Notes

- **HCA datasets** are governed by the HCA Data Release Policy and CC BY 4.0. Do not assume unrestricted redistribution of repackaged copies. Link to canonical sources.
- **GEO datasets** (GSE192693, GSE87692) are subject to NCBI GEO data use terms. Verify exact file types and reuse terms before assigning as required resources.

## Interpretation Resources

[![Zeisel Browser](https://img.shields.io/badge/Tool-Zeisel_Browser-13deba?style=flat-square)](zeisel-browser-guide.md)
[![Marker Matrix](https://img.shields.io/badge/Data-Marker_Matrix-0fe995?style=flat-square)](../../data/track-01/interpretation/track01_marker_matrix.csv)

The Zeisel browser and the marker matrix in the [Track 01 data package](../../data/track-01/README.md) support gene localization. See the [browser guide](zeisel-browser-guide.md) for permitted uses and the fallback plan.

## OpenBio-Derived Challenge Artifacts

The following processed artifacts will be created by OpenBio and made available to participants:

| Artifact | Format | Description |
|---|---|---|
| Processed PE placenta object | `.h5ad` | Annotated, QC-filtered AnnData object with cell-type labels and harmonized metadata |
| Processed healthy reference object | `.h5ad` | Annotated reference atlas subset relevant to maternal-fetal interface |
| Toy training subset | `.h5ad` | Small subset (~5,000 cells) that runs in under 10 minutes on a laptop |
| Cell-level metadata table | `.csv` | Donor, sample, condition, cell-type, and QC columns |
| Donor-level metadata table | `.csv` | One row per donor with clinical and technical variables |
| SHA256 checksums | `SHA256SUMS.txt` | Integrity verification for all OpenBio-derived artifacts |
