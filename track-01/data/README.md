# Track 01 Data Package

[![Back](https://img.shields.io/badge/Back-Track_Overview-13deba?style=flat-square)](../README.md)
[![Data Guide](https://img.shields.io/badge/Guide-2_The_Data-0fe995?style=flat-square)](../2-the-data.md)

The file reference for the package. For a plain-language explanation start with [Understand the data](../2-the-data.md). For setup steps see [Setup](../1-setup.md).

> **Status:** All files are available. Package version **v1.0.0**, released 2026-11-13.

## How to Get the Data

Every file is stored in this folder, so there is nothing to request or unlock.

| Option | How |
|---|---|
| Everything at once | [Download the repository as a ZIP](https://github.com/Harvard-Undergraduate-OpenBio/openbio-datathon-2026/archive/refs/heads/main.zip), unzip it and open `track-01/data` |
| With git | `git clone https://github.com/Harvard-Undergraduate-OpenBio/openbio-datathon-2026.git` |
| One file | Click a **Download** link in the tables below. If the file opens as text in your browser, right-click the link and choose **Save link as** |
| Google Colab | Run the first cell of the [workflow notebook](../notebooks/track01_workflow.ipynb). It fetches the repository for you |

To load a file straight from GitHub in Python:

```python
import pandas as pd
base = "https://github.com/Harvard-Undergraduate-OpenBio/openbio-datathon-2026/raw/main/track-01/data/"
counts = pd.read_csv(base + "track01_counts_vt.csv", index_col=0)
metadata = pd.read_csv(base + "track01_metadata_vt.csv", index_col=0)
```

## Folder Layout

```
data/
├── track01_counts_vt.csv            Core: gene counts
├── track01_metadata_vt.csv          Core: one row per sample
├── track01_data_dictionary.md       Core: what every field means
├── track01_gene_annotation.csv      Core: gene symbols mapped to HGNC
├── interpretation/
│   ├── track01_marker_matrix.csv    Broad cell-type marker genes
│   └── zeisel_browser_guide.md      How to use the gene browser
├── extension/
│   ├── pseudobulk/                  Optional: single-cell data summed by donor and cell class
│   │   ├── track01_pseudobulk_counts.csv
│   │   ├── track01_pseudobulk_metadata.csv
│   │   ├── track01_pseudobulk_donors.csv
│   │   └── track01_cell_class_map.csv
│   └── decidua/                     Optional: maternal-side tissue from the same study
│       ├── track01_counts_db.csv
│       └── track01_metadata_db.csv
├── qc/
│   └── track01_htseq_summary.csv    Sequencing summary per sample
├── provenance/
│   ├── checksums.sha256             File fingerprints
│   ├── source_manifest.md           Sources and licenses
│   ├── transformation_log.md        Every change made to the sources
│   ├── source_checksums.txt         Fingerprints of the downloaded sources
│   └── build_scripts/               Scripts the organizers used to build the package
└── get_gene_sets.py                 Optional: downloads Hallmark gene sets
```

## Core (required)

| File | Contents | Size | Get it |
|---|---|---|---|
| [`track01_counts_vt.csv`](track01_counts_vt.csv) | 26,485 genes as rows, 30 villous-tissue samples as columns, raw whole-number counts | 2.6 MB | [Download](https://github.com/Harvard-Undergraduate-OpenBio/openbio-datathon-2026/raw/main/track-01/data/track01_counts_vt.csv) |
| [`track01_metadata_vt.csv`](track01_metadata_vt.csv) | One row per sample: group, PE status, FGR, control type, gestational age, maternal age, fetal sex, birthweight, blood pressure and audit flags | 4 KB | [Download](https://github.com/Harvard-Undergraduate-OpenBio/openbio-datathon-2026/raw/main/track-01/data/track01_metadata_vt.csv) |
| [`track01_data_dictionary.md`](track01_data_dictionary.md) | Every field with its unit, allowed values, missingness and source, plus the audit findings | 14 KB | [Download](https://github.com/Harvard-Undergraduate-OpenBio/openbio-datathon-2026/raw/main/track-01/data/track01_data_dictionary.md) |
| [`track01_gene_annotation.csv`](track01_gene_annotation.csv) | Each gene symbol mapped to HGNC release 2026-10-06 (HGNC ID, current symbol, Ensembl ID). Unmapped genes are flagged, not removed | 2.1 MB | [Download](https://github.com/Harvard-Undergraduate-OpenBio/openbio-datathon-2026/raw/main/track-01/data/track01_gene_annotation.csv) |

Source: [GSE203507](https://www.ncbi.nlm.nih.gov/geo/query/acc.cgi?acc=GSE203507), villous tissue only. The count and metadata tables link through `sample_id` (`S01_VT` to `S30_VT`).

## Interpretation

| File | Contents | Size | Get it |
|---|---|---|---|
| [`interpretation/track01_marker_matrix.csv`](interpretation/track01_marker_matrix.csv) | Broad cell-class markers from public references | 1 KB | [Download](https://github.com/Harvard-Undergraduate-OpenBio/openbio-datathon-2026/raw/main/track-01/data/interpretation/track01_marker_matrix.csv) |
| [`interpretation/zeisel_browser_guide.md`](interpretation/zeisel_browser_guide.md) | How to use the gene browser and its fallback | 2 KB | [Download](https://github.com/Harvard-Undergraduate-OpenBio/openbio-datathon-2026/raw/main/track-01/data/interpretation/zeisel_browser_guide.md) |

## Optional Extension: Single-Cell Pseudobulk

| File | Contents | Size | Get it |
|---|---|---|---|
| [`extension/pseudobulk/track01_pseudobulk_counts.csv`](extension/pseudobulk/track01_pseudobulk_counts.csv) | 33,660 genes as rows, 362 donor-by-cell-class columns, summed whole-number counts | 28.9 MB | [Download](https://github.com/Harvard-Undergraduate-OpenBio/openbio-datathon-2026/raw/main/track-01/data/extension/pseudobulk/track01_pseudobulk_counts.csv) |
| [`extension/pseudobulk/track01_pseudobulk_metadata.csv`](extension/pseudobulk/track01_pseudobulk_metadata.csv) | One row per count column: donor, cell class, number of cells and the donor's clinical fields | 67 KB | [Download](https://github.com/Harvard-Undergraduate-OpenBio/openbio-datathon-2026/raw/main/track-01/data/extension/pseudobulk/track01_pseudobulk_metadata.csv) |
| [`extension/pseudobulk/track01_pseudobulk_donors.csv`](extension/pseudobulk/track01_pseudobulk_donors.csv) | One row per donor (26): clinical group and delivery information | 4 KB | [Download](https://github.com/Harvard-Undergraduate-OpenBio/openbio-datathon-2026/raw/main/track-01/data/extension/pseudobulk/track01_pseudobulk_donors.csv) |
| [`extension/pseudobulk/track01_cell_class_map.csv`](extension/pseudobulk/track01_cell_class_map.csv) | How the 46 published cell-type labels were grouped into 14 broad classes | 2 KB | [Download](https://github.com/Harvard-Undergraduate-OpenBio/openbio-datathon-2026/raw/main/track-01/data/extension/pseudobulk/track01_cell_class_map.csv) |

Source: Admati/Skarbianskis [processed single-cell data](https://figshare.com/articles/dataset/Placenta_PE_single_cell_RNAseq_dataset_Admati_Skarbianskis_et_al_/23264102), 86,752 cells from 26 donors, CC BY 4.0. Each donor counts once. The early-onset comparison has three control donors against ten PE donors, so treat it as exploratory.

The counts file is too large for GitHub to preview. Use the Download link or load it in a notebook.

## Optional Extension: Decidua Basalis

| File | Contents | Size | Get it |
|---|---|---|---|
| [`extension/decidua/track01_counts_db.csv`](extension/decidua/track01_counts_db.csv) | 26,485 genes as rows, 27 decidua-basalis samples as columns, raw whole-number counts | 2.4 MB | [Download](https://github.com/Harvard-Undergraduate-OpenBio/openbio-datathon-2026/raw/main/track-01/data/extension/decidua/track01_counts_db.csv) |
| [`extension/decidua/track01_metadata_db.csv`](extension/decidua/track01_metadata_db.csv) | One row per decidua sample, same fields as the villous metadata | 4 KB | [Download](https://github.com/Harvard-Undergraduate-OpenBio/openbio-datathon-2026/raw/main/track-01/data/extension/decidua/track01_metadata_db.csv) |

Source: [GSE203507](https://www.ncbi.nlm.nih.gov/geo/query/acc.cgi?acc=GSE203507). The decidua basalis is the maternal tissue the placenta attaches to. 27 of the 30 placentas have a decidua sample. `donor_id` links it to the villous sample from the same pregnancy, so the two are not independent.

## Quality Control

| File | Contents | Size | Get it |
|---|---|---|---|
| [`qc/track01_htseq_summary.csv`](qc/track01_htseq_summary.csv) | Reads assigned to genes and HTSeq counters for each bulk sample | 3 KB | [Download](https://github.com/Harvard-Undergraduate-OpenBio/openbio-datathon-2026/raw/main/track-01/data/qc/track01_htseq_summary.csv) |

## Provenance

| File | Contents | Size | Get it |
|---|---|---|---|
| [`provenance/checksums.sha256`](provenance/checksums.sha256) | SHA-256 checksum for every released file | 2 KB | [Download](https://github.com/Harvard-Undergraduate-OpenBio/openbio-datathon-2026/raw/main/track-01/data/provenance/checksums.sha256) |
| [`provenance/source_manifest.md`](provenance/source_manifest.md) | Original sources and their licenses | 4 KB | [Download](https://github.com/Harvard-Undergraduate-OpenBio/openbio-datathon-2026/raw/main/track-01/data/provenance/source_manifest.md) |
| [`provenance/transformation_log.md`](provenance/transformation_log.md) | How each file was derived from its source | 7 KB | [Download](https://github.com/Harvard-Undergraduate-OpenBio/openbio-datathon-2026/raw/main/track-01/data/provenance/transformation_log.md) |
| [`provenance/source_checksums.txt`](provenance/source_checksums.txt) | SHA-256 checksum for every downloaded source file | 7 KB | [Download](https://github.com/Harvard-Undergraduate-OpenBio/openbio-datathon-2026/raw/main/track-01/data/provenance/source_checksums.txt) |

The package is frozen at v1.0.0. Any change gets a new version number and updated checksums. How the package was built: [data preparation plan](../reference/data-preparation.md).

## Check Your Copy

From `track-01/data`, run:

```bash
sha256sum -c provenance/checksums.sha256       # Linux or Windows WSL
shasum -a 256 -c provenance/checksums.sha256   # macOS
```

Every line should end in `OK`.

## Gene Sets (optional)

MSigDB does not allow redistribution, so the Hallmark gene sets are downloaded on your own machine. From `track-01/data`, run `python get_gene_sets.py`. It writes `track01_gene_sets.gmt`, which git ignores.
