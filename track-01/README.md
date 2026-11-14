# Track 01: Maternal-Fetal Cell Communication in Preeclampsia

[![1 Setup](https://img.shields.io/badge/1-Setup-0fe995?style=flat-square)](1-setup.md)
[![2 The Data](https://img.shields.io/badge/2-The_Data-13deba?style=flat-square)](2-the-data.md)
[![3 Workflow](https://img.shields.io/badge/3-Workflow-0fe995?style=flat-square)](3-workflow.md)
[![4 Submit](https://img.shields.io/badge/4-Submit-13deba?style=flat-square)](4-submit.md)

## The Challenge

Preeclampsia is a pregnancy complication that causes dangerously high blood pressure in the mother. It is thought to begin with problems in the placenta, the organ that connects mother and fetus.

Every cell carries the same genes, but each cell type switches different genes on or off. Measuring which genes are on, and how strongly, tells us what the tissue is doing. Your team will:

1. Compare gene activity in placentas from pregnancies with preeclampsia and control pregnancies.
2. Find the genes that differ most.
3. Use reference data to ask which placental cell types those genes belong to.
4. Propose a testable explanation (a hypothesis) for what you found.

There is no one correct answer. Careful reasoning and honest limits are more important.

## What You Get

| Resource | Role | Required? |
|---|---|---|
| GSE203507 bulk RNA-seq | Gene activity in 30 placental tissue samples, with clinical details for each pregnancy | Yes |
| Zeisel/Admati gene browser | Website showing which placental cell types use a gene | Yes, for at least three genes |
| Admati/Skarbianskis single-cell data | Gene activity per cell type for 26 donors | Optional extension |
| Reference atlases (GSE198373 and two HCA projects) | Maps of healthy placenta for context | Optional, linked only |

[Understand the data](2-the-data.md) explains each of these in detail.

## The Workflow at a Glance

```
 Pick a question  ->  Load and check  ->  Explore samples  ->  Choose a comparison
        |                                                            |
        v                                                            v
   Hypothesis  <-  Look up cell types  <-  Read the results  <-  Run the test
```

The [analysis workflow](3-workflow.md) walks through each box, and the [workflow notebook](notebooks/track01_workflow.ipynb) has a matching section for each one.

## Ground Rules and Notes

- Choosing comparisons and interpreting results is your team's job. Organizers will not suggest gene lists or answers.
- Each person (donor) counts once. Several samples or cells from one person are not independent evidence.
- Keep missing values missing. Report flagged values instead of fixing them.
- Use the released data package rather than rebuilding it from raw sources.

## Everything in This Folder

| Item | What it is |
|---|---|
| [1-setup.md](1-setup.md) | Install software and download the data |
| [2-the-data.md](2-the-data.md) | Plain-language guide to every file |
| [3-workflow.md](3-workflow.md) | Seven-step analysis walkthrough |
| [4-submit.md](4-submit.md) | What to hand in and how |
| [starter-questions.md](starter-questions.md) | Ten research questions to choose from |
| [glossary.md](glossary.md) | Biology and statistics terms |
| [data/](data) | The data package |
| [notebooks/](notebooks) | Guided workflow in Python and R |
| [templates/](templates) | Templates for your submission folder: README, article, analysis plan and hypothesis card |
| [reference/](reference) | Data catalog, citations, limitations and how the data were prepared |
