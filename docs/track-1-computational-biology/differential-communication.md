# Differential Communication Analysis

## Goal

Identify ligand–receptor interactions that differ between preeclampsia and control conditions.

## Workflow

### 1. Run Communication Inference

- Apply one or more tools (CellChat, CellPhoneDB, LIANA, NicheNet) to PE and control data.
- Use the same cell-type annotations for both conditions.
- Use the same ligand–receptor database for consistency.

### 2. Compare Interaction Scores

- For each ligand–receptor pair and sender–receiver combination, compare scores between PE and control.
- Methods for comparison:
  - Direct subtraction of scores (PE − control)
  - Ratio (PE / control)
  - Statistical testing (e.g., permutation-based p-values)
  - Pseudobulk aggregation followed by differential testing

### 3. Identify Differential Edges

- Rank edges by magnitude of change (absolute difference or ratio).
- Apply multiple-testing correction.
- Flag edges that are present in one condition but absent in the other.

### 4. Pathway-Level Aggregation

- Group differential ligand–receptor pairs into signaling pathways.
- Identify pathways with consistent directional change (up or down in PE).

## Visualization

- **Differential chord diagram:** Show gained and lost interactions between cell types.
- **Rank plot:** Rank differential interactions by score change.
- **Network graph:** Highlight edges with the largest disease-associated change.
- **Heatmap:** Sender–receiver matrix of differential interaction scores.

## Pitfalls

- **Cell composition changes:** If a cell type is more abundant in PE, it may appear to have increased communication simply due to more cells. Control for cell-type proportions.
- **Pseudoreplication:** Do not treat cells as independent replicates. Aggregate at the donor level.
- **Method sensitivity:** Different tools and databases will produce different results. Report which methods were used and whether results are robust.
