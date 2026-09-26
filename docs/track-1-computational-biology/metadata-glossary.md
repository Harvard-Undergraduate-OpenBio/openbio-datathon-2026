# Metadata Glossary

## Single-Cell Concepts

- **Donor** - A biological individual contributing one or more samples.
- **Sample** - A biological specimen (e.g., placental biopsy, blood draw) from a donor.
- **Library** - A sequencing library prepared from a sample; one sample may yield multiple libraries.
- **Cell barcode** - A short DNA tag used to identify individual cells in droplet-based scRNA-seq.
- **Feature** - A gene (or transcript) measured in the expression matrix.
- **Count matrix** - A matrix of integer counts where rows are features (genes) and columns are cells.

## Quality Control

- **UMI (Unique Molecular Identifier)** - A random tag added to each transcript before amplification, used to deduplicate PCR copies and reduce amplification bias.
- **Mitochondrial fraction** - Percentage of reads mapping to mitochondrial genes; high values indicate stressed or dying cells.
- **Doublet** - A technical artifact where two cells are captured in the same droplet; should be removed during QC.
- **Ambient RNA** - mRNA molecules released from lysed cells that contaminate droplets; should be corrected (e.g., SoupX, CellBender).
- **Low-quality cell** - A cell with low total UMI counts, high mitochondrial fraction, or few detected genes; typically filtered out.

## Expression

- **Raw counts** - Integer UMI counts without normalization.
- **Normalized expression** - Counts adjusted for library size and sometimes transformed (e.g., log1p) for downstream analysis.

## Analysis

- **Cell type** - A biologically meaningful classification of a cell (e.g., "decidual NK cell").
- **Cluster** - A group of cells with similar expression profiles identified by unsupervised methods (e.g., Leiden, Louvain).
- **Annotation** - The process of assigning biological labels to clusters based on marker genes or reference mapping.
- **Pseudobulk** - Aggregation of single-cell counts per donor and cell type to create pseudo-samples for statistical testing; respects biological replication.
- **Batch** - A group of samples processed together under similar technical conditions; a common source of technical variation.
- **Integration** - Computational methods (e.g., Harmony, scVI, Seurat integration) that align datasets from different batches, platforms, or studies to enable joint analysis.
- **Confounder** - A variable associated with both the exposure and outcome that can create spurious associations if not controlled (e.g., gestational age, batch, donor).

## File Formats

- **AnnData** - Python data structure for single-cell data, stored as `.h5ad` files; used by Scanpy.
- **`.h5ad`** - HDF5-based file format for AnnData objects.
- **Cell Ranger matrix** - Output of 10x Genomics Cell Ranger; consists of `matrix.mtx`, `barcodes.tsv`, and `features.tsv` files.
- **Matrix Market / `.mtx`** - Sparse matrix format used for storing count matrices efficiently.
- **Seurat object** - R data structure for single-cell data; stored as `.rds` files.
