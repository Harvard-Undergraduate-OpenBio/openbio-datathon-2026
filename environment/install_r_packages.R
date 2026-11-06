# Installs the R packages used by track-01/notebooks/track01_workflow.Rmd
install.packages(c("ggplot2", "pheatmap", "rmarkdown", "BiocManager"))
BiocManager::install("DESeq2")
