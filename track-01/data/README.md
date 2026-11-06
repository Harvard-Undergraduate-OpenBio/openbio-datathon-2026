# Track 01 Data Package

[![Back](https://img.shields.io/badge/Back-Track_Overview-13deba?style=flat-square)](../README.md)
[![Data Guide](https://img.shields.io/badge/Guide-2_The_Data-0fe995?style=flat-square)](../2-the-data.md)

The file reference for the package. For a plain-language explanation start with [Understand the data](../2-the-data.md). For download and checksum steps see [Setup](../1-setup.md).

> **Status:** Files marked Pending will be filled in at release. Until then they are empty placeholders.

```
data/
├── track01_counts_vt.csv            Core: gene counts
├── track01_metadata_vt.csv          Core: one row per sample
├── track01_data_dictionary.md       Core: what every field means
├── interpretation/
│   ├── track01_marker_matrix.csv    Broad cell-type marker genes
│   └── zeisel_browser_guide.md      How to use the gene browser
├── extension/pseudobulk/            Optional single-cell extension
│   ├── track01_pseudobulk_counts.csv
│   └── track01_pseudobulk_metadata.csv
├── provenance/
│   ├── checksums.sha256             File fingerprints
│   ├── source_manifest.md           Sources and licenses
│   └── transformation_log.md        Every change made to the sources
└── get_gene_sets.py                 Optional: downloads Hallmark gene sets
```

## Core (required)

| File | Contents | Status |
|---|---|---|
| `track01_counts_vt.csv` | Genes as rows, 30 villous-tissue samples as columns, raw whole-number counts | Pending |
| `track01_metadata_vt.csv` | One row per sample: group, PE status, FGR, control type, gestational age, maternal age, fetal sex and other clinical fields | Pending |
| `track01_data_dictionary.md` | Every field with its unit, allowed values, missingness and source | Pending |

Source: [GSE203507](https://www.ncbi.nlm.nih.gov/geo/query/acc.cgi?acc=GSE203507), villous tissue only. Gene identifiers use a versioned annotation. Genes that could not be mapped are flagged, not removed.

## Interpretation

| File | Contents | Status |
|---|---|---|
| `interpretation/track01_marker_matrix.csv` | Broad cell-class markers from public references | Available |
| `interpretation/zeisel_browser_guide.md` | How to use the gene browser and its fallback | Available |

## Optional Extension

| File | Contents | Status |
|---|---|---|
| `extension/pseudobulk/track01_pseudobulk_counts.csv` | Counts summed by donor and cell type | Pending |
| `extension/pseudobulk/track01_pseudobulk_metadata.csv` | One row per donor: clinical group and delivery information | Pending |

Source: Admati/Skarbianskis processed single-cell data, 86,752 cells from 26 donors.

## Provenance

| File | Contents | Status |
|---|---|---|
| `provenance/checksums.sha256` | SHA-256 checksum for every released file | Pending |
| `provenance/source_manifest.md` | Original sources and their licenses | Pending |
| `provenance/transformation_log.md` | How each file was derived from its source | Pending |

After release the package is frozen. Any change gets a new version number and updated checksums. How the package was built: [data preparation plan](../reference/data-preparation.md).

## Gene Sets (optional)

MSigDB does not allow redistribution, so the Hallmark gene sets are downloaded on your own machine. From `track-01/data`, run `python get_gene_sets.py`. It writes `track01_gene_sets.gmt`, which git ignores.
