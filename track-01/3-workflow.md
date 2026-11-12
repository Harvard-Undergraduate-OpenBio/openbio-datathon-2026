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

**Decide** your question, written 1-2 sentences in your analysis plan.

## 2. Load and Check the Data

The notebook loads the counts and metadata, then checks that every sample appears in both tables and that the counts are clean whole numbers with no duplicates.

If a check fails, note it in your plan and tell an organizer. Do not edit the data files.

## 3. Explore the Samples

Before testing anything, look at how the samples relate to each other. 
This tells you what the biggest sources of difference in the data are, and whether preeclampsia is one of them. 

### What a PCA plot is

Each sample has a value for tens of thousands of genes, too many to plot. **PCA (principal component analysis)** finds the directions in which samples differ the most and summarizes each sample as a few numbers along those directions.

- **PC1** (the x-axis) is the single direction with the most variation between samples. **PC2** (the y-axis) is the next most, independent of PC1.
- The percentage in each axis label is how much of the total variation that axis captures. A PC1 of 35% means that one direction accounts for about a third of all the differences between samples.
- **Points close together have similar overall gene activity. Points far apart are different.** The axes have no units and no built-in biological meaning. You give them meaning by coloring the points.

### How to use it

Set `COLOR_BY` to one metadata column at a time and rerun the cell. Work through at least these:

| Color by | Question |
|---|---|
| Group or PE status | Do preeclampsia samples sit apart from controls? |
| Gestational age | Is there a gradient from early to late deliveries across the plot? |
| Control type | Do preterm and term controls sit in different places? |
| FGR status | Do growth-restricted pregnancies stand out? |
| Fetal sex | Does one axis split samples by sex? |
| Maternal age and other clinical fields | Does anything else line up with the main axes? |

### How to read what you see

| What you see | What it suggests | What to do next |
|---|---|---|
| PE and control samples very separate along PC1 | Preeclampsia is linked to the largest pattern in the data | Check whether gestational age separates the same way before crediting preeclampsia |
| A smooth color gradient along PC1 when colored by gestational age | Delivery timing is a major driver of gene activity | Plan to account for gestational age in Step 4 |
| PE status and gestational age both line up with the same axis | The two are tangled together (confounded) | You cannot tell them apart from this plot. Consider preterm controls only, or a gestational-age covariate. |
| Samples split by fetal sex on PC2 | Sex differences are real but usually not your question | Consider fetal sex as a covariate |
| No visible separation by PE status | The disease effect is smaller than other sources of variation | This is common and does not mean there is no effect. Differential expression tests each gene and can still find differences. |
| Two clear clusters that match no metadata column | A hidden factor, such as a processing batch or a biological subtype | Note it. Within the PE group, this could be the basis of a heterogeneity question. |
| One sample far from all the others | A possible outlier | See below |

### Possible outliers

An odd-looking sample is not automatically a bad one. Before deciding anything:

1. Check its metadata. Is it unusual clinically, such as the earliest delivery or the only one of its kind?
2. Check its total read count. Very low totals make a sample noisy.
3. Run your later analysis both with and without it, and report whether your conclusions change.

Never remove a sample because removing it gives a cleaner result.

**You decide:** which fields seem to drive the biggest differences. Write down what you see. This guides Step 4.

## 4. Choose a Comparison

A comparison splits your samples into two groups and asks which genes differ between them. You build the groups from the metadata table.

### How samples get sorted into groups

The metadata table has one row per sample and one column per piece of clinical information:

| sample_id | pe_status | fgr | gestational_age_weeks |
|---|---|---|---|
| S01 | yes | no | 30.5 |
| S02 | yes | yes | 29.0 |
| S03 | no | no | 31.2 |
| S04 | no | no | 39.1 |
| S05 | yes | no | 32.0 |

Suppose you want to compare pregnancies with preeclampsia against pregnancies without it. You tell the notebook three things:

| Setting | What you type | What it means |
|---|---|---|
| `GROUP_COLUMN` | `"pe_status"` | Sort samples using the `pe_status` column |
| `CASE` | `"yes"` | Rows where `pe_status` is `yes` form the first group, the one you are studying |
| `CONTROL` | `"no"` | Rows where `pe_status` is `no` form the comparison group |

The notebook then reads down the `pe_status` column and sorts every row:

| sample_id | pe_status | Goes into |
|---|---|---|
| S01 | yes | CASE group |
| S02 | yes | CASE group |
| S03 | no | CONTROL group |
| S04 | no | CONTROL group |
| S05 | yes | CASE group |

Rows with any other value, or with `NA`, are left out.

### How this connects to the counts

In the counts table, each sample is a column, and the column names match the `sample_id` values above:

| gene | S01 | S02 | S03 | S04 | S05 |
|---|---|---|---|---|---|
| GENE_A | 310 | 290 | 95 | 110 | 330 |

Once the samples are sorted, the counts columns are sorted the same way. S01, S02 and S05 form the CASE group; S03 and S04 form the CONTROL group. For every gene (every row), DESeq2 compares the CASE columns with the CONTROL columns. Here GENE_A is around 300 in the CASE columns and around 100 in the CONTROL columns, so it is about 3 times higher in the CASE group.

### Adjusting for other columns

`COVARIATES` lists other metadata columns to account for, such as `gestational_age_weeks`. Covariates don't change which group a sample goes into. They let the test ask whether CASE and CONTROL differ *at the same gestational age*, so a difference caused by delivery timing isn't mistaken for a difference caused by preeclampsia. Every sample in both groups needs a value in each covariate column; rows with `NA` there are dropped.

## 5. Run the Test

The notebook runs **differential expression** with DESeq2 (PyDESeq2 in Python). For every gene, it first adjusts for sequencing depth so samples are comparable. It then tests whether the difference between your groups is bigger than the natural variation between samples within a group.

It runs in a few seconds to a few minutes. You do not need to understand the math to use it well.

Note: If it errors, the most common cause is a typo in a column name or value from Step 4.

## 6. Read the Results

You get a table with one row per gene. The columns that matter most:

### The columns

| Column | Meaning | How to read it |
|---|---|---|
| `baseMean` | Average depth-adjusted count across all samples | Under about 10 means very little data. Treat those results cautiously. |
| `log2FoldChange` | Size and direction of the difference, CASE vs. CONTROL | How many times higher or lower the gene is in CASE than in CONTROL, on a log2 scale |
| `lfcSE` | Uncertainty in the fold change | Large relative to the fold change means the estimate is shaky |
| `pvalue` | Evidence for this gene alone | Do not use this to pick genes. It is not corrected for testing thousands of genes. |
| `padj` | Adjusted p-value | Use this. Smaller means stronger evidence. |

### Reading fold change

A **fold change** is how many times bigger one group’s average is than the other’s. Here it compares the average read count of a gene’s expressed mRNA (i.e. its activity) in the CASE samples with its average in the CONTROL samples.

> fold change = average in CASE ÷ average in CONTROL

Say you set `CASE = "yes"` and `CONTROL = "no"` for the `pe_status` column, so your CASE group is the preeclampsia samples and your CONTROL group is the samples without preeclampsia. If a gene averages 300 reads across the CASE group and 100 reads across the CONTROL group, the fold change is 300 ÷ 100 = 3: the gene is 3 times as active in the preeclampsia samples. If the CASE group averaged 50 reads instead, the fold change would be 50 ÷ 100 = 0.5: the gene is half as active in the preeclampsia samples.

DESeq2 reports this ratio on a **log2 scale**, which counts how many times you would double (or halve) to get from CONTROL to CASE. To turn it back into a plain fold change, calculate 2 to the power of the value.


**Example row (invented):** `GENE_A, baseMean 2400, log2FoldChange 1.6, padj 0.0003`. GENE_A is well measured, about 3 times higher in your selected cases, and the evidence is strong.

### Choosing cutoffs

You decide which genes count as "differentially expressed" by setting `PADJ_CUTOFF` and `LFC_CUTOFF`. There is no single right choice:

- A stricter `padj` cutoff means fewer false hits but more missed real ones.
- A fold-change cutoff keeps only bigger effects, which are often easier to interpret biologically.

**Volcano plot** (made by the notebook). Each dot is a gene, and left to right axis is fold change (average cases / average control). Higher up means stronger evidence. Genes in the upper-left and upper-right corners differ the most with the strongest evidence. A lopsided volcano, with almost all hits on one side, is worth mentioning.

**You decide** your cutoffs for `padj` and fold change. The notebook leaves them blank on purpose. Common choices exist (for example padj below 0.05), but state your choice and why. Also check: how many genes pass, and does that change a lot if you loosen or tighten the cutoffs?

## 7. Connect Genes to Cell Types

Bulk data cannot tell you which cells a change comes from. If a gene is higher in preeclampsia samples, either:
- **Different mix:** the tissue contains more of the cell type that uses that gene, or
- **Different behavior:** there are just as many of those cells, but each one is making more of that gene’s RNA.

To start telling these apart:
### 7a. Check the marker table

[`track01_marker_matrix.csv`](data/interpretation/track01_marker_matrix.csv) lists a few marker genes for each broad placental cell class. A marker is a gene used mostly by one cell type, so its level roughly tracks how much of that cell type is in the sample.

The notebook shows which of your passing genes are markers. Then look at **all** the markers for each class, not just the ones that passed:

| What you see for a cell class | Suggests |
|---|---|
| Most of its markers move up (or down) together in cases | A change in how much of that cell type is present |
| Its markers are unchanged, but a gene used mainly by that cell type changed | A change in behavior within that cell type |
| Its markers move in different directions | No clear signal. The markers may not be specific in this tissue. |

**Caveats:** each class has only a few markers. Some classes, such as decidual cells, are mostly absent from villous tissue. The table supports reasoning; it does not prove anything.

### 7b. Look up genes in the gene browser (required)

Look up at least three of your genes in the [Zeisel/Admati browser](https://storage.googleapis.com/www_zeisellab/PE_web/pe_web_test_v1.html). See the [browser guide](data/interpretation/zeisel_browser_guide.md).

**Which genes to choose.** Do not just take the top three by `padj`. Pick genes that:

- have a decent `baseMean`, so the result is reliable
- survived your robustness checks
- represent your story, such as some higher and some lower in cases, or several from one pathway

**What to record for each gene** (the notebook saves this to `results/browser_lookups.csv`):

| Field | Example (invented) |
|---|---|
| Gene | GENE_A |
| Cell types with highest expression | Mostly one trophoblast type, low elsewhere |
| How specific | Specific to one type / a few types / broad |
| PE vs. control difference shown in the browser | Higher in PE within that cell type |
| Notes | Consistent with our bulk result; that cell type's markers did not change in 7a |

**How to combine 7a and 7b:**

| Browser shows | Marker table shows | Reasonable reading |
|---|---|---|
| Changed gene used mainly by cell type X | Cell type X markers unchanged | Behavior change in X is the more likely explanation |
| Changed gene used mainly by cell type X | Cell type X markers also changed in the same direction | Cell-mix/proportion change is a strong alternative |
| Gene used by many cell types | Anything | Cannot localize this gene. |
| Gene higher in PE within cell type X in the browser | Anything | Independent support from a different dataset |

**Caveats:** the browser comes from a different study with different patients and methods. Use it as supporting context, not as validation, and do not present screenshots as quantitative evidence.

Optional: run `python data/get_gene_sets.py` to download Hallmark gene sets and test whether your genes cluster in known biological processes.

**You decide** which genes to look up and what story they suggest. Keep observations ("gene X is higher in cases") separate from interpretations ("which may mean...").

---

## Optional: Single-Cell Extension (advanced)

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
