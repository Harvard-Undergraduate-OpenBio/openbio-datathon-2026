# OpenBio 2026 Datathon

**Maternal–Fetal Cell Communication in Preeclampsia**

Welcome to the Harvard Undergraduate OpenBio 2026 Datathon repository. This repository is the participant-facing source of truth for the datathon, including challenge descriptions, data catalogs, glossaries, starter notebooks, and submission templates.

## Quick Links

- [Challenge Overview](docs/challenge-overview.md)
- [Track 1: Computational Biology](docs/track-1-computational-biology/overview.md)
- [Track 2: Global Health](docs/track-2-global-health/overview.md)
- [Data Catalog (Track 1)](docs/track-1-computational-biology/data-catalog.md)
- [Data Catalog (Track 2)](docs/track-2-global-health/data-catalog.md)
- [Cell & Tissue Glossary](docs/track-1-computational-biology/cell-type-glossary.md)
- [Submission Rubric](docs/submission-rubric.md)
- [FAQ](docs/faq.md)

## Tracks

### Track 1 — Computational Biology

Teams investigate which ligand–receptor communication programs between fetal trophoblast and maternal decidual/immune cells are altered in preeclampsia, using publicly available single-cell RNA-seq datasets.

### Track 2 — Global Health

Teams identify distinct health-system contexts in which preeclampsia morbidity occurs and determine which interventions best fit each context, using DHS Program data and related health-system resources.

## Repository Structure

```
openbio-datathon-2026/
├── README.md
├── LICENSE
├── CODE_OF_CONDUCT.md
├── CONTRIBUTING.md
├── CITATION.cff
├── .gitignore
├── docs/                         # Challenge documentation and glossaries
│   ├── track-1-computational-biology/
│   └── track-2-global-health/
├── data/                          # Manifests, checksums, and toy subsets (NOT raw data)
├── notebooks/                     # Starter notebooks for each track
├── src/                           # Shared Python utilities
├── environment/                   # Conda/pip/renv lockfiles
├── templates/                     # Submission and proposal templates
└── submissions/                   # Team submission area
```

## Important Notes

- **This repository does not host large raw datasets.** It contains documentation, download scripts, small toy subsets, checksums, and starter code.
- **DHS microdata is never stored in this repository.** Only derived/aggregated datasets, codebooks, and extraction scripts are distributed.
- **HCA data is governed by the HCA Data Release Policy and CC BY 4.0.** Do not assume unrestricted redistribution of repackaged copies.

## License

This repository's documentation and code are licensed under [MIT](LICENSE). Dataset-specific licenses are documented in each dataset's entry in the [data catalog](docs/track-1-computational-biology/data-catalog.md).

## Contact

- OpenBio: exec@harvardopenbio.org
- Website: https://www.openbiolab.org/
