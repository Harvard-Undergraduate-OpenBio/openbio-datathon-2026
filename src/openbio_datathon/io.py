"""I/O utilities for loading and saving challenge data."""

import scanpy as sc
import pandas as pd
from pathlib import Path


def load_h5ad(path: str | Path) -> sc.AnnData:
    """Load an .h5ad file and print basic info."""
    adata = sc.read_h5ad(str(path))
    print(f"Loaded {adata.shape[0]} cells x {adata.shape[1]} genes from {path}")
    return adata


def load_manifest(path: str | Path = None) -> pd.DataFrame:
    """Load the data manifest CSV."""
    if path is None:
        path = Path(__file__).parent.parent.parent / "data" / "manifest.csv"
    return pd.read_csv(str(path))


def load_cell_metadata(path: str | Path) -> pd.DataFrame:
    """Load a cell-level metadata table."""
    return pd.read_csv(str(path))


def load_donor_metadata(path: str | Path) -> pd.DataFrame:
    """Load a donor-level metadata table."""
    return pd.read_csv(str(path))
