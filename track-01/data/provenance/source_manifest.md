# Track 01 Source Manifest

[![Back](https://img.shields.io/badge/Back-Data_Package-13deba?style=flat-square)](../README.md)

Package version: **v1.0.0**. All sources were downloaded on 2026-11-13. SHA-256 checksums of every downloaded source file are in [`source_checksums.txt`](source_checksums.txt).

## Sources Used to Build Released Files

| Source | What was downloaded | Used for | License or terms |
|---|---|---|---|
| NCBI GEO [GSE203507](https://www.ncbi.nlm.nih.gov/geo/query/acc.cgi?acc=GSE203507) | `GSE203507_RAW.tar` (57 HTSeq count files: 30 villous tissue and 27 decidua basalis) and `GSE203507_series_matrix.txt.gz` (sample metadata) from the [GEO FTP folder](https://ftp.ncbi.nlm.nih.gov/geo/series/GSE203nnn/GSE203507/) | `track01_counts_vt.csv`, `track01_metadata_vt.csv`, `qc/track01_htseq_summary.csv`, `extension/decidua/` | Public GEO record. See the [GEO disclaimer](https://www.ncbi.nlm.nih.gov/geo/info/disclaimer.html) for NCBI's data use terms. Cite the GEO accession and the original authors |
| Figshare [23264102](https://figshare.com/articles/dataset/Placenta_PE_single_cell_RNAseq_dataset_Admati_Skarbianskis_et_al_/23264102), DOI [10.6084/m9.figshare.23264102.v1](https://doi.org/10.6084/m9.figshare.23264102.v1) | `sc_PE_allcells_with_metadata_29-May-2023.txt.zip` (processed genes-by-cells UMI table with per-cell metadata, 256 MB zipped) | `extension/pseudobulk/` | [CC BY 4.0](https://creativecommons.org/licenses/by/4.0/). Attribution required. The released pseudobulk tables are an adaptation |
| HGNC [complete set archive](https://storage.googleapis.com/public-download-files/hgnc/archive/archive/monthly/tsv/hgnc_complete_set_2026-10-06.txt), release 2026-10-06 | `hgnc_complete_set_2026-10-06.txt` | `track01_gene_annotation.csv` | [CC0](https://www.genenames.org/about/license/). HGNC recommends attribution |

GSE203507 was submitted by Ackerman WE, Buhimschi IA and Buhimschi CS (University of Illinois Chicago College of Medicine) and became public on 2023-08-25. GEO links it to PubMed records [36987911](https://pubmed.ncbi.nlm.nih.gov/36987911/) and [41641529](https://pubmed.ncbi.nlm.nih.gov/41641529/).

## Sources Linked but Not Distributed

| Source | Role | License or terms |
|---|---|---|
| Figshare [23628471](https://figshare.com/articles/dataset/Placenta_PE_single_cell_RNAseq_cellranger_files_raw_data_Admati_Skarbianskis_et_al_/23628471) | Raw Cell Ranger archive for the single-cell study (1.3 GB). Organizer-side only. It was not downloaded for this build | CC BY 4.0 |
| [Zeisel/Admati gene browser](https://storage.googleapis.com/www_zeisellab/PE_web/pe_web_test_v1.html) | Required interpretation tool | See browser |
| NCBI GEO [GSE198373](https://www.ncbi.nlm.nih.gov/geo/query/acc.cgi?acc=GSE198373) | Healthy second-trimester atlas, reference only | GEO data use terms |
| HCA [fetal-maternal interface](https://explore.data.humancellatlas.org/projects/f83165c5-e2ea-4d15-a5cf-33f3550bffde) | Healthy first-trimester reference | CC BY 4.0 |
| HCA [spatial multiomics trophoblast atlas](https://explore.data.humancellatlas.org/projects/aecfd908-674c-4d4e-b36e-0c1ceab02245) | Trophoblast development reference | HCA Data Release Policy |
| MSigDB Hallmark gene sets | Optional, downloaded by each team with `get_gene_sets.py` | MSigDB license, no redistribution |

## Files Carried Over Unchanged in Origin

`interpretation/track01_marker_matrix.csv` and `interpretation/zeisel_browser_guide.md` were already in the repository before this build. The only change to the marker matrix is recorded in the [transformation log](transformation_log.md).
