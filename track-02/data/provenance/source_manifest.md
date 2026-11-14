# Track 02 Source Manifest

[![Back](https://img.shields.io/badge/Back-Data_Files-13deba?style=flat-square)](../README.md)

Package version: **v1.0.0**. All sources were downloaded on 2026-11-13. SHA-256 checksums of every downloaded source file are in [`source_checksums.txt`](source_checksums.txt).

## Sources Used to Build Released Files

| Source | What was downloaded | Used for | License or terms |
|---|---|---|---|
| Kaggle [Cardiovascular Disease dataset](https://www.kaggle.com/datasets/sulianova/cardiovascular-disease-dataset) by Svetlana Ulianova, version 1, last updated 2019-01-20 | `cardio_train.csv` (2,941,524 bytes) | `cardiovascular_dataset_OpenBio_Final.csv` | Kaggle lists the license as **Unknown**. No reuse terms are stated on the page |
| Kaggle [Heart Attack Risk Prediction Dataset](https://www.kaggle.com/datasets/iamsouravbanerjee/heart-attack-prediction-dataset) by Sourav Banerjee, version 2, last updated 2024-05-11 | `heart_attack_prediction_dataset.csv` (1,456,385 bytes) | `heart_attack_prediction_dataset_OpenBio_Final.csv` | Kaggle lists the license as **Other (specified in description)**. The description says the data are synthetic, generated with ChatGPT for beginners to practice on. It names no formal license |
| Li Y, Yin N, Li C, Yang S-W. Global burden of cardiovascular disease in women, 1990-2019. Medicine (Baltimore). 2025;104(27):e43215. [PMC12237364](https://pmc.ncbi.nlm.nih.gov/articles/PMC12237364/), DOI [10.1097/MD.0000000000043215](https://doi.org/10.1097/MD.0000000000043215) | Supplement `medi-104-e43215-s001.docx` (2,620,719 bytes) from the [PMC Open Access cloud service](https://pmc.ncbi.nlm.nih.gov/tools/pmcaws/). The publisher's copy at [links.lww.com/MD/P340](https://links.lww.com/MD/P340) has the same checksum | `gbd/table_s1.csv` and `gbd/table_s2.csv` | [CC BY-NC 4.0](https://creativecommons.org/licenses/by-nc/4.0/). Attribution required. Commercial use needs permission from the journal |

## Notes on Each Source

**Dataset 1.** The Kaggle page describes three kinds of input (objective, examination and subjective) and says all values were collected at a medical examination. It does not say where or when.

**Dataset 2.** The Kaggle page states: "This dataset is a synthetic creation generated using ChatGPT to simulate a realistic experience." These are not real patients.

**Dataset 3.** The article's license statement reads: "This is an open-access article distributed under the terms of the Creative Commons Attribution-Non Commercial License 4.0 (CCBY-NC), where it is permissible to download, share, remix, transform, and buildup the work provided it is properly cited. The work cannot be used commercially without permission from the journal." The estimates in the tables come from the Global Burden of Disease Study 2019, published by the Institute for Health Metrics and Evaluation (IHME). IHME has its own [terms of use](https://www.healthdata.org/data-tools-practices/data-practices/terms-and-conditions) for GBD data.

## Sources Linked but Not Distributed

| Source | Role | License or terms |
|---|---|---|
| [GBD Results Tool](https://vizhub.healthdata.org/gbd-results/) | Where the article's authors obtained the underlying estimates. Not downloaded for this build | IHME terms of use |

## How to Cite

See [`reference/citations.md`](../../reference/citations.md).
