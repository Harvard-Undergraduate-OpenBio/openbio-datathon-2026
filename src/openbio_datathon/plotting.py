"""Plotting utilities for datathon visualizations."""

import matplotlib.pyplot as plt
import numpy as np
import pandas as pd


def plot_celltype_composition(adata, groupby: str = "disease_status", celltype_col: str = "cell_type_harmonized"):
    """Plot stacked bar chart of cell-type proportions by condition."""
    props = adata.obs.groupby([groupby, celltype_col]).size().unstack(fill_value=0)
    props_pct = props.div(props.sum(axis=1), axis=0) * 100

    fig, ax = plt.subplots(figsize=(10, 6))
    props_pct.plot(kind="bar", stacked=True, ax=ax, colormap="tab20")
    ax.set_ylabel("Proportion (%)")
    ax.set_title(f"Cell-Type Composition by {groupby}")
    ax.legend(bbox_to_anchor=(1.05, 1), loc="upper left")
    plt.tight_layout()
    return fig, ax


def plot_diff_communication_heatmap(
    diff_matrix: pd.DataFrame,
    title: str = "Differential Communication: PE vs Control",
    save_path: str = None,
):
    """Plot a heatmap of differential communication scores.

    Parameters
    ----------
    diff_matrix : DataFrame with senders as rows and receivers as columns
    """
    fig, ax = plt.subplots(figsize=(8, 6))
    im = ax.imshow(diff_matrix.values, cmap="RdBu_r", aspect="auto")
    ax.set_xticks(range(len(diff_matrix.columns)))
    ax.set_xticklabels(diff_matrix.columns, rotation=45, ha="right")
    ax.set_yticks(range(len(diff_matrix.index)))
    ax.set_yticklabels(diff_matrix.index)
    ax.set_title(title)
    fig.colorbar(im, ax=ax, label="Score Change")
    plt.tight_layout()
    if save_path:
        fig.savefig(save_path, dpi=300, bbox_inches="tight")
    return fig, ax
