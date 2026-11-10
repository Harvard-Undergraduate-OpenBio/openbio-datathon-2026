# Track 02: Cardiovascular Health in Women

[![1 Setup](https://img.shields.io/badge/1-Setup-0fe995?style=flat-square)](1-setup.md)
[![2 The Data](https://img.shields.io/badge/2-The_Data-13deba?style=flat-square)](2-the-data.md)
[![3 Workflow](https://img.shields.io/badge/3-Workflow-0fe995?style=flat-square)](3-workflow.md)
[![4 Submit](https://img.shields.io/badge/4-Submit-13deba?style=flat-square)](4-submit.md)

## The Challenge in Plain Terms

Cardiovascular disease (CVD), meaning disease of the heart and blood vessels, is a leading cause of death for women worldwide. Yet heart disease in women is often under-recognized and under-studied. Symptoms can look different from the "classic" male pattern and women have been under-represented in heart trials. Risk is also shaped by circumstances such as pregnancy, menopause, income and access to care.

This track gives you three datasets that look at the same problem at different scales, from single patients up to whole countries. The central question:

> What does the data tell us about who is at risk of cardiovascular disease, how that risk differs for women and how individual-level risk factors connect to the global, unequal burden of disease in women?

You do not need to answer all of it. Your team will:

1. Pick a focused angle from the [starter questions](starter-questions.md).
2. Clean the data responsibly and log every decision.
3. Explore the data and build a model you can defend.
4. Explain what you found so someone outside your field could understand it.

Judges reward honest, careful work more than dramatic results.

## What You Get

| Dataset | What it is | Level |
|---|---|---|
| 1. Cardiovascular Disease Dataset | Real-world-style clinical records: blood pressure, cholesterol, glucose and lifestyle, with a CVD label | Individual patients |
| 2. Heart Attack Risk Prediction Dataset | Synthetic (computer-generated) records with diet, stress, sleep, income and country, with a heart-attack-risk label | Individual patients (synthetic) |
| 3. Global CVD in Women (GBD) | Published tables of CVD rates in women by region and country, 1990 and 2019 | Population |

[Understand the data](2-the-data.md) explains each one and what to watch for.

## The Workflow at a Glance

```
 Pick a question  ->  Clean and log  ->  Explore  ->  Model
                                                        |
                                                        v
     Submit  <-  Headline visual  <-  Interpret  <-  Check your work
```

The [analysis workflow](3-workflow.md) walks through each box. The two notebooks in [`team/notebooks/`](team/notebooks) do the coding: [01_cleaning](team/notebooks/01_cleaning.ipynb) and [02_analysis](team/notebooks/02_analysis.ipynb).

## Ground Rules

Every submission must respect these. The [responsible use page](reference/limitations.md) explains each one.

- **Correlation is not causation.** Avoid causal language unless you can justify it.
- **Synthetic is not real.** Do not present findings from Dataset 2 as clinical evidence.
- **Countries are not individuals.** Do not use Dataset 3 to make claims about individual women.
- **Sex is recorded as binary.** Note this limitation and do not overgeneralize.
- **Not medical advice.** Include a short statement saying so in your deliverables.
- **Show uncertainty.** Report confidence intervals or variability where you can.
- **Respect the data licenses** of the original Kaggle pages and the article publisher.

## Everything in This Folder

| Item | What it is |
|---|---|
| [1-setup.md](1-setup.md) | Open Colab, load the data and set up your team repository |
| [2-the-data.md](2-the-data.md) | Plain-language guide to all three datasets |
| [3-workflow.md](3-workflow.md) | Step-by-step analysis walkthrough |
| [4-submit.md](4-submit.md) | The four deliverables and how to hand them in |
| [starter-questions.md](starter-questions.md) | Focused angles to choose from |
| [glossary.md](glossary.md) | Health and statistics terms |
| [data/](data) | The data files |
| [team/](team) | Your team's workspace: notebooks, figures, cleaning log and article |
| [reference/](reference) | Data catalog, citations and responsible use |
