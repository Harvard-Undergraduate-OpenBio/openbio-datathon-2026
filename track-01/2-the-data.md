# Step 2: Understand the Data

[![Back](https://img.shields.io/badge/Back-1_Setup-13deba?style=flat-square)](1-setup.md)
[![Next](https://img.shields.io/badge/Next-3_Workflow-0fe995?style=flat-square)](3-workflow.md)

> **Status:** Files marked Pending will be filled in at release. Until then they are empty placeholders.

## The Core Dataset in One Minute

The core data come from [GSE203507](https://www.ncbi.nlm.nih.gov/geo/query/acc.cgi?acc=GSE203507), a public study of 30 placentas collected at delivery. Researchers took a piece of villous tissue (the part of the placenta that exchanges nutrients with the mother's blood) from each one.

They then used **bulk RNA sequencing**. When a gene is switched on, the cell copies 
the gene into mRNA sequences, and sequencing allows us to measure the mRNA levels. Bulk sequencing means that a whole tissue piece was measured at once (instead of individual cells), so the data is a total across all cells in that sample. 

The data contains multiple samples from multiple tissues.

You get two tables that link through a shared sample ID.

### Table 1: Counts (`track01_counts_vt.csv`)

|  | sample_01 | sample_02 | ... |
|---|---|---|---|
| **GENE_A** | 1520 | 1874 | ... |
| **GENE_B** | 3 | 0 | ... |
| ... | ... | ... | ... |

- One row per gene (tens of thousands of rows) and one column per sample (30 columns).
- Each number is how many RNA reads came from that gene in that sample. A larger number of reads means that a gene produced more mRNA, meaning it was more active.
- Counts are raw whole numbers. Samples were sequenced to different depths, so do not compare raw numbers between columns directly. The workflow handles this for you.

### Table 2: Metadata (`track01_metadata_vt.csv`)

One row per sample describing the pregnancy:

| Field | Meaning |
|---|---|
| group | Clinical group the study assigned to the sample |
| PE status | Whether the pregnancy had preeclampsia |
| FGR | Whether the fetus had growth restriction (grew less than expected) |
| control type | For controls, which kind (for example preterm or term birth) |
| gestational age | Weeks of pregnancy at delivery |
| maternal age, fetal sex and other clinical fields | Described in the data dictionary |

Exact column names, units and allowed values are in [`data/track01_data_dictionary.md`](data/track01_data_dictionary.md). Read it before you choose a comparison.

Missing values are written `NA` and never filled in. Values that look implausible are flagged in the dictionary, not corrected.

### One Important Caution

Preeclampsia often forces early delivery. So preeclampsia samples may also be earlier in pregnancy than many controls. A gene can differ because of preeclampsia or because of gestational age, and often you cannot tell which without checking. Keep this in mind from the start.

## The Gene Browser (required)

The [Zeisel/Admati gene browser](https://storage.googleapis.com/www_zeisellab/PE_web/pe_web_test_v1.html) is a website. Type a gene name and it shows which placental cell types use that gene. Bulk data cannot tell you which cells a signal comes from, so this is how you connect your results to cell types. Every team looks up at least three genes. See the [browser guide](data/interpretation/zeisel_browser_guide.md).

The [marker table](data/interpretation/track01_marker_matrix.csv) is the offline backup. It lists genes known to mark broad placental cell types.

## The Single-Cell Extension (optional)

For teams that want more detail. The Admati/Skarbianskis study measured 86,752 individual placental cells from 26 donors and labeled each cell's type. We added up the counts for each donor and cell type (called **pseudobulk**), so you get one smaller table with a column per donor and cell type instead of 86,752 columns.

- `extension/pseudobulk/track01_pseudobulk_counts.csv`: counts by donor and cell type
- `extension/pseudobulk/track01_pseudobulk_metadata.csv`: one row per donor with clinical group and delivery information

Each donor counts once, even if they were sequenced more than once. The early-onset comparison in this dataset has only three control donors against ten preeclampsia donors, so treat it as exploratory.

## Reference Atlases (linked only)

Maps of healthy placenta at earlier stages of pregnancy. Use them for context, never as control groups.

| Atlas | What it shows | Link |
|---|---|---|
| GSE198373 | Healthy second-trimester placenta, four donors | [GEO](https://www.ncbi.nlm.nih.gov/geo/query/acc.cgi?acc=GSE198373) |
| HCA fetal-maternal interface | Healthy first-trimester placenta, uterine lining and maternal blood, 16 donors | [Human Cell Atlas](https://explore.data.humancellatlas.org/projects/f83165c5-e2ea-4d15-a5cf-33f3550bffde) |
| HCA spatial multiomics trophoblast atlas | How trophoblast cells develop, 34 donors | [Human Cell Atlas](https://explore.data.humancellatlas.org/projects/aecfd908-674c-4d4e-b36e-0c1ceab02245) |

## Full File List

See [`data/README.md`](data/README.md) for every file, its status and how the package was built.
