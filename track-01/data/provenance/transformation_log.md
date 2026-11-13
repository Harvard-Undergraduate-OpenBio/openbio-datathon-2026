# Track 01 Transformation Log

[![Back](https://img.shields.io/badge/Back-Data_Package-13deba?style=flat-square)](../README.md)

Package version: **v1.0.0**, built 2026-11-13. Every change made between the downloaded sources and the released files is listed here. The scripts that performed them are in [`build_scripts/`](build_scripts). Sources and licenses are in the [source manifest](source_manifest.md).

No released file contains a differential-expression table, a pathway result, a gene ranking or a recommended interpretation.

## Bulk Core and Decidua (GSE203507)

Script: `build_scripts/build_bulk.py`

| # | Step | Detail |
|---|---|---|
| 1 | Download | `GSE203507_RAW.tar` and `GSE203507_series_matrix.txt.gz` from GEO FTP. Checksums recorded in `source_checksums.txt` |
| 2 | Read count files | 57 files, one per sample. Each has 26,490 rows of `gene<TAB>count`. Quotes and Windows line endings removed |
| 3 | Split off HTSeq counters | The five rows starting with `__` are not genes. Moved to `qc/track01_htseq_summary.csv` |
| 4 | Assemble matrix | Joined on gene symbol into 26,485 genes x 57 samples. All files share the same gene list in the same order. No value was missing after the join |
| 5 | Duplicate gene rule | Rule: if a symbol appears more than once in a file, stop the build. No duplicates were found, so no rows were merged or dropped |
| 6 | Check values | All counts are nonnegative integers |
| 7 | Rename samples | Columns named `S01_VT` style from the GEO file names. GEO accessions are kept in the metadata |
| 8 | Split by tissue | 30 villous columns to `track01_counts_vt.csv`. 27 decidua columns to `extension/decidua/track01_counts_db.csv` |
| 9 | Parse metadata | `!Sample_characteristics_ch1` rows turned into one row per sample. `N/A` written as `NA`. Nothing imputed |
| 10 | Standardize units | Gestational age `weeks.days` kept as published and also converted to decimal weeks (`weeks + days / 7`). Birthweight bins split into lower and upper edges in grams. Blood pressure kept in mmHg |
| 11 | Derive group fields | `pe_status`, `pe_onset`, `fgr_status`, `control_type` and `preterm_delivery` derived from `group` and gestational age. Rules are in the data dictionary |
| 12 | Audit | Plausibility rules applied and written to `qc_flags`. No value changed. Findings listed in the data dictionary |
| 13 | Hold back race and ethnicity | `maternal race` and `maternal ethnicity` are not released pending clinical reviewer sign-off |
| 14 | Gene mapping | Source symbols matched to HGNC release 2026-10-06: approved symbol, then previous symbol, then alias. Ambiguous and unmapped symbols are flagged in `track01_gene_annotation.csv`. No gene was removed from the count tables |

Fields dropped from GEO because they are identical for every sample or describe the laboratory: sample status and dates, organism, molecule, extraction and library protocols, data processing text, platform, instrument, submitter contact details, BioSample and SRA links.

Source processing as stated by the authors on GEO: adapter trimming with Trimmomatic 0.39, alignment to UCSC hg38 with TopHat2 2.0.14, counting with HTSeq 0.11.2 using the Illumina iGenomes annotation.

## Single-Cell Pseudobulk (Admati/Skarbianskis)

Scripts: `build_scripts/aggregate_sc.py`, then `build_scripts/build_pseudobulk.py`

| # | Step | Detail |
|---|---|---|
| 1 | Download | Processed table from Figshare 23264102. MD5 matched the value published by Figshare. The raw Cell Ranger archive was not used |
| 2 | Read | 23 metadata rows and 33,694 gene rows across 86,752 cells. All values are nonnegative integers |
| 3 | Check donors | 26 donors and 31 libraries. Five donors have two libraries. Every clinical field is constant within a donor |
| 4 | Sum by donor and cell type | UMI counts summed over all cells sharing a donor and a published cell-type label. Libraries from one donor are summed together, so technical replicates never count as separate people |
| 5 | Duplicate gene rule | 34 gene symbols appear on more than one row in the source. Rule: sum the rows that share a symbol. Result: 33,660 unique genes. The symbols are listed below |
| 6 | Group into broad classes | The 46 published labels were grouped into 14 broad classes by summing. The full mapping is released as `track01_cell_class_map.csv` |
| 7 | Check totals | The grand total of counts is identical before and after aggregation (962,152,952) |
| 8 | Donor metadata | Indicator columns recoded into labelled categories. Decimal weeks, grams and percentiles kept as published. `labor_induction` is `NA` for 7 donors where neither indicator is set |
| 9 | Exploratory label | Early-onset donors (3 control and 10 PE) carry `early_onset_comparison = exploratory_3_control_vs_10_PE` |
| 10 | Audit | Plausibility rules written to `qc_flags`. No value changed |

No cells or genes were filtered. Columns built from very few cells are kept and can be identified with `n_cells`.

Duplicate symbols summed in step 5: AKR1C3, ATRIP, BLOC1S5, C11orf71, C17orf100, C1QTNF9B-AS1, CAPS, CCDC7, CFAP99, CRHR1, CYB561D2, ECSCR, FAM231C, FBF1, IGHV2-70, LINC00864, LINC01297, LINC01422, LINC01481, MATR3, PABPC1L2B-AS1, PGM5-AS1, PIK3R3, PRICKLE2-AS1, PRICKLE4, RABL6, RAET1E-AS1, RGS5, SERPINA3, SPATA13, TBC1D26, TIMM10B, TMBIM4, TMEM256-PLSCR3.

## Marker Matrix

| # | Step | Detail |
|---|---|---|
| 1 | Symbol correction | `HLAG` changed to `HLA-G` and `ERVW1` changed to `ERVW-1` so the markers match approved HGNC symbols and the count tables. No marker was added or removed |

Known gap: the marker `TRAC` has no row in the source bulk count files, so it cannot be looked up in the bulk tables. It is present in the pseudobulk table.

## Verification

| Check | Result |
|---|---|
| `track01_workflow.ipynb` runs top to bottom on the released files with the decision cells left blank | Pass |
| The same notebook runs through differential expression when test values are entered (scratch copy, outputs discarded) | Pass |
| Pseudobulk tables filter to one cell class and run through PyDESeq2 (scratch copy, outputs discarded) | Pass |
| `track01_workflow.Rmd` | Not run. R was not available in the build environment. It reads the same files with the same layout |
| Released files contain no differential-expression table, pathway result or interpretation | Pass |
| Clinical reviewer sign-off on race and ethnicity | Outstanding, fields held back |

## Change Policy

The package is frozen at v1.0.0. Any change requires a new version number and updated checksums in `checksums.sha256`.
