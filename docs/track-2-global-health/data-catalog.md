# Track 2: Data Catalog

## Dataset Manifest

| Dataset ID | Role | Source Title | Source URL | Access Level | Format | Distribution Policy | Notes |
|---|---|---|---|---|---|---|---|
| DHS_PROGRAM | Required | Demographic and Health Surveys | https://dhsprogram.com/ | Public registration required | Flat files (DTA, CSV) | OpenBio-derived aggregated dataset only; never store microdata | Requires pre-registration and approval; plan ahead |
| WHO_MNCAH | Reference | WHO Maternal, Newborn, Child and Adolescent Health | https://www.who.int/health-topics/maternal-newborn-child-adolescent-health | Public | Reports, databases | Link-only | Policy and guidelines context |
| WORLD_BANK | Reference | World Bank Open Data | https://data.worldbank.org/ | Public | API, CSV | Link-only | Country-level health expenditure, facility density, mortality |

## DHS Program Data Access

**Critical:** DHS Program data requires registration and approval. Do not store microdata in this repository.

OpenBio will:
1. Register and obtain approval for relevant DHS datasets before the datathon.
2. Create a permitted derived/aggregated challenge dataset.
3. Provide a codebook and reproducible extraction script.
4. Distribute only the derived dataset to participants.

## OpenBio-Derived Challenge Artifacts

| Artifact | Format | Description |
|---|---|---|
| DHS derived dataset | `.csv` | Aggregated, non-identifiable country/region-level data with preeclampsia-relevant variables |
| DHS codebook | `.md` | Variable definitions, units, and source notes |
| DHS extraction script | `.py` / `.R` | Reproducible script used to create the derived dataset (for transparency) |
| Country context table | `.csv` | Country-level health-system indicators |
