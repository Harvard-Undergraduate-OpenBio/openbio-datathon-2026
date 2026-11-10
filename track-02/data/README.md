# Track 02 Data Files

[![Back](https://img.shields.io/badge/Back-Track_Overview-13deba?style=flat-square)](../README.md)
[![Data Guide](https://img.shields.io/badge/Guide-2_The_Data-0fe995?style=flat-square)](../2-the-data.md)

The file reference for Track 2. For a plain-language explanation start with [Understand the data](../2-the-data.md).

> **Status:** Files marked Pending will be filled in at release. Until then they are empty placeholders.

```
data/
├── cardiovascular_dataset_OpenBio_Final.csv          Dataset 1
├── heart_attack_prediction_dataset_OpenBio_Final.csv Dataset 2
└── gbd/                                              Dataset 3
    ├── table_s1 (CSV or Excel)                       MIR by region
    └── table_s2 (CSV or Excel)                       Country SDI and incidence
```

| # | Dataset | File | Level | Source | Status |
|---|---|---|---|---|---|
| 1 | Cardiovascular Disease Dataset | `cardiovascular_dataset_OpenBio_Final.csv` | Individual | [Kaggle](https://www.kaggle.com/datasets/sulianova/cardiovascular-disease-dataset) | Pending |
| 2 | Heart Attack Risk Prediction Dataset | `heart_attack_prediction_dataset_OpenBio_Final.csv` | Individual (synthetic) | [Kaggle](https://www.kaggle.com/datasets/iamsouravbanerjee/heart-attack-prediction-dataset) | Pending |
| 3 | Global CVD in Women (GBD) | `gbd/table_s1.*` and `gbd/table_s2.*` | Population (region and country) | [Research article, PMC12237364](https://pmc.ncbi.nlm.nih.gov/articles/PMC12237364/) | Pending |

The cleaning notebook finds files here automatically. It also checks the Colab file panel and a `datathon` folder in Google Drive, so uploaded copies work too.

Do not edit these files. All cleaning happens in [`01_cleaning.ipynb`](../team/notebooks/01_cleaning.ipynb), which writes cleaned copies to `team/data_clean/`.
