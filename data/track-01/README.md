# Track 01 Download Guide

[![Participant Guide](https://img.shields.io/badge/Guide-Track_01-0fe995?style=flat-square)](../../docs/track-1-computational-biology/README.md)
[![Starter Questions](https://img.shields.io/badge/Docs-Starter_Questions-13deba?style=flat-square)](../../docs/track-1-computational-biology/research-questions.md)
[![Starter Notebooks](https://img.shields.io/badge/Code-Starter_Notebooks-0fe995?style=flat-square)](../../notebooks/track-1)

Everything you need for Track 01 is in this folder or linked below. You do not need sequencing reads, raw Cell Ranger files or any GEO download.

> **Status:** Files marked Pending will be filled in at data release. Until then they are empty placeholders.

## 1. Get the Package

At release, download the versioned ZIP from the repository's Releases page. You can also clone the repository:

```bash
git clone https://github.com/Harvard-Undergraduate-OpenBio/openbio-datathon-2026.git
cd openbio-datathon-2026/data/track-01
```

Keep the folder structure as is so the starter notebooks find the files.

## 2. Verify the Files

Every released file has a SHA-256 checksum. From `data/track-01`, run:

```bash
sha256sum -c provenance/checksums.sha256       # Linux or Windows WSL
shasum -a 256 -c provenance/checksums.sha256   # macOS
```

Every line should read `OK`. If one does not, download the package again or contact the organizers.

## 3. What Is Inside

```
data/track-01/
├── track01_counts_vt.csv            # core counts
├── track01_metadata_vt.csv          # core sample metadata
├── track01_data_dictionary.md       # field definitions
├── interpretation/
│   ├── track01_marker_matrix.csv    # broad cell-class markers
│   └── zeisel_browser_guide.md      # browser how-to and fallback
├── extension/pseudobulk/            # optional single-cell extension
│   ├── track01_pseudobulk_counts.csv
│   └── track01_pseudobulk_metadata.csv
└── provenance/
    ├── checksums.sha256
    ├── source_manifest.md           # sources and licenses
    └── transformation_log.md        # every change made to the sources
```

### Core Files (required)

| File | Contents | Status |
|---|---|---|
| `track01_counts_vt.csv` | Genes as rows, 30 villous-tissue samples as columns, integer raw counts | Pending |
| `track01_metadata_vt.csv` | One row per sample: group, PE status, FGR, control type, gestational age, maternal age, fetal sex and other clinical fields | Pending |
| `track01_data_dictionary.md` | Every field with its unit, allowed values, missingness and source | Pending |

Source: [GSE203507](https://www.ncbi.nlm.nih.gov/geo/query/acc.cgi?acc=GSE203507), villous tissue only.

How to read the core files:

- Sample IDs match between the count columns and the metadata rows.
- Missing values are `NA`. Nothing has been imputed.
- Units are standardized: weeks for gestational age, mmHg for blood pressure, grams or percentiles for birthweight.
- Gene identifiers use a versioned annotation. Genes that could not be mapped are flagged, not removed.
- Implausible values are flagged in the data dictionary, not corrected.

### Interpretation Files

| File | Contents | Status |
|---|---|---|
| `interpretation/track01_marker_matrix.csv` | Broad cell-class markers from public references | Available |
| `interpretation/zeisel_browser_guide.md` | How to use the gene browser and its fallback | Available |

### Optional Extension

| File | Contents | Status |
|---|---|---|
| `extension/pseudobulk/track01_pseudobulk_counts.csv` | Counts summed by donor and cell type | Pending |
| `extension/pseudobulk/track01_pseudobulk_metadata.csv` | One row per donor: clinical group and delivery information | Pending |

Source: Admati/Skarbianskis processed single-cell data, 86,752 cells from 26 donors. Each donor is one biological sample. The early-onset comparison is exploratory (three control donors against ten PE donors).

### Provenance

| File | Contents | Status |
|---|---|---|
| `provenance/checksums.sha256` | SHA-256 checksum for every released file | Pending |
| `provenance/source_manifest.md` | Original sources and their licenses | Pending |
| `provenance/transformation_log.md` | How each file was derived from its source | Pending |

## 4. Linked Resources (not downloaded)

| Resource | Use it for | Link |
|---|---|---|
| Zeisel/Admati gene browser | Seeing which placental cells express a gene (required for at least three genes) | [Open browser](https://storage.googleapis.com/www_zeisellab/PE_web/pe_web_test_v1.html) |
| GSE198373 | Healthy second-trimester placental atlas, four donors | [GEO](https://www.ncbi.nlm.nih.gov/geo/query/acc.cgi?acc=GSE198373) |
| HCA fetal-maternal interface | Healthy first-trimester map of placenta, decidua and maternal blood, 16 donors (CC BY 4.0) | [Human Cell Atlas](https://explore.data.humancellatlas.org/projects/f83165c5-e2ea-4d15-a5cf-33f3550bffde) |
| HCA spatial multiomics trophoblast atlas | Trophoblast development across stages, 34 donors | [Human Cell Atlas](https://explore.data.humancellatlas.org/projects/aecfd908-674c-4d4e-b36e-0c1ceab02245) |

These are context, not competition data. They come from healthy pregnancies at earlier stages, so do not use them as control groups.

## 5. Optional: Gene Sets

MSigDB terms do not allow redistribution. To use Hallmark gene sets, run this from `data/track-01`:

```bash
python track01_fetch_gene_sets.py
```

It writes `track01_gene_sets.gmt` locally. Do not commit it.

## Versioning

After release the package is frozen. Any change gets a new version number and updated checksums, recorded in `provenance/transformation_log.md`.

How the package was built: [data preparation plan](../../docs/track-1-computational-biology/data-preparation.md).
