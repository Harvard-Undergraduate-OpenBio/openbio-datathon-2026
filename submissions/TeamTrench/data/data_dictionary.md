# Track 02 Data Dictionary

[![Back](https://img.shields.io/badge/Back-Data_Files-13deba?style=flat-square)](README.md)
[![Data Guide](https://img.shields.io/badge/Guide-2_The_Data-0fe995?style=flat-square)](../2-the-data.md)

Every column in the Track 2 files, checked against the files in this folder on 2026-11-13. The counts below were computed from those files. The "What is in the file" notes describe the raw values. They are not cleaning rules. Deciding what to keep is your job, and each decision belongs in your cleaning log.

## Dataset 1: `cardiovascular_dataset_OpenBio_Final.csv`

70,000 rows, 13 columns, one row per patient. Semicolon-separated, so load it with `pd.read_csv(path, sep=";")`. No missing values. Source: [Kaggle](https://www.kaggle.com/datasets/sulianova/cardiovascular-disease-dataset), where the file is called `cardio_train.csv`.

| Column | Meaning | Type on Kaggle | Coding and unit | What is in the file |
|---|---|---|---|---|
| `id` | Row identifier | | Whole number | Unique. Runs from 0 to 99,999 with gaps |
| `age` | Age | Objective | **Days** | 10,798 to 23,713 days, about 30 to 65 years |
| `gender` | Sex | Objective | 1 = women, 2 = men | 45,530 rows with code 1 and 24,470 with code 2 |
| `height` | Height | Objective | cm | 55 to 250 |
| `weight` | Weight | Objective | kg, can have decimals | 10 to 200 |
| `ap_hi` | Systolic blood pressure | Examination | mmHg | -150 to 16,020 |
| `ap_lo` | Diastolic blood pressure | Examination | mmHg | -70 to 11,000 |
| `cholesterol` | Cholesterol | Examination | 1 = normal, 2 = above normal, 3 = well above normal | Ordered category |
| `gluc` | Glucose | Examination | 1 = normal, 2 = above normal, 3 = well above normal | Ordered category |
| `smoke` | Smoking | Subjective | 0 = no, 1 = yes | 6,169 rows with 1 |
| `alco` | Alcohol intake | Subjective | 0 = no, 1 = yes | 3,764 rows with 1 |
| `active` | Physical activity | Subjective | 0 = no, 1 = yes | 56,261 rows with 1 |
| `cardio` | Has cardiovascular disease (the outcome) | Target | 0 = no, 1 = yes | 34,979 rows with 1, almost exactly half |

Objective means a fact about the patient. Examination means a result from the medical exam. Subjective means the patient reported it.

Things the Kaggle page does not tell you:

- **Which gender code is women.** The page says only "categorical code". Code 1 has the lower mean height (161.4 cm against 169.9 cm for code 2), which is why this track treats 1 as women. The cleaning notebook repeats this check.
- **What 0 and 1 mean** for `smoke`, `alco`, `active` and `cardio`. The page says "binary". This track reads 1 as yes.
- **Where and when the data were collected.** The page says only that values were recorded at a medical examination.

Known quirks:

- Systolic is lower than diastolic in 1,234 rows. 7 rows have a negative `ap_hi` and 1 has a negative `ap_lo`.
- 953 rows have `ap_lo` above 200 and 40 rows have `ap_hi` above 300.
- 24 rows match another row in every column except `id`.

## Dataset 2: `heart_attack_prediction_dataset_OpenBio_Final.csv`

8,763 rows, 26 columns, one row per synthetic patient. Comma-separated. No missing values. Source: [Kaggle](https://www.kaggle.com/datasets/iamsouravbanerjee/heart-attack-prediction-dataset), where the file is called `heart_attack_prediction_dataset.csv`. The Kaggle page says the dataset was generated with ChatGPT.

The Kaggle page gives no units. The "What is in the file" column shows the range you will see.

| Column | Meaning | What is in the file |
|---|---|---|
| `Patient ID` | Record identifier | Three letters and four digits, such as `BMW7812`. Unique |
| `Age` | Age in years | 18 to 90 |
| `Sex` | Sex | Text: `Male` (6,111 rows) or `Female` (2,652 rows) |
| `Cholesterol` | Cholesterol level | 120 to 400 |
| `Blood Pressure` | Systolic and diastolic together | Text such as `158/88`. Systolic 90 to 180, diastolic 60 to 110 |
| `Heart Rate` | Heart rate | 40 to 110 |
| `Diabetes` | Has diabetes | 0 = no, 1 = yes |
| `Family History` | Family history of heart problems | 0 = no, 1 = yes |
| `Smoking` | Smoker | 0 = no, 1 = yes. About 90% of rows are 1 |
| `Obesity` | Obese | 0 = no, 1 = yes |
| `Alcohol Consumption` | Drinks alcohol | 0 = no, 1 = yes |
| `Exercise Hours Per Week` | Hours of exercise per week | 0 to 20, with decimals |
| `Diet` | Diet quality | Text: `Unhealthy`, `Average` or `Healthy` |
| `Previous Heart Problems` | Earlier heart problems | 0 = no, 1 = yes |
| `Medication Use` | Takes medication | 0 = no, 1 = yes |
| `Stress Level` | Self-reported stress | Whole numbers 1 to 10 |
| `Sedentary Hours Per Day` | Hours sitting per day | 0 to 12, with decimals |
| `Income` | Income | 20,062 to 299,954. Currency not stated |
| `BMI` | Body mass index | 18 to 40, with decimals |
| `Triglycerides` | Triglyceride level | 30 to 800 |
| `Physical Activity Days Per Week` | Days with physical activity | Whole numbers 0 to 7 |
| `Sleep Hours Per Day` | Hours of sleep | Whole numbers 4 to 10 |
| `Country` | Country | 20 countries, short names such as `United States` and `Vietnam` |
| `Continent` | Continent | 6 values. `Australia` is used for Australia and New Zealand |
| `Hemisphere` | Hemisphere | `Northern Hemisphere` or `Southern Hemisphere` |
| `Heart Attack Risk` | Heart attack risk (the outcome) | 0 = no, 1 = yes. 3,139 rows with 1, about 36% |

Where the file differs from its Kaggle description:

- **Diabetes** is described as Yes/No. The file holds 0 and 1.
- **Alcohol Consumption** is described as None, Light, Moderate or Heavy. The file holds only 0 and 1.

Known quirks:

- Systolic is lower than diastolic in 391 rows and equal to it in 40 rows.
- Italy and Spain are labelled `Southern Hemisphere`.
- Country names are short forms. Table S2 spells some of the same places differently.

## Dataset 3: Tables S1 and S2

Both files are copied cell for cell from the Word supplement of [Li et al., Medicine (2025)](https://pmc.ncbi.nlm.nih.gov/articles/PMC12237364/). Row and column numbers below start at 0, the way pandas shows them when you load with `header=None`.

### `gbd/table_s1.csv`

32 rows, 3 columns.

| Row | Contents |
|---|---|
| 0 | Table title |
| 1 | Column headers. The first one is empty |
| 2 | `Global Female` |
| 3 | Label row `Socio-demographic index`, no numbers |
| 4 to 8 | The five SDI regions: Low, Low-middle, Middle, High-middle, High |
| 9 | Label row `GBD regions`, no numbers |
| 10 to 30 | The 21 GBD regions |
| 31 | Footnote explaining GBD and SDI |

| Column | Printed header | Meaning |
|---|---|---|
| 0 | (empty) | Region name. Names under a label row start with three spaces |
| 1 | `MIR per 100,000 in 1990` | Mortality-to-incidence ratio for CVD in women, 1990 |
| 2 | `MIR per 100,000 in 2019` | The same ratio in 2019 |

The printed header says "per 100,000", but the article defines MIR as the crude mortality rate divided by the crude incidence rate. The values run from 0.12 to 0.56, which fits a plain ratio. Table S1 has no intervals.

### `gbd/table_s2.csv`

207 rows, 11 columns. Row 0 is the table title. Rows 1 and 2 are a two-row header: row 1 holds `1990`, `2019` and `1990-2019` over the columns they cover, and row 2 holds the column names. Rows 3 to 206 are the 204 countries and territories. Columns 3, 6 and 9 are empty spacers.

| Column | Header row 1 | Header row 2 | Meaning | Format |
|---|---|---|---|---|
| 0 | `Region` | | Country or territory name, as GBD spells it | Text |
| 1 | `1990` | `Incident cases No.  (95% UI)` | New CVD cases in women, 1990 | `37223.4 (34624.49, 39944.22)` |
| 2 | | `ASIR per 100, 000 No. (95% UI)` | Age-standardized incidence rate per 100,000 women, 1990 | `1083.58 (1011.93, 1164.76)` |
| 4 | `2019` | `Incident cases No.  (95% UI)` | New CVD cases in women, 2019 | Same as column 1 |
| 5 | | `ASIR per 100, 000 No. (95% UI)` | Age-standardized incidence rate per 100,000 women, 2019 | Same as column 2 |
| 7 | `1990-2019` | `Percentage change of incident cases (%)` | Change in the number of new cases from 1990 to 2019 | Plain number such as `106.07` |
| 8 | | `EAPC (95% CI) ` | Estimated annual percentage change in ASIR, 1990 to 2019 | `-0.25 (-0.31, -0.2)` |
| 10 | `SDI value in 2019` | | Socio-demographic index in 2019, from 0 to 1 | Plain number such as `0.343` |

Reading the intervals: the first number is the estimate and the two numbers in brackets are the lower and upper ends. UI is an uncertainty interval and CI is a confidence interval. An EAPC interval that includes 0 means the rate was stable.

Known quirks:

- Every SDI value ends with a space, such as `0.343 `. So does every number in Table S1.
- Trailing zeros are dropped, so `37223.4` and `-0.2` appear beside values with two decimals.
- Country names follow GBD spelling, such as `United States of America` and `Viet Nam`. Dataset 2 uses shorter names.

Terms such as SDI, ASIR, MIR and EAPC are explained in the [glossary](../glossary.md).
