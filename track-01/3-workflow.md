# Step 3: Analysis Workflow

[![Back](https://img.shields.io/badge/Back-2_The_Data-13deba?style=flat-square)](2-the-data.md)
[![Next](https://img.shields.io/badge/Next-4_Submit-0fe995?style=flat-square)](4-submit.md)
[![Notebook](https://img.shields.io/badge/Open-Workflow_Notebook-0fe995?style=flat-square)](notebooks/track01_workflow.ipynb)

Seven steps take you from raw counts to a hypothesis. Each one matches a numbered section in the [workflow notebook](notebooks/track01_workflow.ipynb) ([R version](notebooks/track01_workflow.Rmd)). The notebook does the coding mechanics. Your team makes the decisions, marked **You decide** below.

Keep a copy of the [analysis plan template](templates/analysis-plan.md) open and fill it in as you go. It becomes part of your submission.

| Step | Goal | Notebook section |
|---|---|---|
| 1 | Pick a question | 1 |
| 2 | Load and check the data | 2 |
| 3 | Explore the samples | 3 |
| 4 | Choose a comparison | 4 |
| 5 | Run the test | 5 |
| 6 | Read the results | 6 |
| 7 | Connect genes to cell types | 7 |

---

## 1. Pick a Question

Read the [starter questions](starter-questions.md) and pick one. Questions 1, 2, 5 and 6 work with the core data alone and are good first choices.

**You decide:** your question, written as one sentence in your analysis plan.

## 2. Load and Check the Data

The notebook loads the counts and metadata, then checks that every sample appears in both tables and that the counts are clean whole numbers with no duplicates.

**You decide:** nothing yet. If a check fails, note it in your plan and tell an organizer. Do not edit the data files.

## 3. Explore the Samples

Before testing anything, look at how the samples relate to each other. The notebook makes a **PCA plot**: it squeezes each sample's thousands of gene counts into two numbers so that samples with similar gene activity land close together.

Color the plot by different metadata fields, such as group or gestational age, and ask:

- Do samples cluster by preeclampsia status? By gestational age? By something else?
- Does any sample sit far from all the others? That may be an outlier worth discussing, but do not drop it without a stated reason.

**You decide:** which fields seem to drive the biggest differences. Write down what you see. This guides Step 4.

## 4. Choose a Comparison

A **comparison** asks: which genes differ between group A and group B? You define both groups using metadata columns.

Fill in these settings in the notebook:

| Setting | What it means | Example format |
|---|---|---|
| `GROUP_COLUMN` | The metadata column that defines your groups | a column name from the dictionary |
| `CASE` and `CONTROL` | The two values of that column you will compare | two values that column contains |
| `COVARIATES` | Other columns to account for, such as gestational age | a list of column names, or empty |

Things to weigh:

- **Fair comparison.** If cases were delivered much earlier than controls, differences may reflect timing. Adding gestational age as a covariate, or choosing controls of similar age, helps separate the two.
- **Sample size.** Each group needs enough samples. With five or fewer per group, results will be noisy.

**You decide:** your groups, any covariates and why. Write a two-sentence justification in your plan.

## 5. Run the Test

The notebook runs **differential expression** with DESeq2 (PyDESeq2 in Python). For every gene, it first adjusts for sequencing depth so samples are comparable. It then tests whether the difference between your groups is bigger than the natural variation between samples within a group.

It runs in a few seconds to a few minutes. You do not need to understand the math to use it well.

**You decide:** nothing new. If it errors, the most common cause is a typo in a column name or value from Step 4.

## 6. Read the Results

You get a table with one row per gene. The columns that matter most:

| Column | Meaning | How to read it |
|---|---|---|
| `log2FoldChange` | How much higher or lower the gene is in CASE vs CONTROL, on a log2 scale | +1 means twice as high in CASE. −1 means half as high. 0 means no change. |
| `padj` | Adjusted p-value: how likely a difference this large is by chance, corrected for testing thousands of genes | Smaller means stronger evidence. |
| `baseMean` | Average count across all samples | Very low values give unreliable results. |

The notebook draws a **volcano plot** (fold change against evidence strength). Genes far left or right and high up differ the most with the strongest evidence.

**You decide:** your cutoffs for `padj` and fold change. The notebook leaves them blank on purpose. Common choices exist (for example padj below 0.05), but state your choice and why. Also check: how many genes pass, and does that change a lot if you loosen or tighten the cutoffs?

## 7. Connect Genes to Cell Types

Bulk data cannot tell you which cells a change comes from. Two possibilities look the same in bulk:

- **Different mix:** the tissue has more or fewer of some cell type.
- **Different behavior:** the same cells changed their gene activity.

To start telling these apart:

1. **Marker table.** The notebook checks which of your genes appear in [`track01_marker_matrix.csv`](data/interpretation/track01_marker_matrix.csv). If many markers of one cell type move together, a change in cell mix is one explanation.
2. **Gene browser (required).** Look up at least three of your genes in the [Zeisel/Admati browser](https://storage.googleapis.com/www_zeisellab/PE_web/pe_web_test_v1.html) and record which cell types use them. See the [browser guide](data/interpretation/zeisel_browser_guide.md).

Optional: run `python data/get_gene_sets.py` to download Hallmark gene sets and test whether your genes cluster in known biological processes.

**You decide:** which genes to look up and what story they suggest. Keep observations ("gene X is higher in cases") separate from interpretations ("which may mean...").

---

## Optional: Single-Cell Extension

Want to know whether a specific cell type changes? The [pseudobulk files](2-the-data.md#the-single-cell-extension-optional) let you rerun Steps 4 to 6 inside one cell type at a time. Notebook section 8 shows how to load them. Treat each donor as one sample, and treat the early-onset comparison as exploratory.

## Common Pitfalls

| Pitfall | Better approach |
|---|---|
| Choosing groups after seeing which gives the most genes | Choose groups in Step 4 before running Step 5, and report what you tried |
| Treating a correlation as a cause | Say "associated with" or "consistent with" |
| Ignoring gestational age | Show you checked it in Steps 3 and 4 |
| Dropping samples that look odd | Keep them, or explain clearly why you removed them |
| Treating browser images as proof | Use them as supporting context only |

## When You Are Done

You should have a filled-in analysis plan, a results table and at least two figures. Move on to [Step 4: Submit](4-submit.md) to turn them into a hypothesis.
