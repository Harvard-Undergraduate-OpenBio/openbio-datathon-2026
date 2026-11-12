# Step 1: Setup

[![Back](https://img.shields.io/badge/Back-Track_Overview-13deba?style=flat-square)](README.md)
[![Next](https://img.shields.io/badge/Next-2_The_Data-0fe995?style=flat-square)](2-the-data.md)

By the end of this page you will have the data on your computer and a notebook that opens without errors. Pick one of the two options below. If you have never set up Python before, use Option A.

## Option A: Google Colab (no installation)

1. Open [Google Colab](https://colab.research.google.com) and sign in with a Google account.
2. Choose **File > Open notebook > GitHub**, paste `Harvard-Undergraduate-OpenBio/openbio-datathon-2026` and open `track-01/notebooks/track01_workflow.ipynb`.
3. Run the first code cell. On Colab it downloads the repository and installs the one extra package the workflow needs.

Colab resets when you close it. Download any results or figures you want to keep.

## Option B: Your Own Computer

### Python

1. Install [Miniconda](https://docs.conda.io/en/latest/miniconda.html) if you do not have conda.
2. In a terminal, run:

   ```bash
   git clone https://github.com/Harvard-Undergraduate-OpenBio/openbio-datathon-2026.git
   cd openbio-datathon-2026
   conda env create -f environment/environment.yml
   conda activate openbio-datathon-2026
   jupyter lab
   ```

3. In Jupyter, open `track-01/notebooks/track01_workflow.ipynb`.

No conda? Run `pip install -r environment/requirements.txt` inside a virtual environment instead.

### R

1. Install [R](https://cran.r-project.org) and [RStudio](https://posit.co/download/rstudio-desktop/).
2. Clone the repository as above, then in R run `source("environment/install_r_packages.R")`.
3. Open `track-01/notebooks/track01_workflow.Rmd` in RStudio.

## Get the Data

The data package is in [`track-01/data`](data), so cloning the repository already downloads it. At release a versioned ZIP will also be attached to the repository's Releases page.

Files marked Pending in the [data guide](2-the-data.md) are empty until release day.

## Check the Download

Each file has a fingerprint (a SHA-256 checksum) that you must run on your downloaded copy to ensure that no bytes were changed whilst downloading. From `track-01/data`, run:

```bash
sha256sum -c provenance/checksums.sha256       # Linux or Windows WSL
shasum -a 256 -c provenance/checksums.sha256   # macOS
```

Every line should end in `OK`. If not, download again or ask an organizer. The workflow notebook also checks the files for you, so you can skip this step on Colab.

## You Are Ready When

- The workflow notebook opens.
- The first two code cells run without errors and print the size of each data file.

Stuck? Ask a mentor or email exec@harvardopenbio.org. Setup problems are the most common issue and quick to fix.
