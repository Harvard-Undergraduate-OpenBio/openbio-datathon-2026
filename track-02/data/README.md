# Track 02 Data Files

[![Back](https://img.shields.io/badge/Back-Track_Overview-13deba?style=flat-square)](../README.md)
[![Data Guide](https://img.shields.io/badge/Guide-2_The_Data-0fe995?style=flat-square)](../2-the-data.md)

The file reference for Track 2. For a plain-language explanation start with [Understand the data](../2-the-data.md). For setup steps see [Setup](../1-setup.md).

> **Status:** All files are available. Package version **v1.0.0**, released 2026-11-13.

## How to Get the Data

Every file is stored in this folder, so there is nothing to request or unlock. You do not need a Kaggle account.

| Option | How |
|---|---|
| Google Colab | Run the first cell of [`01_cleaning.ipynb`](../team/notebooks/01_cleaning.ipynb). It finds the files, or fetches the repository if they are not there |
| Everything at once | [Download the repository as a ZIP](https://github.com/Harvard-Undergraduate-OpenBio/openbio-datathon-2026/archive/refs/heads/main.zip), unzip it and open `track-02/data` |
| With git | `git clone https://github.com/Harvard-Undergraduate-OpenBio/openbio-datathon-2026.git` |
| One file | Click a **Download** link in the table below. If the file opens as text in your browser, right-click the link and choose **Save link as** |

To load the files straight from GitHub in Python:

```python
import pandas as pd
base = "https://github.com/Harvard-Undergraduate-OpenBio/openbio-datathon-2026/raw/main/track-02/data/"
df1 = pd.read_csv(base + "cardiovascular_dataset_OpenBio_Final.csv", sep=";")   # semicolon-separated
df2 = pd.read_csv(base + "heart_attack_prediction_dataset_OpenBio_Final.csv")
s1 = pd.read_csv(base + "gbd/table_s1.csv", header=None)                        # header=None keeps the title and header rows
s2 = pd.read_csv(base + "gbd/table_s2.csv", header=None)
```

## Folder Layout

```
data/
├── cardiovascular_dataset_OpenBio_Final.csv            Dataset 1
├── heart_attack_prediction_dataset_OpenBio_Final.csv   Dataset 2
├── gbd/                                                Dataset 3
│   ├── table_s1.csv                                    MIR by region
│   └── table_s2.csv                                    Country SDI and incidence
├── data_dictionary.md                                  What every column means
└── provenance/
    ├── checksums.sha256                                File fingerprints
    ├── source_manifest.md                              Sources and licenses
    ├── transformation_log.md                           Every change made to the sources
    ├── source_checksums.txt                            Fingerprints of the downloaded sources
    └── build_scripts/                                  Script the organizers used for Tables S1 and S2
```

## The Files

| # | File | Contents | Size | Get it |
|---|---|---|---|---|
| 1 | [`cardiovascular_dataset_OpenBio_Final.csv`](cardiovascular_dataset_OpenBio_Final.csv) | 70,000 patients as rows, 13 columns, both sexes. **Semicolon-separated** | 2.9 MB | [Download](https://github.com/Harvard-Undergraduate-OpenBio/openbio-datathon-2026/raw/main/track-02/data/cardiovascular_dataset_OpenBio_Final.csv) |
| 2 | [`heart_attack_prediction_dataset_OpenBio_Final.csv`](heart_attack_prediction_dataset_OpenBio_Final.csv) | 8,763 synthetic records as rows, 26 columns, both sexes. Comma-separated | 1.5 MB | [Download](https://github.com/Harvard-Undergraduate-OpenBio/openbio-datathon-2026/raw/main/track-02/data/heart_attack_prediction_dataset_OpenBio_Final.csv) |
| 3 | [`gbd/table_s1.csv`](gbd/table_s1.csv) | Table S1: mortality-to-incidence ratio for CVD in women, 1990 and 2019. One global row, 5 SDI regions and 21 GBD regions | 1 KB | [Download](https://github.com/Harvard-Undergraduate-OpenBio/openbio-datathon-2026/raw/main/track-02/data/gbd/table_s1.csv) |
| 3 | [`gbd/table_s2.csv`](gbd/table_s2.csv) | Table S2: 204 countries and territories with incident cases and ASIR in 1990 and 2019, the change between them and SDI in 2019 | 33 KB | [Download](https://github.com/Harvard-Undergraduate-OpenBio/openbio-datathon-2026/raw/main/track-02/data/gbd/table_s2.csv) |
| | [`data_dictionary.md`](data_dictionary.md) | Every column in all four files, with coding and known quirks | 9 KB | [Download](https://github.com/Harvard-Undergraduate-OpenBio/openbio-datathon-2026/raw/main/track-02/data/data_dictionary.md) |

Sources: Dataset 1 is the [Cardiovascular Disease dataset](https://www.kaggle.com/datasets/sulianova/cardiovascular-disease-dataset) on Kaggle. Dataset 2 is the [Heart Attack Risk Prediction Dataset](https://www.kaggle.com/datasets/iamsouravbanerjee/heart-attack-prediction-dataset) on Kaggle. Dataset 3 comes from the supplement of [Li et al., Medicine (2025)](https://pmc.ncbi.nlm.nih.gov/articles/PMC12237364/).

## What to Expect When You Open Them

These are raw files. Nothing has been cleaned or filtered, because cleaning is part of the challenge.

- **Datasets 1 and 2 are the Kaggle files, byte for byte.** Only the file names changed.
- **Dataset 1 uses semicolons.** Without `sep=";"` it loads as a single column. GitHub's preview also shows it as one column.
- **Tables S1 and S2 are copied cell for cell from the article's supplement.** The first row is the table title. Table S2 has a two-row header and empty spacer columns. Table S1 has label rows and a footnote row.

The [data dictionary](data_dictionary.md) lists every column and quirk. The cleaning notebook handles the loading for you.

Do not edit these files. All cleaning happens in [`01_cleaning.ipynb`](../team/notebooks/01_cleaning.ipynb), which writes cleaned copies to `team/data_clean/`. It also checks the Colab file panel and a `datathon` folder in Google Drive, so uploaded copies work too.

## Provenance

| File | Contents | Get it |
|---|---|---|
| [`provenance/checksums.sha256`](provenance/checksums.sha256) | SHA-256 checksum for each of the four data files | [Download](https://github.com/Harvard-Undergraduate-OpenBio/openbio-datathon-2026/raw/main/track-02/data/provenance/checksums.sha256) |
| [`provenance/source_manifest.md`](provenance/source_manifest.md) | Original sources and their licenses | [Download](https://github.com/Harvard-Undergraduate-OpenBio/openbio-datathon-2026/raw/main/track-02/data/provenance/source_manifest.md) |
| [`provenance/transformation_log.md`](provenance/transformation_log.md) | How each file was derived from its source | [Download](https://github.com/Harvard-Undergraduate-OpenBio/openbio-datathon-2026/raw/main/track-02/data/provenance/transformation_log.md) |
| [`provenance/source_checksums.txt`](provenance/source_checksums.txt) | SHA-256 checksum for every downloaded source file | [Download](https://github.com/Harvard-Undergraduate-OpenBio/openbio-datathon-2026/raw/main/track-02/data/provenance/source_checksums.txt) |

The package is frozen at v1.0.0. Any change gets a new version number and updated checksums.

## Check Your Copy

From `track-02/data`, run:

```bash
sha256sum -c provenance/checksums.sha256       # Linux or Windows WSL
shasum -a 256 -c provenance/checksums.sha256   # macOS
```

Every line should end in `OK`.

## Licenses

Each source keeps its own terms. Read the [source manifest](provenance/source_manifest.md) before reusing these files outside the datathon, and cite every dataset you use ([citations](../reference/citations.md)).
