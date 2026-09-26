"""Quality control utilities for single-cell data."""

import scanpy as sc
import numpy as np


def compute_qc_metrics(adata, mt_prefix: str = "MT-") -> sc.AnnData:
    """Compute standard QC metrics including mitochondrial fraction."""
    adata.var["mt"] = adata.var_names.str.startswith(mt_prefix)
    sc.pp.calculate_qc_metrics(adata, qc_vars=["mt"], inplace=True)
    return adata


def filter_cells(
    adata,
    min_counts: int = 500,
    min_genes: int = 200,
    max_mt_pct: float = 20.0,
) -> sc.AnnData:
    """Filter low-quality cells based on standard thresholds."""
    n_before = adata.shape[0]
    adata = adata[adata.obs["total_counts"] >= min_counts, :].copy()
    adata = adata[adata.obs["n_genes_by_counts"] >= min_genes, :].copy()
    if "pct_counts_mt" in adata.obs.columns:
        adata = adata[adata.obs["pct_counts_mt"] <= max_mt_pct, :].copy()
    n_after = adata.shape[0]
    print(f"Filtered: {n_before} -> {n_after} cells")
    return adata


def filter_genes(adata, min_cells: int = 3) -> sc.AnnData:
    """Filter genes detected in very few cells."""
    n_before = adata.shape[1]
    sc.pp.filter_genes(adata, min_cells=min_cells)
    n_after = adata.shape[1]
    print(f"Filtered: {n_before} -> {n_after} genes")
    return adata
