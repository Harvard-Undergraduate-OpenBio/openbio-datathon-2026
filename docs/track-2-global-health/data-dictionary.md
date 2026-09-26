# Track 2: Data Dictionary

## DHS-Derived Variables

| Field | Type | Description |
|---|---|---|
| `country` | string | Country name |
| `region` | string | Sub-national region |
| `year` | int | Survey year |
| `urban_rural` | string | `urban` or `rural` |
| `anc_visits` | float | Average number of antenatal care visits |
| `anc_facility_delivery` | float | Proportion of deliveries in health facilities |
| `bp_screened` | float | Proportion of pregnant women with blood pressure screening |
| `magnesium_sulfate_available` | bool | Whether MgSO4 is available at facility level |
| `referral_time_hours` | float | Average referral time to facility (hours) |
| `maternal_mortality_ratio` | float | Maternal mortality ratio (per 100,000 live births) |
| `preeclampsia_prevalence` | float | Estimated PE prevalence (if available) |

## Provenance

For each field, indicate whether the value is:
- **DHS-derived:** Aggregated from DHS microdata
- **WHO-reported:** From WHO databases or reports
- **World Bank:** From World Bank Open Data
- **OpenBio-estimated:** Modeled or estimated by OpenBio (state method)

## Important Rule

Do not fabricate or infer missing variables. If a field is unknown for a country/region, mark it as `unknown`.
