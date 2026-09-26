# Preprocessing and Quality Control

## Overview

This document provides a decision framework for preprocessing single-cell RNA-seq data. It does not prescribe a single pipeline but highlights the key steps and considerations.

## Steps

### 1. Loading Data

- Load `.h5ad` (AnnData) or Cell Ranger matrix files (`matrix.mtx`, `barcodes.tsv`, `features.tsv`).
- Verify matrix dimensions: features (genes) x cells.
- Inspect available metadata (cell-level and donor-level).

### 2. Quality Control

For each cell, compute:
- Total UMI counts per cell
- Number of detected genes per cell
- Mitochondrial gene fraction (% mitochondrial reads)

**Filtering thresholds** (adjust based on data):
- Remove cells with very low total UMI counts (e.g., < 500–1000)
- Remove cells with very few detected genes (e.g., < 200–500)
- Remove cells with high mitochondrial fraction (e.g., > 15–20%)

For each gene:
- Remove genes detected in very few cells (e.g., < 3 cells)

### 3. Doublet Removal

- Use tools such as Scrublet (Python) or DoubletFinder (R) to identify and remove doublets.
- Expected doublet rate depends on the number of cells loaded.

### 4. Ambient RNA Correction

- Use tools such as SoupX or CellBender to remove contamination from lysed cells.
- This step is important when ambient RNA contamination is high.

### 5. Normalization

- Common approaches: library-size normalization followed by log1p transformation (Scanpy default).
- SCTransform (Seurat) is an alternative variance-stabilizing transformation.

### 6. Feature Selection

- Identify highly variable genes (HVGs) for downstream dimensionality reduction.
- Typical range: 2,000–4,000 HVGs.
- Exclude mitochondrial and ribosomal genes from HVG selection if they dominate.

### 7. Dimensionality Reduction

- PCA on HVGs, typically 30–50 components.
- Inspect variance explained.

### 8. Clustering and Annotation

- Build a neighbor graph using PCA embeddings.
- Cluster using Leiden or Louvain algorithms.
- Annotate clusters using marker genes, reference mapping (e.g., scArches, CellTypist), or manual inspection.

## State Exactly What You Did

Document all transformations applied to the data:
- QC thresholds used (and justify them)
- Normalization method
- Number of HVGs selected
- Whether integration was applied (and which method)
- Whether cell-type annotations are from the source, OpenBio, or your own
- Whether and how doublets and ambient RNA were handled

This transparency is essential for reproducibility and fair judging.
