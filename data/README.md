# Data Directory

This directory contains manifests, checksums, and small toy subsets — **not full raw datasets**.

## Contents

- `manifest.csv` — One row per data resource with metadata (dataset ID, track, role, source URL, format, license, etc.)
- `checksums/SHA256SUMS.txt` — Integrity verification for OpenBio-derived artifacts
- `sample_data/` — Small toy subsets for testing notebooks

## Rules

- **Do not commit large raw datasets.** The `.gitignore` excludes `.h5ad`, `.rds`, `.mtx`, and other large formats.
- **Do not store DHS microdata.** Only derived/aggregated data is permitted.
- **Do not store repackaged HCA data.** Link to canonical HCA sources instead.

## Downloading Full Data

Use the download scripts referenced in each dataset's entry in the [Track 1 data catalog](../docs/track-1-computational-biology/data-catalog.md) or [Track 2 data catalog](../docs/track-2-global-health/data-catalog.md).
