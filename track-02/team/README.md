# [Team Name]: [Project Title]

OpenBio 2026 Datathon, Track 2: Cardiovascular Health in Women

> This project is a student data analysis. It is not medical advice, a diagnostic tool or clinical guidance.

## Team

| Name | Role |
|---|---|
| | |

## Research Question

[One sentence. Example format: "Among women in Dataset 1, is X associated with Y after accounting for age?"]

## Datasets Used

- [ ] Dataset 1: Cardiovascular Disease Dataset
- [ ] Dataset 2: Heart Attack Risk Prediction Dataset (synthetic)
- [ ] Dataset 3: Global CVD in Women, Tables S1 and S2

## How to Run

1. The raw files are already in `track-02/data/` (see the [data guide](../data/README.md)). On Colab the first notebook cell downloads them.
2. Install packages: `pip install -r requirements.txt`
3. Run `notebooks/01_cleaning.ipynb`, then `notebooks/02_analysis.ipynb`, top to bottom.

## Files

| Path | Contents |
|---|---|
| `notebooks/01_cleaning.ipynb` | Loads and cleans the data, writes the cleaning log |
| `notebooks/02_analysis.ipynb` | Summary statistics, models, checks and the headline visual |
| `src/` | Helper functions (optional) |
| `figures/` | Exported graphs, including `headline.png` |
| `docs/cleaning_log.md` | Each cleaning rule and the records affected |
| `docs/article.md` | Science communication article, following the [HUDP article guide](../../docs/article-guide.md) |
| `requirements.txt` | Python packages |

## Key Findings

[Two or three sentences with effect sizes and confidence intervals.]

## Limitations

[Synthetic data, ecological fallacy, binary sex variable, anything else that limits your claims.]

## Presentation

Video link: [add your unlisted YouTube link]
