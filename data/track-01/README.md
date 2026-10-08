# Track 01 Data Package

[![Participant Guide](https://img.shields.io/badge/Guide-Track_01-13deba?style=flat-square)](../../docs/track-1-computational-biology/README.md)
[![Track 01](https://img.shields.io/badge/Track-01-0fe995?style=flat-square)](../../docs/track-1-computational-biology/overview.md)
[![Data Catalog](https://img.shields.io/badge/Docs-Data_Catalog-13deba?style=flat-square)](../../docs/track-1-computational-biology/data-catalog.md)
[![Starter Notebooks](https://img.shields.io/badge/Code-Starter_Notebooks-0fe995?style=flat-square)](../../notebooks/track-1)
[![Browser Guide](https://img.shields.io/badge/Docs-Browser_Guide-13deba?style=flat-square)](../../docs/track-1-computational-biology/zeisel-browser-guide.md)

Participant data package for Track 01. Files that HDAG prepares are pending release and are currently blank.

## Contents

| File | Status | Description |
|---|---|---|
| `track01_counts_vt.csv` | Pending HDAG | Villous-tissue raw count matrix, genes by 30 samples |
| `track01_metadata_vt.csv` | Pending HDAG | One row per sample with clinical fields |
| `track01_data_dictionary.md` | Pending HDAG | Field definitions and allowed values |
| `track01_reference_genes.csv` | Available (v0.1.0) | Orientation-only reference genes by program |
| `interpretation/track01_marker_matrix.csv` | Available (v0.1.0) | Broad cell-class markers for gene localization |
| `extension/pseudobulk/` | Pending HDAG | Donor-by-cell-type pseudobulk matrices |
| `provenance/` | Pending HDAG | Checksums and provenance records |

## Gene Sets

MSigDB terms do not permit redistribution here. Run `python track01_fetch_gene_sets.py` from this directory to download the Hallmark collection and write `track01_gene_sets.gmt` locally.

## Rules

- Do not commit downloaded datasets or generated gene sets to this repository.
- Verify `provenance/checksums.sha256` against the released package before analysis.
