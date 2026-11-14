# Step 2: Understand the Data

[![Back](https://img.shields.io/badge/Back-1_Setup-13deba?style=flat-square)](1-setup.md)
[![Next](https://img.shields.io/badge/Next-3_Workflow-0fe995?style=flat-square)](3-workflow.md)

> **Status:** All files are in the [data folder](data/README.md), ready to download. Every column is listed in the [data dictionary](data/data_dictionary.md).

The three datasets look at the same problem at different scales. Datasets 1 and 2 have one row per person. Dataset 3 has one row per region or country. You can use one dataset or combine insights across them, but you cannot join them row by row.

## Dataset 1: Cardiovascular Disease Dataset

**File:** [`cardiovascular_dataset_OpenBio_Final.csv`](data/cardiovascular_dataset_OpenBio_Final.csv) ([download](https://github.com/Harvard-Undergraduate-OpenBio/openbio-datathon-2026/raw/main/track-02/data/cardiovascular_dataset_OpenBio_Final.csv)) · **Source:** [Kaggle](https://www.kaggle.com/datasets/sulianova/cardiovascular-disease-dataset)

70,000 patients, one row each, men and women together. Every value was recorded at a medical exam. `cardio` is the outcome: whether the patient has cardiovascular disease.

| Column | Meaning | Coding |
|---|---|---|
| `id` | Row identifier | Whole number |
| `age` | Age | **Days**, not years |
| `gender` | Sex | 1 = women, 2 = men |
| `height`, `weight` | Body size | cm and kg |
| `ap_hi`, `ap_lo` | Systolic and diastolic blood pressure (the top and bottom numbers) | mmHg |
| `cholesterol`, `gluc` | Cholesterol and glucose | 1 = normal, 2 = above normal, 3 = well above normal |
| `smoke`, `alco`, `active` | Smoking, alcohol, physical activity (self-reported) | 0 = no, 1 = yes |
| `cardio` | Has cardiovascular disease | 0 = no, 1 = yes |

**Watch for:**

- **The file is semicolon-separated.** Load it with `pd.read_csv(path, sep=";")`. Without `sep` it loads as a single column.
- **Age is in days.** Convert to years before any analysis or plot.
- **Filter to women** using `gender`. The Kaggle page does not say which code is women, so check by comparing average height for each code. Code 1 is the shorter group.
- **Blood pressure has impossible values:** negative numbers, systolic lower than diastolic, readings in the thousands. Decide on a plausibility rule and document it.
- **Check height and weight** for implausible values, and calculate BMI only after cleaning them.
- **Cholesterol and glucose are ordered categories,** not measurements. A 3 is higher than a 2, but not "50% more."

## Dataset 2: Heart Attack Risk Prediction Dataset

**File:** [`heart_attack_prediction_dataset_OpenBio_Final.csv`](data/heart_attack_prediction_dataset_OpenBio_Final.csv) ([download](https://github.com/Harvard-Undergraduate-OpenBio/openbio-datathon-2026/raw/main/track-02/data/heart_attack_prediction_dataset_OpenBio_Final.csv)) · **Source:** [Kaggle](https://www.kaggle.com/datasets/iamsouravbanerjee/heart-attack-prediction-dataset)

8,763 **synthetic** records, meaning a computer generated them to look like patients from around the world. `Heart Attack Risk` is the outcome (0 or 1). Columns cover clinical measures (cholesterol, blood pressure, BMI), lifestyle (diet, exercise, sleep, stress), medical history, income and geography (country, continent, hemisphere).

**Watch for:**

- **Blood Pressure is one text field,** such as `158/88`. Split it into systolic and diastolic number columns.
- **Mixed formats.** The yes/no variables are already stored as 1 and 0. That includes Diabetes and Alcohol Consumption, which the Kaggle page describes differently. Sex and Diet are text. Diet has ordered levels (Unhealthy, Average, Healthy), so keep them in order when you encode them.
- **Synthetic data behave differently.** Relationships may be weaker, stronger or simply different from real clinical data. Treat any model here as a methods exercise, not clinical evidence, and say so.
- **Both sexes are included.** Decide whether to analyze women only or compare women with men, and justify the choice.

## Dataset 3: Global CVD in Women (GBD)

**Files:** [`data/gbd/table_s1.csv`](data/gbd/table_s1.csv) ([download](https://github.com/Harvard-Undergraduate-OpenBio/openbio-datathon-2026/raw/main/track-02/data/gbd/table_s1.csv)) and [`data/gbd/table_s2.csv`](data/gbd/table_s2.csv) ([download](https://github.com/Harvard-Undergraduate-OpenBio/openbio-datathon-2026/raw/main/track-02/data/gbd/table_s2.csv)) · **Source:** [Li et al., Medicine (2025)](https://pmc.ncbi.nlm.nih.gov/articles/PMC12237364/)

Supplementary Tables S1 and S2 from a published study of CVD in women using Global Burden of Disease (GBD) estimates, 1990 to 2019. Each CSV is copied cell for cell from the article's supplement.

| Table | Contents |
|---|---|
| S1 | Mortality-to-incidence ratio (MIR) for CVD in women in 1990 and 2019: one global row, 5 SDI regions and 21 GBD regions |
| S2 | For 204 countries and territories: SDI in 2019, incident cases and age-standardized incidence rates (ASIR) in 1990 and 2019, and the trend from 1990 to 2019 |

Key terms (more in the [glossary](glossary.md)):

- **SDI (socio-demographic index):** a 0 to 1 score of a country's development, combining income, education and fertility. Higher means more developed.
- **ASIR (age-standardized incidence rate):** new cases per 100,000 women, adjusted so countries with older or younger populations can be compared fairly.
- **MIR (mortality-to-incidence ratio):** deaths divided by new cases. A rough signal of how deadly or poorly managed disease is relative to how often it occurs. Read the article's definition before interpreting it.

**Watch for:**

- **These are group statistics, not patients.** A pattern across countries does not tell you about individual women (the ecological fallacy).
- **Messy tables.** Load them with `header=None` and look before you trust the column names. The first row of each file is the table title. Table S2 has a two-row header (the year on top, the measure below) and empty spacer columns. Table S1 has label rows with no numbers and a footnote in its last row.
- **Intervals are stored as text,** such as `1083.58 (1011.93, 1164.76)`. Split them into an estimate, a lower bound and an upper bound. Table S1 has no intervals.
- **Reshape and rename.** Table S2 is wide, with 1990 and 2019 side by side, so you may need to reshape it (wide to long). Its country column is headed `Region` and uses GBD spellings such as `United States of America`.
- **Table S2 holds the SDI and trend columns** you need to connect burden to development level.

## Full File List

See [`data/README.md`](data/README.md) for every file and its download link.
