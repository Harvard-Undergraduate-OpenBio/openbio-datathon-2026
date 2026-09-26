# Track 1: Data Dictionary

This document defines every metadata field expected in the OpenBio-provided challenge objects.

## Cell-Level Metadata

| Field | Type | Source | Description |
|---|---|---|---|
| `cell_id` | string | OpenBio-derived | Unique cell identifier |
| `donor_id` | string | Source-provided | Donor identifier |
| `sample_id` | string | Source-provided | Sample identifier |
| `dataset_id` | string | OpenBio-derived | Stable dataset name (e.g., `PE_PLACENTA_ADMATI_2023`) |
| `condition` | string | Source-provided | Experimental condition |
| `disease_status` | string | Source-provided | `preeclampsia`, `control`, or `healthy_reference` |
| `gestational_age_weeks` | float | Source-provided | Gestational age in weeks (if available) |
| `gestational_age_bin` | string | OpenBio-derived | `early`, `term`, `postpartum`, or `unknown` |
| `tissue` | string | Source-provided | `placenta`, `decidua`, `maternal_blood`, `PBMC` |
| `compartment` | string | OpenBio-derived | `fetal`, `maternal`, or `unknown` |
| `cell_type_original` | string | Source-provided | Cell-type label from original publication |
| `cell_type_harmonized` | string | OpenBio-derived | Cross-dataset harmonized cell-type label |
| `cell_type_confidence` | float | OpenBio-derived | Annotation confidence score (0–1) |
| `sequencing_platform` | string | Source-provided | Platform (e.g., `10x_3p_v3`) |
| `batch` | string | OpenBio-derived | Batch identifier for technical covariate control |
| `sex_if_available` | string | Source-provided | `male`, `female`, or `unknown` (fetal sex) |
| `maternal_or_fetal_origin` | string | OpenBio-derived | `maternal` or `fetal` |
| `included_in_primary_analysis` | bool | OpenBio-derived | Whether cell passes all QC filters |

## Provenance Fields

For every field, indicate whether the value is:
- **source-provided:** Directly from the original dataset
- **OpenBio-derived:** Computed or harmonized by OpenBio
- **unknown:** Not available and not inferable
- **suppressed:** Intentionally withheld for privacy
- **not applicable:** Does not apply to this dataset

## Important Rule

Do not fabricate or infer missing clinical variables. If a field is unknown, mark it as `unknown`.
