# Track 02 Transformation Log

[![Back](https://img.shields.io/badge/Back-Data_Files-13deba?style=flat-square)](../README.md)

Package version: **v1.0.0**, built 2026-11-13. Every change made between the downloaded sources and the released files is listed here. Sources and licenses are in the [source manifest](source_manifest.md).

No released file has been cleaned. No row, column or value was removed, corrected or recoded.

## Dataset 1

| # | Step | Detail |
|---|---|---|
| 1 | Download | `cardiovascular-disease-dataset.zip` from Kaggle. It holds one file, `cardio_train.csv` |
| 2 | Rename | `cardio_train.csv` saved as `cardiovascular_dataset_OpenBio_Final.csv` |
| 3 | Verify | The released file has the same SHA-256 checksum as `cardio_train.csv`. It is 70,000 rows by 13 columns, semicolon-separated |

## Dataset 2

| # | Step | Detail |
|---|---|---|
| 1 | Download | `heart-attack-prediction-dataset.zip` from Kaggle. It holds one file, `heart_attack_prediction_dataset.csv` |
| 2 | Rename | Saved as `heart_attack_prediction_dataset_OpenBio_Final.csv` |
| 3 | Verify | The released file has the same SHA-256 checksum as the Kaggle file. It is 8,763 rows by 26 columns, comma-separated, with Windows line endings as on Kaggle |

## Dataset 3: Tables S1 and S2

Script: [`build_scripts/build_gbd_tables.py`](build_scripts/build_gbd_tables.py)

The supplement is a Word file with several tables and figures. Tables S1 and S2 were copied into CSV files so that pandas can read them. The layout was kept as printed.

| # | Step | Detail |
|---|---|---|
| 1 | Download | `medi-104-e43215-s001.docx` from the PMC Open Access cloud service. Its MD5 checksum matches the one PMC lists for the article, and the publisher's copy is identical |
| 2 | Select tables | The two Word tables whose first cell starts with `Table S1.` and `Table S2.` Nothing else in the supplement is released |
| 3 | Copy the grid | One CSV row for each Word table row and one CSV column for each Word grid column. Table S1 is 32 rows by 3 columns. Table S2 is 207 rows by 11 columns |
| 4 | Merged cells | Text stays in the top-left position of a merged cell. The other positions it covered are left empty, as a spreadsheet would show them |
| 5 | Line breaks inside a cell | Replaced with one space. This affects header cells only |
| 6 | Cell text | Kept exactly, including leading and trailing spaces. Numbers were not reformatted |
| 7 | Encoding | UTF-8 with Unix line endings |
| 8 | Verify | Every data cell was compared with a second, independent read of the Word file and matched. Table S2 has 204 distinct country names. Its 2019 incident cases add up to 27.62 million, the global total quoted in the article |

To rebuild both tables: `pip install python-docx`, then `python build_scripts/build_gbd_tables.py medi-104-e43215-s001.docx gbd`.

## Files Changed in the Repository

`.gitattributes` now marks `track-02/data/**` as `-text` so git never rewrites line endings in the data files.
