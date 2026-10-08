# Track 1: Computational Biology - Overview

[![Data Catalog](https://img.shields.io/badge/Docs-Data_Catalog-0fe995?style=flat-square)](data-catalog.md)
[![Data Dictionary](https://img.shields.io/badge/Docs-Data_Dictionary-13deba?style=flat-square)](data-dictionary.md)
[![Cell Glossary](https://img.shields.io/badge/Docs-Cell_Glossary-0fe995?style=flat-square)](cell-type-glossary.md)
[![Metadata Glossary](https://img.shields.io/badge/Docs-Metadata_Glossary-13deba?style=flat-square)](metadata-glossary.md)
[![Methods](https://img.shields.io/badge/Docs-Communication_Methods-0fe995?style=flat-square)](communication-methods.md)
[![QC Guide](https://img.shields.io/badge/Docs-Preprocessing_QC-13deba?style=flat-square)](preprocessing-and-qc.md)
[![Integration](https://img.shields.io/badge/Docs-Batch_Integration-0fe995?style=flat-square)](batch-correction-and-integration.md)
[![Differential Comm](https://img.shields.io/badge/Docs-Diff_Communication-13deba?style=flat-square)](differential-communication.md)
[![Interpretation](https://img.shields.io/badge/Docs-Interpretation-0fe995?style=flat-square)](biological-interpretation.md)
[![Limitations](https://img.shields.io/badge/Docs-Limitations-13deba?style=flat-square)](limitations-and-responsible-use.md)
[![Citations](https://img.shields.io/badge/Docs-Citations-0fe995?style=flat-square)](citations.md)

## Research Question

> Which ligand-receptor communication programs between fetal trophoblast and maternal decidual/immune cells are altered in preeclampsia, and which altered interactions yield the strongest testable hypotheses about failed placentation, immune tolerance, vascular remodeling, or maternal systemic immune activation?

## Biological Focus

Teams should compare communication involving:

### Fetal placental cells
- Villous cytotrophoblast
- Syncytiotrophoblast
- Extravillous trophoblast (EVT)
- Other annotated fetal populations

### Maternal interface cells
- Decidual stromal cells
- Decidual NK cells
- Macrophages / monocytes
- T cells
- Endothelial / perivascular cells
- Other maternal immune or vascular populations

### Disease contrasts
- Preeclampsia vs. appropriate controls
- Gestational age, sample source, sequencing platform, donor composition, and cell-type abundance treated as potential confounders

### Mechanistic themes
- Trophoblast invasion
- Spiral-artery remodeling
- Immune tolerance
- Inflammation
- Angiogenesis
- Hypoxia / stress response
- Extracellular-vesicle-associated signaling (exploratory extension)

## Minimum Viable Analysis

Every team should be capable of completing the challenge with the supplied processed data:

1. Load an OpenBio-provided annotated object (`.h5ad` or Seurat `.rds`).
2. Inspect metadata and cell-type annotations.
3. Select a biologically coherent sender-receiver comparison.
4. Run or reproduce one cell-cell communication strategy.
5. Compare disease and control interaction patterns.
6. Produce 2-4 figures and a prioritised list of candidate interaction programs.
7. State one testable follow-up hypothesis and its limitations.

## Track 01 Data Package

[![Data Package](https://img.shields.io/badge/Data-Track_01_Package-13deba?style=flat-square)](../../data/track-01/README.md)
[![Starter Notebook](https://img.shields.io/badge/Code-Starter_Notebook-0fe995?style=flat-square)](../../notebooks/track-1/track01_starter.ipynb)
[![Starter Rmd](https://img.shields.io/badge/Code-Starter_Rmd-13deba?style=flat-square)](../../notebooks/track-1/track01_starter.Rmd)
[![Browser Guide](https://img.shields.io/badge/Docs-Browser_Guide-0fe995?style=flat-square)](zeisel-browser-guide.md)

The Track 01 data package holds the bulk count matrix, sample metadata, reference genes, and interpretation resources. Files that HDAG prepares are pending release and are currently blank. Start from the starter notebook or starter Rmd and follow the participant journey in the challenge guide.

## Advanced Directions (Optional)

| Direction | Example Question | Possible Output |
|---|---|---|
| Disease-network rewiring | Which sender-receiver edges appear or disappear in PE? | Differential interaction network, ranked altered pairs |
| Stage or severity | Do early- and late-onset disease patterns differ? | Stratified network comparison |
| Method comparison | Do CellChat, CellPhoneDB, LIANA, or NicheNet converge? | Agreement matrix and consensus ranking |
| Spatial anchoring | Are predicted interactions plausible in the spatial atlas? | Spatial proximity / colocalization figure |
| Maternal systemic link | Do placental changes correspond to PBMC immune shifts? | Cross-tissue pathway comparison |
| Extracellular vesicles | Can teams formulate an EV-mediated signaling hypothesis? | Hypothesis diagram |

## Important Scientific Distinction

scRNA-seq ligand-receptor inference predicts **potential communication from expression patterns**. It does not directly measure physical contact, ligand secretion, receptor activation, extracellular vesicles, or causality. Teams should be rewarded for stating this limitation clearly.

## Preventing Invalid Comparisons

- **Pseudoreplication:** Cells from the same donor are not independent biological replicates.
- **Gestational age:** May be a dominant confounder in placenta comparisons.
- **Tissue and compartment mismatch:** Placenta, decidua, placental bed, and peripheral blood are related but not interchangeable.
- **Batch and platform effects:** A disease/control difference can be technical unless study design and preprocessing are assessed.
- **Cell-composition changes:** Increased representation of a cell type can be mistaken for within-cell-type expression or signaling change.
- **Model-dependent predictions:** Different communication tools and databases will yield different network edges.
