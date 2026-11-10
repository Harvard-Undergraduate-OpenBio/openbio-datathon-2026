# Step 2: Understand the Data

[![Back](https://img.shields.io/badge/Back-1_Setup-13deba?style=flat-square)](1-setup.md)
[![Next](https://img.shields.io/badge/Next-3_Workflow-0fe995?style=flat-square)](3-workflow.md)

> **Status:** Files marked Pending in the [data folder](data/README.md) will be filled in at release. Until then they are empty placeholders.

The three datasets look at the same problem at different scales. Datasets 1 and 2 have one row per person. Dataset 3 has one row per region or country. You can use one dataset or combine insights across them, but you cannot join them row by row.

## Dataset 1: Cardiovascular Disease Dataset

**File:** `cardiovascular_dataset_OpenBio_Final.csv` · **Source:** [Kaggle](https://www.kaggle.com/datasets/sulianova/cardiovascular-disease-dataset)

About 70,000 patients, one row each. Every value was recorded at a medical exam. `cardio` is the outcome: whether the patient has cardiovascular disease.

| Column | Meaning | Coding |
|---|---|---|
| `age` | Age | **Days**, not years |
| `gender` | Sex | 1 = women, 2 = men |
| `height`, `weight` | Body size | cm and kg |
| `ap_hi`, `ap_lo` | Systolic and diastolic blood pressure (the top and bottom numbers) | mmHg |
| `cholesterol`, `gluc` | Cholesterol and glucose | 1 = normal, 2 = above normal, 3 = well above normal |
| `smoke`, `alco`, `active` | Smoking, alcohol, physical activity (self-reported) | 0 = no, 1 = yes |
| `cardio` | Has cardiovascular disease | 0 = no, 1 = yes |

**Watch for:**

- **Age is in days.** Convert to years before any analysis or plot.
- **Filter to women** using `gender`. Check the coding by comparing average height for each code.
- **Blood pressure has impossible values:** negative numbers, systolic lower than diastolic, readings in the thousands. Decide on a plausibility rule and document it.
- **Check height and weight** for implausible values, and calculate BMI only after cleaning them.
- **Cholesterol and glucose are ordered categories,** not measurements. A 3 is higher than a 2, but not "50% more."

## Dataset 2: Heart Attack Risk Prediction Dataset

**File:** `heart_attack_prediction_dataset_OpenBio_Final.csv` · **Source:** [Kaggle](https://www.kaggle.com/datasets/iamsouravbanerjee/heart-attack-prediction-dataset)

8,763 **synthetic** records, meaning a computer generated them to look like patients from around the world. `Heart Attack Risk` is the outcome (0 or 1). Columns cover clinical measures (cholesterol, blood pressure, BMI), lifestyle (diet, exercise, sleep, stress), medical history, income and geography (country, continent, hemisphere).

**Watch for:**

- **Blood Pressure is one text field,** such as `158/88`. Split it into systolic and diastolic number columns.
- **Mixed formats.** Some variables are Yes/No text and some are levels (Alcohol Consumption, Diet). Encode them thoughtfully and keep ordered levels in order.
- **Synthetic data behave differently.** Relationships may be weaker, stronger or simply different from real clinical data. Treat any model here as a methods exercise, not clinical evidence, and say so.
- **Both sexes are included.** Decide whether to analyze women only or compare women with men, and justify the choice.

## Dataset 3: Global CVD in Women (GBD)

**Files:** Supplementary Tables S1 and S2 in `data/gbd/` · **Source:** [Li et al., Medicine (2025)](https://pmc.ncbi.nlm.nih.gov/articles/PMC12237364/)

Tables from a published study of CVD in women using Global Burden of Disease (GBD) estimates, 1990 to 2019.

| Table | Contents |
|---|---|
| S1 | Mortality-to-incidence ratio (MIR) for CVD in women, by SDI region and GBD region, 1990 and 2019 |
| S2 | For 204 countries and territories: SDI in 2019, incident cases and age-standardized incidence rates (ASIR) in 1990 and 2019, and the trend from 1990 to 2019 |

Key terms (more in the [glossary](glossary.md)):

- **SDI (socio-demographic index):** a 0 to 1 score of a country's development, combining income, education and fertility. Higher means more developed.
- **ASIR (age-standardized incidence rate):** new cases per 100,000 women, adjusted so countries with older or younger populations can be compared fairly.
- **MIR (mortality-to-incidence ratio):** deaths divided by new cases. A rough signal of how deadly or poorly managed disease is relative to how often it occurs. Read the article's definition before interpreting it.

**Watch for:**

- **These are group statistics, not patients.** A pattern across countries does not tell you about individual women (the ecological fallacy).
- **Messy tables.** Expect wide layouts with multiple header rows. You will need to reshape them (wide to long), standardize country names and split confidence intervals stored as text, such as `963.95 (850.1 to 1080.2)`.
- **Table S2 holds the SDI and trend columns** you need to connect burden to development level.

## Full File List

See [`data/README.md`](data/README.md) for every file and its status.
