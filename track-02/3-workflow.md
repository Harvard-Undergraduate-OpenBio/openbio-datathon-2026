# Step 3: Analysis Workflow

[![Back](https://img.shields.io/badge/Back-2_The_Data-13deba?style=flat-square)](2-the-data.md)
[![Next](https://img.shields.io/badge/Next-4_Submit-0fe995?style=flat-square)](4-submit.md)
[![Cleaning](https://img.shields.io/badge/Open-01_Cleaning-0fe995?style=flat-square)](team/notebooks/01_cleaning.ipynb)
[![Analysis](https://img.shields.io/badge/Open-02_Analysis-13deba?style=flat-square)](team/notebooks/02_analysis.ipynb)

Seven steps take you from raw files to a headline finding. Steps 2 and 3 use [`01_cleaning.ipynb`](team/notebooks/01_cleaning.ipynb). Steps 3 to 7 use [`02_analysis.ipynb`](team/notebooks/02_analysis.ipynb). The notebooks do the coding mechanics. Your team makes the decisions, marked **You decide** below and in the notebooks.

| Step | Goal | Notebook |
|---|---|---|
| 1 | Pick a question | 02, section 1 |
| 2 | Clean the data and log every rule | 01 |
| 3 | Explore | 02, section 2 |
| 4 | Build a model | 02, section 3 |
| 5 | Check your work | 02, section 4 |
| 6 | Interpret | 02, section 5 |
| 7 | Make a headline visual | 02, section 6 |

---

## 1. Pick a Question

Read the [starter questions](starter-questions.md) and pick one. Decide which dataset or datasets you need.

**You decide:** your question as one sentence, written at the top of `02_analysis.ipynb` and in your team README.

## 2. Clean the Data and Log Every Rule

Raw data contain mistakes. Cleaning means deciding which values to fix or remove and writing down each decision. The cleaning notebook records every rule and how many records it affected, then writes the log to [`team/docs/cleaning_log.md`](team/docs/cleaning_log.md) for you.

Only clean the datasets you use. The notebook has one section per dataset.

| Dataset | Main cleaning tasks | You decide |
|---|---|---|
| 1 | Convert age to years, keep women, remove impossible blood pressure and body measurements, calculate BMI | Plausible ranges for blood pressure, height and weight |
| 2 | Split blood pressure into two numbers, encode sex and the ordered diet levels | Women only, or women compared with men |
| 3 | Find the real header rows, reshape wide to long, split confidence intervals, standardize country names | Which rows hold the headers and which columns you need |

How to pick a plausibility range: look at the distribution first (the notebook plots it), then choose a range you can defend in one sentence using what is physically possible. Write that reason in the log.

**Checkpoint:** the cleaning log lists every rule with a count, and the notebook saves cleaned files to `team/data_clean/`.

## 3. Explore

Before modeling, describe your data. The analysis notebook prints sample sizes and summary statistics, then plots each variable against your outcome.

- How many people (or countries) are in your analysis after cleaning?
- What do the main variables look like? Any surprises?
- Which variables seem related to the outcome?
- Are some groups much smaller than others?

**You decide:** which variables look worth modeling. Note anything odd in your README.

## 4. Build a Model

A model puts a number on a relationship and its uncertainty. Your presentation must include a regression graph where it fits your question. The notebook supports two kinds.

| Model | Use when | What you get |
|---|---|---|
| **Logistic regression** | The outcome is yes/no, such as `cardio` or `Heart Attack Risk` | An **odds ratio** with a 95% confidence interval for each risk factor, shown as a forest plot |
| **Linear regression** | The outcome is a number, such as systolic blood pressure or ASIR | A fitted line with a confidence band, plus the slope and R² |

Examples of linear questions: age against systolic blood pressure (Dataset 1), or SDI against ASIR (Dataset 3).

How to read the results:

- **Odds ratio (OR):** 1 means no association. 1.5 means 50% higher odds of the outcome per unit of the predictor. 0.8 means 20% lower odds.
- **95% confidence interval:** the range of values consistent with the data. If it crosses 1 (for OR) or 0 (for a slope), the data cannot rule out no effect.
- **R²:** the share of variation in the outcome explained by the line, from 0 to 1.

**You decide:** the outcome, the predictors and how each is encoded. Keep ordered categories ordered, and think about which variables could confound the one you care about (age is a common one).

## 5. Check Your Work

A model can look good by chance. The notebook helps you test it.

- **Logistic models:** the notebook holds back 20% of the data, fits on the rest and reports the **AUC** on the held-back part. AUC runs from 0.5 (no better than a coin flip) to 1 (perfect).
- **Linear models:** the notebook plots residuals (the gaps between the line and the points). A pattern in the residuals means a straight line is not a good fit.

Also try changing one decision, such as a cleaning range or a predictor, and see whether your main result holds.

**You decide:** whether your model is good enough to support your claim. Say so honestly.

## 6. Interpret

Turn numbers into a plain sentence. Compare:

| Too strong | Better |
|---|---|
| "High cholesterol causes heart disease in women." | "Women with well-above-normal cholesterol had higher odds of CVD (OR X.X, 95% CI X.X to X.X) after accounting for age." |
| "Poorer countries make women sicker." | "Countries with lower SDI tended to have [higher or lower] ASIR. This describes countries, not individual women." |
| "Stress predicts heart attacks." | "In this synthetic dataset, stress was [or was not] associated with risk. This is a methods exercise, not clinical evidence." |

These rows show the format only, not expected results. Check each claim against the [ground rules](README.md#ground-rules).

## 7. Make a Headline Visual

One graph that shows your single most important finding to a non-specialist. You will use it in both the video and the article. The article needs at least four graphs in total ([article guide](../docs/article-guide.md#graphs)), so save other useful graphs as you go. A good headline visual:

- Has a title that states the finding in plain words
- Labels axes in everyday language, with units
- Shows uncertainty, such as error bars or a confidence band
- Is readable at normal video resolution

The notebook saves it to `team/figures/headline.png`.

---

## Common Pitfalls

| Pitfall | Better approach |
|---|---|
| Forgetting age is in days | Convert in the first cleaning step |
| Dropping odd rows without saying so | Log every rule with its count |
| Treating cholesterol 1, 2, 3 as measurements | Keep them as ordered categories |
| Presenting Dataset 2 results as real | Label them a methods exercise |
| Claiming country patterns apply to individuals | Keep Dataset 3 claims at the country or region level |
| Reporting a result without uncertainty | Add confidence intervals or variability |

## When You Are Done

You should have a cleaning log, cleaned data, a model with a regression graph and a headline visual. Move on to [Step 4: Submit](4-submit.md).
