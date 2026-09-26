# Batch Correction and Integration

## Why Integration Matters

When combining datasets from different donors, studies, platforms, or sequencing batches, technical variation can dominate biological signal. Integration methods aim to align datasets so that cells of the same type cluster together regardless of their batch origin.

## Key Considerations

- **Do not over-correct:** Aggressive integration can remove real biological differences between conditions (e.g., disease vs. control).
- **Preserve disease signal:** When integrating PE and control datasets, ensure that the integration does not artificially align disease and control cells of the same type.
- **Evaluate integration quality:** Use metrics such as kBET, iLISI, or ASW to assess whether integration reduced batch effects while preserving biological signal.

## Methods

| Method | Language | Approach | Notes |
|---|---|---|---|
| [Harmony](https://github.com/immunogenomics/harmony) | Python/R | Iterative clustering and soft assignment | Fast, widely used |
| [scVI](https://github.com/scverse/scvi-tools) | Python | Variational autoencoder | Deep learning; handles complex batch structures |
| [Seurat integration](https://satijalab.org/seurat/articles/integration_introduction.html) | R | Anchor-based canonical correlation analysis (CCA) | Well-established; can be computationally intensive |
| [BBKNN](https://github.com/Teichlab/bbknn) | Python | Graph-based batch-balanced kNN | Lightweight, fast |

## Recommendations

1. Start with Harmony as a baseline — it is fast and effective for most cases.
2. If batch effects are severe or complex, try scVI.
3. Always inspect UMAP/PCA before and after integration to verify that batch effects are reduced without over-correcting biological signal.
4. Report which method was used and with what parameters.

## Warning for PE vs. Control Comparisons

Integrating PE and control data risks removing the very disease signal you want to detect. Consider:
- Analyzing each condition separately, then comparing results.
- Using integration for cell-type annotation only, then reverting to non-integrated data for differential analysis.
- Using pseudobulk approaches that aggregate per donor and cell type before statistical testing.
