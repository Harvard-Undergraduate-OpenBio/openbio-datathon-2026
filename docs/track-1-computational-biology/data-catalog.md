# Track 01 Data Catalog

[![Download Guide](https://img.shields.io/badge/Data-Download_Guide-0fe995?style=flat-square)](../../data/track-01/README.md)
[![Manifest](https://img.shields.io/badge/Data-Manifest-13deba?style=flat-square)](../../data/manifest.csv)

| Resource | Role | What it is | In the download? |
|---|---|---|---|
| [GSE203507](https://www.ncbi.nlm.nih.gov/geo/query/acc.cgi?acc=GSE203507) | Required core | Bulk RNA-seq of 30 placental villous-tissue samples with clinical metadata | Yes, as prepared counts and metadata |
| [Zeisel/Admati gene browser](https://storage.googleapis.com/www_zeisellab/PE_web/pe_web_test_v1.html) | Required interpretation | Gene lookup across placental cell types; use for at least three genes | Linked |
| [Admati/Skarbianskis single-cell data](https://figshare.com/articles/dataset/Placenta_PE_single_cell_RNAseq_cellranger_files_raw_data_Admati_Skarbianskis_et_al_/23628471) | Optional extension | 86,752 labeled placental cells from 26 donors | Yes, as donor-by-cell-type pseudobulk |
| [GSE198373](https://www.ncbi.nlm.nih.gov/geo/query/acc.cgi?acc=GSE198373) | Reference | Healthy second-trimester placental atlas, four donors, about 50,000 cells | Linked |
| [HCA fetal-maternal interface](https://explore.data.humancellatlas.org/projects/f83165c5-e2ea-4d15-a5cf-33f3550bffde) | Reference | Healthy first-trimester placenta, decidua and maternal blood; 16 donors, about 70,000 cells; CC BY 4.0 | Linked |
| [HCA spatial multiomics trophoblast atlas](https://explore.data.humancellatlas.org/projects/aecfd908-674c-4d4e-b36e-0c1ceab02245) | Reference | Trophoblast development across stages; 34 donors, about 325,700 cells | Linked |

## Data Use

- Each source keeps its own terms. The repository's MIT license covers code and documentation only.
- Cite every dataset you use. See [citations](citations.md).
