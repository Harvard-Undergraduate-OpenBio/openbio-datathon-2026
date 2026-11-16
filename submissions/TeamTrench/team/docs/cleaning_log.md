# Cleaning Log

Written by `01_cleaning.ipynb`. Rerun the notebook to update it.

| Dataset | Rule | Reason | Records before | Records after | Records affected |
|---|---|---|---|---|---|
| D1 | Drop duplicate ids | Each patient should appear once | 70,000 | 70,000 | 0 |
| D1 | Drop rows identical in every column except id | Two patients matching on age in days and every measurement is far more likely a repeated entry | 70,000 | 69,976 | 24 |
| D1 | Keep women only | Track focus on women | 69,976 | 45,509 | 24,467 |
| D1 | Keep ap_hi between 70 and 250 | Systolic pressure outside 70 to 250 mmHg is not compatible with a routine exam and suggests an entry error | 45,509 | 45,358 | 151 |
| D1 | Keep ap_lo between 40 and 150 | Diastolic pressure outside 40 to 150 mmHg is not compatible with a routine exam and suggests an entry error | 45,358 | 44,754 | 604 |
| D1 | Keep height between 130 and 200 | Adult heights outside 130 to 200 cm are rare enough to be likely entry errors | 44,754 | 44,699 | 55 |
| D1 | Keep weight between 35 and 200 | Adult weights under 35 kg are implausible at these heights | 44,699 | 44,687 | 12 |
| D1 | Keep rows where systolic > diastolic | Systolic is always higher than diastolic | 44,687 | 44,639 | 48 |
