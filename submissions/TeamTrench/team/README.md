# Team Trench

OpenBio 2026 Datathon, Track 2: Cardiovascular Health in Women

> This project is a student data analysis. It is not medical advice, a diagnostic tool or clinical guidance.

## Team Trench

| Name | Role |
|---|---|
|Adam |Repo and cleaning |
|Gabriella |Analysis |
|Maneli |Slides and Article |
|Ava |Slides and Article |

## Research Question

Among women aged about 30 to 65, do cholesterol and glucose levels tell us anything about cardiovascular disease beyond age and blood pressure?

## Datasets Used

- [x] Dataset 1: Cardiovascular Disease Dataset
- [ ] Dataset 2: Heart Attack Risk Prediction Dataset (synthetic)
- [ ] Dataset 3: Global CVD in Women, Tables S1 and S2

## How to Run

1. The raw files are already in `track-02/data/` (see the [data guide](../data/README.md)). On Colab the first notebook cell downloads them.
2. Install packages: `pip install -r requirements.txt`
3. Run `notebooks/01_cleaning.ipynb`, then `notebooks/02_analysis.ipynb`, top to bottom.

## Files

| Path | Contents |
|---|---|
| `notebooks/01_cleaning.ipynb` | Loads and cleans the data, writes the cleaning log |
| `notebooks/02_analysis.ipynb` | Summary statistics, models, checks and the headline visual |
| `src/` | Helper functions (optional) |
| `figures/` | Exported graphs, including `headline.png` |
| `docs/cleaning_log.md` | Each cleaning rule and the records affected |
| `docs/article.md` | Science communication article, following the [HUDP article guide](../../docs/article-guide.md) |
| `requirements.txt` | Python packages |

## Key Findings

Among 44,639 women aged 30 to 65, cholesterol stayed strongly associated with cardiovascular disease (CVD) after accounting for age, systolic blood pressure and glucose. Women with well above normal cholesterol had about three times the odds of CVD compared with women with normal cholesterol. Adding cholesterol improved prediction slightly beyond age and blood pressure, and glucose added nothing further once cholesterol was included.

**Odds ratios from the main logistic regression model (all factors in one model):**

| Factor | Odds ratio | 95% CI |
|---|---|---|
| Cholesterol above normal (vs normal) | 1.45 | 1.36 to 1.55 |
| Cholesterol well above normal (vs normal) | 3.09 | 2.84 to 3.37 |
| Glucose above normal (vs normal) | 1.04 | 0.95 to 1.13 |
| Glucose well above normal (vs normal) | 0.74 | 0.68 to 0.82 |
| Age, per year | 1.06 | 1.05 to 1.06 |
| Systolic blood pressure, per mmHg | 1.06 | 1.06 to 1.07 |

**How well each model predicts CVD (held-out AUC, where 0.5 is a coin flip and 1 is perfect):**

| Model | AUC |
|---|---|
| Age and blood pressure only | 0.787 |
| Adding glucose | 0.788 |
| Adding cholesterol | 0.798 |
| Adding both (main model) | 0.798 |

Adding cholesterol raised the AUC by about 0.011. Adding glucose on top of cholesterol did not change it.

**Glucose well above normal, compared with normal:**

| Model | Odds ratio (95% CI) |
|---|---|
| Accounting for age and blood pressure | 1.41 (1.30 to 1.53) |
| Also accounting for cholesterol | 0.74 (0.68 to 0.82) |

High glucose and high cholesterol tend to occur in the same women. Once cholesterol is in the model, glucose adds no independent information and its odds ratio falls below 1. This reflects that overlap, not a protective effect of high glucose.



## Limitations

- **Association, not cause.** Each woman was measured only once, so we cannot claim that lowering cholesterol would prevent CVD. That would take longitudinal studies that follow people over time
- **Unknown sample.** We do not know where, when or how the patients were chosen, and nearly half of them have CVD. They may not represent women in general, and the data cannot estimate how common CVD is
- **Limited age range.** Ages run from about 30 to 65, so findings may not apply to older women
- **Coarse measurements.** Cholesterol and glucose come in three broad levels (normal, above normal, well above normal) rather than lab values, and the cutoffs are not documented
- **Rounded blood pressure.** Many systolic readings are exactly 120 or 140, which suggests rounding
- **No diagnoses or medications.** The data has no diabetes diagnoses or medication records, so we cannot test whether treatment explains the glucose result
- **Overlapping risk factors.** Glucose and cholesterol tend to rise together, which makes their separate effects hard to untangle
- **Undefined outcome.** CVD is a single yes-or-no label, and the dataset does not say which conditions count
- **Binary sex, inferred.** Sex is recorded only as a binary code, so our results cannot speak beyond it. The code for women was inferred from average height (161 vs 170 cm)

## Presentation

Video link: [(https://youtu.be/1RYAbYoPz4Y)](https://youtu.be/1RYAbYoPz4Y)
