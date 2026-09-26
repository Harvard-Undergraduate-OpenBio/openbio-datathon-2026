# Track 1: Computational Biology — Overview

## Research Question

> Which ligand–receptor communication programs between fetal trophoblast and maternal decidual/immune cells are altered in preeclampsia, and which altered interactions yield the strongest testable hypotheses about failed placentation, immune tolerance, vascular remodeling, or maternal systemic immune activation?

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
3. Select a biologically coherent sender–receiver comparison.
4. Run or reproduce one cell–cell communication strategy.
5. Compare disease and control interaction patterns.
6. Produce 2–4 figures and a prioritised list of candidate interaction programs.
7. State one testable follow-up hypothesis and its limitations.

## Advanced Directions (Optional)

| Direction | Example Question | Possible Output |
|---|---|---|
| Disease-network rewiring | Which sender–receiver edges appear or disappear in PE? | Differential interaction network, ranked altered pairs |
| Stage or severity | Do early- and late-onset disease patterns differ? | Stratified network comparison |
| Method comparison | Do CellChat, CellPhoneDB, LIANA, or NicheNet converge? | Agreement matrix and consensus ranking |
| Spatial anchoring | Are predicted interactions plausible in the spatial atlas? | Spatial proximity / colocalization figure |
| Maternal systemic link | Do placental changes correspond to PBMC immune shifts? | Cross-tissue pathway comparison |
| Extracellular vesicles | Can teams formulate an EV-mediated signaling hypothesis? | Hypothesis diagram |

## Important Scientific Distinction

scRNA-seq ligand–receptor inference predicts **potential communication from expression patterns**. It does not directly measure physical contact, ligand secretion, receptor activation, extracellular vesicles, or causality. Teams should be rewarded for stating this limitation clearly.

## Preventing Invalid Comparisons

- **Pseudoreplication:** Cells from the same donor are not independent biological replicates.
- **Gestational age:** May be a dominant confounder in placenta comparisons.
- **Tissue and compartment mismatch:** Placenta, decidua, placental bed, and peripheral blood are related but not interchangeable.
- **Batch and platform effects:** A disease/control difference can be technical unless study design and preprocessing are assessed.
- **Cell-composition changes:** Increased representation of a cell type can be mistaken for within-cell-type expression or signaling change.
- **Model-dependent predictions:** Different communication tools and databases will yield different network edges.

## Key Documents

- [Data Catalog](data-catalog.md)
- [Data Dictionary](data-dictionary.md)
- [Cell & Tissue Glossary](cell-type-glossary.md)
- [Metadata Glossary](metadata-glossary.md)
- [Communication Methods](communication-methods.md)
- [Preprocessing and QC](preprocessing-and-qc.md)
- [Batch Correction and Integration](batch-correction-and-integration.md)
- [Differential Communication](differential-communication.md)
- [Biological Interpretation](biological-interpretation.md)
- [Limitations and Responsible Use](limitations-and-responsible-use.md)
- [Citations](citations.md)
