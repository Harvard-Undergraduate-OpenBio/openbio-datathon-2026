# Glossary

[![Back](https://img.shields.io/badge/Back-Track_Overview-13deba?style=flat-square)](README.md)

Plain-language definitions, grouped by topic.

## Data Terms

- **Gene** - A stretch of DNA with instructions for making a molecule the cell uses. Every cell has the same genes but uses different ones.
- **Gene activity (expression)** - How strongly a gene is switched on. Measured by counting the RNA copies a cell makes from it.
- **RNA sequencing (RNA-seq)** - A lab method that reads the RNA in a sample and counts how many copies came from each gene.
- **Bulk RNA-seq** - RNA-seq on a whole tissue piece at once. Each count is a total across every cell in the sample.
- **Single-cell RNA-seq** - RNA-seq on individual cells, so each cell gets its own counts and can be labeled by type.
- **Pseudobulk** - Single-cell counts added up per donor and cell type, giving one bulk-like column for each.
- **Count matrix** - The main table: genes as rows, samples as columns, read counts in each cell.
- **Metadata** - Information about each sample, such as clinical group or gestational age.
- **Sequencing depth (library size)** - Total reads in a sample. Deeper samples have higher counts for every gene, so counts must be scaled before comparing.
- **Donor** - The person a sample came from. Each donor counts once in any statistical test.
- **Marker gene** - A gene used mostly by one cell type, so it can signal that cell type's presence.

## Statistics Terms

- **PCA (principal component analysis)** - A way to summarize thousands of gene values per sample into a few numbers so samples can be plotted. Nearby points have similar overall gene activity.
- **Comparison (contrast)** - The two groups you test against each other, such as group A versus group B.
- **Covariate** - An extra variable included in the test so its effect is not mistaken for the effect you care about.
- **Confounder** - A variable linked to both your groups and gene activity, which can create a false difference. Gestational age is a common one here.
- **Differential expression** - A test of whether each gene's activity differs between two groups.
- **DESeq2 / PyDESeq2** - A widely used differential expression method (R and Python versions).
- **Fold change** - How many times higher a gene is in one group than the other.
- **log2 fold change** - Fold change on a log2 scale: +1 is twice as high, −1 is half, 0 is no change.
- **p-value** - How surprising a result would be if there were no real difference. Smaller means more surprising.
- **Adjusted p-value (padj)** - A p-value corrected for testing thousands of genes at once, which would otherwise produce many false hits.
- **Volcano plot** - A plot of fold change against evidence strength for every gene.
- **Outlier** - A sample that looks very different from the rest. Investigate it before deciding anything.
- **Gene set** - A list of genes known to work together in a biological process.


## Anatomy

- **Placenta** - Organ that develops during pregnancy, facilitating exchange of nutrients, gases and waste between mother and fetus.
- **Decidua** - The modified endometrial lining of the uterus during pregnancy; the maternal side of the maternal-fetal interface.
- **Maternal-fetal interface** - The specialized region where maternal decidual tissue and fetal placental tissue interact.
- **Chorionic villus** - Finger-like projections of the placenta containing fetal blood vessels, surrounded by trophoblast.
- **Placental bed** - The region of the uterine wall where the placenta attaches, containing maternal spiral arteries and decidual tissue.

## Fetal Cell Types

- **Trophoblast** - The outer layer of the blastocyst that gives rise to the placental epithelium.
- **Villous cytotrophoblast (vCTB)** - Proliferative trophoblast cells that line the chorionic villi and can fuse into syncytiotrophoblast.
- **Syncytiotrophoblast (STB)** - Multinucleated, non-proliferative outer layer of the villus responsible for hormone production and nutrient/gas exchange.
- **Extravillous trophoblast (EVT)** - Trophoblast cells that invade the maternal decidua and remodel maternal spiral arteries; includes interstitial and endovascular EVT subtypes.

## Maternal Cell Types

- **Decidual stromal cells (DSC)** - Fibroblast-like cells of the decidualized endometrium that support pregnancy and modulate immune responses.
- **Decidual NK cells (dNK)** - Specialized natural killer cells abundant in the decidua; involved in vascular remodeling and immune tolerance.
- **Macrophages** - Immune cells (including Hofbauer cells in the villous stroma and decidual macrophages) involved in phagocytosis, remodeling and immune regulation.
- **T cells** - Adaptive immune cells including CD8+ cytotoxic T cells, CD4+ helper T cells and regulatory T cells (Tregs) important for immune tolerance.
- **Endothelial cells** - Cells lining blood vessels; spiral artery endothelial cells are targets of EVT remodeling.
- **Perivascular cells** - Cells surrounding blood vessels, including pericytes and vascular smooth muscle cells.

## Biological Processes

- **Spiral-artery remodeling** - Process by which EVT cells invade and replace maternal spiral artery endothelium and smooth muscle, converting high-resistance vessels into low-resistance, high-capacity vessels. Failure contributes to preeclampsia.
- **Trophoblast invasion** - Migration of EVT cells into the maternal decidua and spiral arteries; essential for proper placentation.
- **Maternal immune tolerance** - Active suppression of maternal immune responses against the semi-allogeneic fetus; involves Tregs, dNK cells and immunomodulatory signaling.
- **Angiogenesis** - Formation of new blood vessels; critical for placental vascular development.
- **Hypoxia / stress response** - Cellular responses to low oxygen or other stressors; relevant to placental pathology in preeclampsia.

## Disease Context

- **Preeclampsia (PE)** - Pregnancy complication characterized by new-onset hypertension after 20 weeks gestation, often with proteinuria and/or other end-organ dysfunction. Thought to originate from abnormal placentation.
- **Early-onset PE** - Preeclampsia diagnosed before 34 weeks gestation; often associated with more severe placental dysfunction.
- **Late-onset PE** - Preeclampsia diagnosed at or after 34 weeks gestation; may have different etiology and severity profile.
- **Gestational-age-matched control** - A control sample matched to a PE case by gestational age at delivery, reducing confounding by developmental stage.
