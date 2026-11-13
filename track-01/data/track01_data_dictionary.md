# Track 01 Data Dictionary

[![Back](https://img.shields.io/badge/Back-Data_Package-13deba?style=flat-square)](README.md)

Package version: **v1.0.0** (built 2026-11-13). Every released field is listed here with its unit, allowed values, missingness and source. Missing values are written `NA` and are never filled in. Values that look implausible are flagged in a `qc_flags` column and in the audit tables below. Nothing was corrected.

## Contents

- [Bulk core: counts](#bulk-core-counts-track01_counts_vtcsv)
- [Bulk core: metadata](#bulk-core-metadata-track01_metadata_vtcsv)
- [Gene annotation](#gene-annotation-track01_gene_annotationcsv)
- [QC: HTSeq summary](#qc-htseq-summary-qctrack01_htseq_summarycsv)
- [Extension: decidua basalis](#extension-decidua-basalis-extensiondecidua)
- [Extension: single-cell pseudobulk](#extension-single-cell-pseudobulk-extensionpseudobulk)
- [Audit findings](#audit-findings)
- [Fields not released](#fields-not-released)

## Bulk Core: Counts (`track01_counts_vt.csv`)

| Item | Value |
|---|---|
| Shape | 26,485 genes (rows) x 30 samples (columns) |
| Row index | `gene`: gene symbol exactly as written by the original authors (UCSC hg38, Illumina iGenomes annotation) |
| Columns | `S01_VT` to `S30_VT`, matching `sample_id` in the metadata |
| Values | Raw read counts from HTSeq 0.11.2. Nonnegative integers. Not normalized |
| Missingness | None. Every gene has a count in every sample |
| Duplicate genes | None in the source files |
| Source | GEO [GSE203507](https://www.ncbi.nlm.nih.gov/geo/query/acc.cgi?acc=GSE203507), files `GSM6175116` to `GSM6175145` (`*_VT.count.txt.gz`) |

The five HTSeq summary rows (`__no_feature`, `__ambiguous`, `__too_low_aQual`, `__not_aligned`, `__alignment_not_unique`) are not genes. They were moved to `qc/track01_htseq_summary.csv`.

## Bulk Core: Metadata (`track01_metadata_vt.csv`)

One row per villous-tissue sample. The index column `sample_id` matches the count column names. Source for every field: GEO series matrix `GSE203507_series_matrix.txt.gz` (`!Sample_characteristics_ch1` unless stated).

| Field | Type | Unit | Allowed values | Missing | Derivation |
|---|---|---|---|---|---|
| `sample_id` | text | | `S01_VT` to `S30_VT` | 0 | Study sample number plus tissue code |
| `geo_accession` | text | | `GSM6175116` to `GSM6175145` | 0 | `!Sample_geo_accession` |
| `donor_id` | text | | `S01` to `S30` | 0 | Study sample number from `!Sample_title`. Links a villous sample to its decidua sample from the same placenta |
| `group` | category | | `EOPE`, `EOPE+FGR`, `FGR`, `iPTB`, `TB` | 0 | `clinical group`, unchanged |
| `pe_status` | category | | `PE`, `no_PE` | 0 | `PE` if `group` is `EOPE` or `EOPE+FGR` |
| `pe_onset` | category | | `early_onset`, `not_applicable` | 0 | All PE in this study is early onset by design |
| `fgr_status` | category | | `FGR`, `no_FGR` | 0 | `FGR` if `group` contains `FGR` |
| `control_type` | category | | `preterm_birth`, `term_birth`, `not_control` | 0 | `iPTB` becomes `preterm_birth`, `TB` becomes `term_birth`. `FGR` is a normotensive case group, so it is `not_control` |
| `ga_delivery_source` | text | weeks.days | as published | 0 | `gestational age_at_delivery_(weeks.days)`, unchanged. `33.4` means 33 weeks and 4 days, not 33.4 weeks |
| `ga_delivery_completed_weeks` | integer | weeks | 26 to 39 | 0 | Part before the dot |
| `ga_delivery_extra_days` | integer | days | 0 to 6 expected | 0 | Part after the dot, 0 if absent. One value is 7 (see audit) |
| `ga_delivery_weeks` | decimal | weeks | 26.0 to 39.4 | 0 | `completed_weeks + extra_days / 7`, rounded to 3 decimals |
| `preterm_delivery` | category | | `yes`, `no` | 0 | `yes` if `ga_delivery_weeks` < 37 |
| `maternal_age_years` | integer | years | 15 to 39 | 0 | `age of_mother_(years)` |
| `birthweight_interval_g` | text | grams | `400-500` to `1900-2000` | 5 | `birthweight interval_(grams)`. GEO publishes 100 g bins, not exact weights. `N/A` becomes `NA` |
| `birthweight_lower_g` | integer | grams | 400 to 1900 | 5 | Lower edge of the bin |
| `birthweight_upper_g` | integer | grams | 500 to 2000 | 5 | Upper edge of the bin |
| `fetal_sex` | category | | `female`, `male` | 0 | `assigned neonatal_sex`, lowercased |
| `sbp_max_mmhg` | integer | mmHg | 92 to 208 | 5 | `highest antepartum_systolic_blood_pressure_(mm_hg)` |
| `dbp_max_mmhg` | integer | mmHg | 57 to 122 | 5 | `highest antepartum_diastolic_blood_pressure_(mm_hg)` |
| `qc_flags` | text | | `none` or `;`-separated flags below | 0 | Organizer audit. Does not change any other value |

Group sizes: EOPE 8, EOPE+FGR 7, FGR 5, iPTB 5, TB 5.

All five missing birthweight and blood pressure values are the term-birth (`TB`) controls S26 to S30. GEO lists them as `N/A`. Birthweight percentiles are not published for this dataset, so none are provided.

### Bulk `qc_flags` values

| Flag | Rule |
|---|---|
| `ga_out_of_range` | `ga_delivery_weeks` outside 20 to 42 |
| `ga_days_component_gt6` | Days part of the weeks.days value is above 6 |
| `preterm_group_ga_term` | `iPTB` sample delivered at 37 weeks or later |
| `term_group_ga_preterm` | `TB` sample delivered before 37 weeks |
| `early_onset_pe_delivered_ge34w` | EOPE sample delivered at 34 weeks or later |
| `sbp_out_of_range` / `dbp_out_of_range` | SBP outside 70 to 250 or DBP outside 30 to 150 mmHg |
| `dbp_ge_sbp` | Diastolic at or above systolic |
| `pe_without_bp_ge_140_90` | PE sample whose recorded maximum BP stays below 140/90 |
| `no_pe_with_bp_ge_140_90` | Non-PE sample with maximum SBP at least 140 or DBP at least 90 |
| `bp_missing` / `birthweight_missing` | Value is `NA` |

A flag means "check before relying on this value". It does not mean the value is wrong.

## Gene Annotation (`track01_gene_annotation.csv`)

Maps each row of the bulk count tables to a versioned namespace. Annotation release: **HGNC complete set 2026-10-06** (`hgnc_complete_set_2026-10-06.txt`). Unmapped genes stay in the count table.

| Field | Meaning | Missing |
|---|---|---|
| `gene` | Source symbol, identical to the count table row index | 0 |
| `hgnc_id` | HGNC identifier, for example `HGNC:5` | 1,710 |
| `hgnc_symbol` | Current approved HGNC symbol | 1,710 |
| `ensembl_gene_id` | Ensembl gene ID listed by HGNC | 1,890 (1,710 unmapped plus 180 HGNC genes without an Ensembl ID) |
| `locus_type` | HGNC locus type, for example `gene with protein product` | 1,710 |
| `mapping_status` | `approved_symbol` (23,063), `previous_symbol` (1,614), `alias_symbol` (98), `ambiguous_previous_symbol` (5), `ambiguous_alias_symbol` (1), `unmapped` (1,704) | 0 |
| `shares_hgnc_id_with_other_row` | `yes` if another source symbol maps to the same HGNC ID (140 rows). Decide yourself whether to merge them | 0 |

Mapping rule: exact match to an approved symbol first, then a previous symbol, then an alias. A previous or alias symbol that points to more than one HGNC gene is marked ambiguous and left unmapped. The single-cell extension uses its own gene symbols and is not mapped.

## QC: HTSeq Summary (`qc/track01_htseq_summary.csv`)

One row per bulk sample (villous and decidua). Columns: `assigned_to_genes` (sum of the gene counts), then the HTSeq counters `no_feature`, `ambiguous`, `too_low_aQual`, `not_aligned`, `alignment_not_unique` (read counts). Use it to judge library quality. It is not expression data.

## Extension: Decidua Basalis (`extension/decidua/`)

Optional. The same study also sequenced the maternal decidua basalis from 27 of the 30 placentas (no decidua for S01 to S03).

| File | Contents |
|---|---|
| `track01_counts_db.csv` | 26,485 genes x 27 samples (`S04_DB` to `S30_DB`), raw integer counts, same gene rows as the villous table |
| `track01_metadata_db.csv` | Same fields and rules as the villous metadata. `donor_id` links each decidua sample to its villous sample |

A villous and decidua sample with the same `donor_id` come from the same pregnancy. They are not independent.

## Extension: Single-Cell Pseudobulk (`extension/pseudobulk/`)

Source: Admati, Skarbianskis et al., processed dataset `sc_PE_allcells_with_metadata_29-May-2023.txt` on [Figshare 23264102](https://figshare.com/articles/dataset/Placenta_PE_single_cell_RNAseq_dataset_Admati_Skarbianskis_et_al_/23264102) (CC BY 4.0). 86,752 cells, 31 sequencing libraries, 26 donors.

Counts were summed over all cells from the same donor and cell class. Libraries from the same donor were summed together, so each donor appears once per cell class.

### `track01_pseudobulk_counts.csv`

| Item | Value |
|---|---|
| Shape | 33,660 genes x 362 pseudobulk samples |
| Row index | `gene`: gene symbol from the processed file (10x Genomics feature names) |
| Columns | `pseudobulk_id` in the form `<donor_id>__<cell_class>`, for example `PE_early_1__syncytiotrophoblast` |
| Values | Summed UMI counts. Nonnegative integers |
| Missingness | None. A donor with no cells of a class has no column for it |

A donor-by-class column exists only when that donor has at least one cell of that class. 22 columns are built from fewer than 10 cells. Check `n_cells` before using a column.

### `track01_pseudobulk_metadata.csv`

One row per pseudobulk column. Use it to filter to one `cell_class` before a comparison. It carries every donor field below plus:

| Field | Type | Allowed values | Meaning |
|---|---|---|---|
| `pseudobulk_id` | text | | Index, matches the count columns |
| `cell_class` | category | 14 classes (see `track01_cell_class_map.csv`) | Broad cell class |
| `compartment` | category | `trophoblast`, `stromal`, `vascular`, `immune` | Top-level group |
| `n_cells` | integer | 1 to 1,837 | Cells summed into the column |
| `total_counts` | integer | | Sum of the column (library size) |

### `track01_pseudobulk_donors.csv`

One row per donor (26 rows). Source: the per-cell metadata rows of the processed file. Every field is constant within a donor.

| Field | Type | Unit | Allowed values | Missing | Derivation |
|---|---|---|---|---|---|
| `donor_id` | text | | for example `PE_early_1`, `control_3` | 0 | `donorID`, unchanged |
| `pe_status` | category | | `PE`, `control` | 0 | From `donorID` prefix |
| `onset_group` | category | | `early`, `late` | 0 | `early_PE` or `early_control` = 1 gives `early` |
| `clinical_group` | category | | `PE_early` (10), `PE_late` (7), `control_early` (3), `control_late` (6) | 0 | `pe_status` + `onset_group` |
| `early_onset_comparison` | category | | `exploratory_3_control_vs_10_PE`, `not_applicable` | 0 | Reminder that early-onset comparisons have only 3 control donors |
| `fgr_status` | category | | `FGR`, `no_FGR` | 0 | `IUGR` = 1 |
| `fetal_sex` | category | | `female`, `male` | 0 | `female_fetus` = 1 |
| `delivery_mode` | category | | `c_section`, `vaginal` | 0 | `C-section_birth` / `vaginal_birth` |
| `labor_induction` | category | | `yes`, `no` | 7 | `induction` / `non-induction`. `NA` when neither indicator is set |
| `magnesium_sulfate` | category | | `yes`, `no` | 0 | `magnesium` |
| `anesthesia` | category | | `spinal`, `epidural`, `general`, `none_recorded` | 0 | The anaesthesia indicator set to 1 |
| `ga_delivery_weeks` | decimal | weeks | 24.6 to 40.3 | 0 | `delivery_week`, decimal weeks as published |
| `birthweight_g` | integer | grams | 420 to 4,250 | 0 | `weight` |
| `birthweight_percentile_dolberg` | integer | percentile | 3 to 97 | 0 | `wieght_percentile-Dolberg` (spelling as in the source) |
| `maternal_age_years` | integer | years | 18 to 42 | 0 | `donor_age` |
| `n_libraries` | integer | | 1, 2 | 0 | Distinct `sample` values. 5 donors have 2 libraries (technical replicates) |
| `library_ids` | text | | `;`-separated | 0 | Source library IDs |
| `n_cells` | integer | cells | 876 to 6,700 | 0 | Cells from this donor |
| `qc_flags` | text | | `none` or flags below | 0 | Organizer audit |

Pseudobulk `qc_flags`: `ga_out_of_range` (outside 20 to 42 weeks), `early_group_delivered_at_term`, `late_group_delivered_before_34w`, `birthweight_out_of_range` (outside 300 to 5,500 g), `fgr_with_birthweight_percentile_ge10`, `no_fgr_with_birthweight_percentile_lt3`.

### `track01_cell_class_map.csv`

How the 46 published cell-type labels were grouped into 14 broad classes. Columns: `source_cell_type` (label as published, typos included), `cell_class`, `n_cells`, `compartment`. The grouping follows the label prefixes and names from the source. Teams who disagree with a grouping can see exactly which labels went into each class.

## Audit Findings

| File | Record | Flag | Detail |
|---|---|---|---|
| bulk VT and DB | S26 | `ga_days_component_gt6` | Published as `38.7`. Seven days is not a valid days part. Read literally it is 39 weeks 0 days |
| bulk VT and DB | S26 to S30 (all `TB`) | `bp_missing;birthweight_missing` | GEO lists `N/A` |
| bulk VT and DB | S04, S15 (`FGR`) | `no_pe_with_bp_ge_140_90` | Normotensive by study definition but maximum BP is 143/79 (S04) and 113/90 (S15) mmHg. May reflect isolated readings or gestational hypertension |
| bulk VT and DB | S12 (`EOPE+FGR`) | `pe_without_bp_ge_140_90` | Recorded maximum is 138/88 mmHg |
| pseudobulk | PE_early_1 | `fgr_with_birthweight_percentile_ge10` | Labelled growth restricted with a Dolberg percentile of 13. FGR can be diagnosed from criteria other than birthweight |

Birthweight against FGR status could not be checked for the bulk data because GEO publishes only 100 g bins and no percentiles.

## Fields Not Released

GEO also lists `maternal ethnicity` and `maternal race` for the bulk samples. The plan requires a clinical reviewer to sign off on race and ethnicity variables, with their limitations documented, before release. Until that happens they are held back. They are self-reported, use only three race categories (`Black`, `White`, `Other`) and cover 30 people, so any group comparison would rest on very small numbers.
