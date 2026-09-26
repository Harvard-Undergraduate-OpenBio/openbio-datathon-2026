"""Validation utilities for checking data integrity and metadata completeness."""

import pandas as pd
import numpy as np


EXPECTED_CELL_FIELDS = [
    "cell_id",
    "donor_id",
    "sample_id",
    "dataset_id",
    "condition",
    "disease_status",
    "tissue",
    "cell_type_harmonized",
    "maternal_or_fetal_origin",
]


def check_metadata_completeness(obs: pd.DataFrame, expected_fields: list = None) -> dict:
    """Check which expected metadata fields are present and how complete they are.

    Returns a dict with field names as keys and dicts with 'present' (bool),
    'missing_pct' (float), and 'n_unique' (int) as values.
    """
    if expected_fields is None:
        expected_fields = EXPECTED_CELL_FIELDS

    report = {}
    for field in expected_fields:
        if field in obs.columns:
            missing = obs[field].isna().sum()
            missing_pct = (missing / len(obs)) * 100
            n_unique = obs[field].nunique()
            report[field] = {
                "present": True,
                "missing_pct": round(missing_pct, 2),
                "n_unique": n_unique,
            }
        else:
            report[field] = {"present": False, "missing_pct": 100.0, "n_unique": 0}
    return report


def check_pseudoreplication(adata) -> bool:
    """Warn if cells are being treated as independent replicates.

    Returns True if pseudoreplication risk is detected.
    """
    if "donor_id" in adata.obs.columns:
        n_cells = adata.shape[0]
        n_donors = adata.obs["donor_id"].nunique()
        if n_donors < 5:
            print(f"WARNING: Only {n_donors} donors for {n_cells} cells. "
                  "Consider pseudobulk approaches to avoid pseudoreplication.")
            return True
    return False
