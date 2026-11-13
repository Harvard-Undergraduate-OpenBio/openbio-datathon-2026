# Track 01 Data Preparation Plan

[![Download Guide](https://img.shields.io/badge/Data-Data_Package-0fe995?style=flat-square)](../data/README.md)

How the organizers build the Track 01 package. Participants do not need to repeat any of this.

Our job is preparation, not analysis. Participants should start with usable data without being handed the answers.

## Release Contents

Paths are relative to `track-01/data`.

| File | Contents |
|---|---|
| `track01_counts_vt.csv` | Genes x 30 villous-tissue samples, integer raw counts |
| `track01_metadata_vt.csv` | One row per sample: group, PE status, FGR, control type, gestational age, maternal age, fetal sex, clinical fields |
| `track01_data_dictionary.md` | Every field with unit, allowed values, missingness, provenance |
| `interpretation/track01_marker_matrix.csv` | Broad cell-class markers from public references |
| `interpretation/zeisel_browser_guide.md` | How to use the browser and its fallback |
| `extension/pseudobulk/` | Donor-by-cell-type counts and donor metadata |

Include SHA-256 checksums, a source manifest with licenses and a transformation log for everything released.

## Bulk Core (GSE203507)

1. Download the 30 villous-tissue raw count files and sample metadata from [GEO](https://www.ncbi.nlm.nih.gov/geo/query/acc.cgi?acc=GSE203507), plus the 27 decidua-basalis files for the extension.
2. Record a checksum for every downloaded file.
3. Assemble the villous samples into one genes-by-samples matrix of nonnegative integers. Resolve duplicate gene identifiers with a documented rule.
4. Parse the GEO metadata into one row per sample. Use explicit `NA` for missing values and never impute. Standardize units (weeks, mmHg, grams or percentiles).
5. Map gene identifiers to a versioned namespace and record the annotation release. Flag unmapped genes rather than dropping them.
6. Audit for implausible values (gestational age, blood pressure, birthweight vs FGR status). Flag them in the dictionary; do not correct silently.
7. Verify starter notebooks run on the final files and that no released file contains a differential-expression table, pathway result or recommended interpretation.

## Admati Single-Cell Extension

1. Download the [processed expression dataset](https://figshare.com/articles/dataset/Placenta_PE_single_cell_RNAseq_dataset_Admati_Skarbianskis_et_al_/23264102) from Figshare, not the [raw Cell Ranger archive](https://figshare.com/articles/dataset/Placenta_PE_single_cell_RNAseq_cellranger_files_raw_data_Admati_Skarbianskis_et_al_/23628471). The raw archive is organizer-side only; participants never touch it.
2. The processed file contains 86,752 cells from 26 biological donors with cell-type labels, donor IDs, clinical group and delivery information. Some donors have multiple libraries; these are technical replicates, not independent patients.
3. Aggregate counts by donor and cell class. The donor is the unit of replication.
4. Release the donor-by-cell-type pseudobulk counts and donor metadata as the extension. Label the early-onset comparison exploratory, since it has three control donors against ten PE donors.

## Reference Datasets (linked only)

| Dataset | Description | Use |
|---|---|---|
| [GSE198373](https://www.ncbi.nlm.nih.gov/geo/query/acc.cgi?acc=GSE198373) | Healthy second-trimester placental atlas; four donors with villi/basal plate and smooth chorion sampling; about 50,000 cells after QC | Build marker lists for the cell classes in the marker matrix. Do not distribute as competition data. |
| [HCA fetal-maternal interface](https://explore.data.humancellatlas.org/projects/f83165c5-e2ea-4d15-a5cf-33f3550bffde) | About 70,000 first-trimester cells from 16 donors covering placenta, decidua and maternal blood; CC BY 4.0 | Healthy early-pregnancy context for pathway plausibility checks |
| [HCA spatial multiomics trophoblast atlas](https://explore.data.humancellatlas.org/projects/aecfd908-674c-4d4e-b36e-0c1ceab02245) | About 325,700 cells from 34 donors across multiple assays and developmental stages | Too complex to distribute. If used at all, extract one small curated artifact such as a trophoblast marker table and document it in the transformation log. |

## Rules

- Do not hand participants solved contrasts, top gene lists, pathway interpretations, chosen outliers or a prewritten biological story.
- Broad cell-class annotations are fine to supply; participants decide how much confidence to place in them.
- Starter code scaffolds mechanics only, never contrast choice, thresholds or results.
- If race or ethnicity variables are included, document their limitations and have the clinical reviewer sign off before release.

## Timeline

| Phase | When | Work |
|---|---|---|
| Source freeze | T-6 weeks | Download, checksum, verify licenses |
| Package build | T-4 weeks | Counts, metadata, dictionary, gene mapping |
| Starter notebooks | T-3 weeks | R and Python scaffolds, tested on clean environments |
| Pilot | T-2 weeks | Novice team dry run, fix issues |
| Final freeze | T-1 week | Leakage review, QC checklist, versioned ZIP |

After the data freeze, any change requires a version bump and updated checksums.
