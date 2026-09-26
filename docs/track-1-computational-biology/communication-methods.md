# Communication Inference Methods

## Core Concepts

- **Sender** - A cell type that expresses a ligand.
- **Receiver** - A cell type that expresses the corresponding receptor.
- **Ligand** - A signaling molecule (e.g., growth factor, cytokine, chemokine) secreted by one cell that binds to receptors on another.
- **Receptor** - A cell-surface or intracellular protein that binds a ligand and transduces a signal.
- **Ligand-receptor pair** - A known interacting pair of ligand and receptor proteins (e.g., VEGFA-KDR).
- **Interaction score** - A quantitative measure of the likelihood or strength of communication between a sender and receiver via a specific ligand-receptor pair.
- **Edge** - A connection in the communication network representing an interaction between two cell types.
- **Communication network** - A graph where nodes are cell types and edges are weighted by interaction scores.
- **Differential communication** - Comparison of communication networks between conditions (e.g., PE vs. control) to identify edges that are gained, lost, or changed in magnitude.

## Pathway-Level Analysis

- **Pathway-level aggregation** - Grouping individual ligand-receptor pairs into signaling pathways (e.g., "VEGF pathway", "TGF-β pathway") for higher-level interpretation.
- **Ligand activity** - A measure of how strongly a ligand's expression correlates with downstream target gene expression in receiver cells.

## Databases and Priors

- **Database priors** - Curated sets of known ligand-receptor interactions used as input for communication inference (e.g., OmniPath, CellChatDB, Ramilowski et al. 2015).
- **Database coverage** - The extent to which a given database includes the ligand-receptor pairs relevant to the biological system being studied.

## Statistical Inference

- **Permutation test** - A non-parametric test that shuffles cell-type labels to generate a null distribution for interaction scores.
- **Multiple-testing correction** - Adjustment of p-values (e.g., Bonferroni, Benjamini-Hochberg) to control for false positives when testing many ligand-receptor pairs.

## Key Distinction

- **Predicted interaction** - An interaction inferred from expression data using computational tools; represents potential communication.
- **Validated interaction** - An interaction confirmed by experimental methods (e.g., co-culture, ligand stimulation, spatial proximity, protein-level measurement).

## Tools

| Tool | Language | Key Features |
|---|---|---|
| [CellChat](https://github.com/jinworks/CellChat) | R | Pathway-level inference, rich visualization, comparison across conditions |
| [CellPhoneDB](https://github.com/Teichlab/cellphonedb) | Python | Permutation-based inference, UniProt-based database, multi-condition comparison |
| [LIANA](https://github.com/saezlab/liana) | Python/R | Meta-framework running multiple methods, consensus scoring |
| [NicheNet](https://github.com/saezlab/nichenetr) | R | Ligand activity prediction using prior knowledge and target gene expression |

## Spatial Context

- **Spatial proximity** - Physical distance between sender and receiver cells in tissue; can support or challenge predicted interactions.
- **Colocalization** - Co-occurrence of cell types in the same spatial region; a prerequisite for direct cell-cell communication.
