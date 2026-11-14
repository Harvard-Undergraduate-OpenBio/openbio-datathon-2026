# Step 1: Setup

[![Back](https://img.shields.io/badge/Back-Track_Overview-13deba?style=flat-square)](README.md)
[![Next](https://img.shields.io/badge/Next-2_The_Data-0fe995?style=flat-square)](2-the-data.md)

By the end of this page you will have the data on your computer and a notebook that opens without errors. Pick one of the two options below. If you have never set up Python before, we recommend that you use Option A.

> **New to coding?** Setup takes patience, and it is often the slowest part of the datathon. Go one step at a time. An error message or two is normal, so ask on [Slack](https://join.slack.com/t/openbiodatathon/shared_invite/zt-4fwud5ffn-9CAX0OqyjtwbE0Hlx5QV1A) as soon as you are stuck.

## Option A: Google Colab (no installation)

1. Open [Google Colab](https://colab.research.google.com) and sign in with a Google account.
2. Choose **File > Open notebook > GitHub**, paste `Harvard-Undergraduate-OpenBio/openbio-datathon-2026` and open `track-01/notebooks/track01_workflow.ipynb`.
3. Run the first code cell. On Colab it downloads the repository and installs the one extra package the workflow needs.

NOTE: Colab resets when you close it. Download any results or figures you want to keep.

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

3. In Jupyter, open `track-01/notebooks/track01_workflow.ipynb`. You can open the Jupyter Notebook file with [JupyterLab](https://jupyterlab.readthedocs.io/en/stable/), in your terminal, [VS Code](https://code.visualstudio.com/Download), etc. 

No conda? Run `pip install -r environment/requirements.txt` inside a virtual environment instead.

### R

1. Install [R](https://cran.r-project.org) and [RStudio](https://posit.co/download/rstudio-desktop/).
2. [Clone the repository](https://oxford-ihtm.io/ihtm-handbook/clone-repository-rstudio.html) as above, then in R run `source("environment/install_r_packages.R")`.
3. Open `track-01/notebooks/track01_workflow.Rmd` in RStudio.

## Get the Data

The data package is in [`track-01/data`](data), so cloning the repository already downloads it. On Colab the first notebook cell does this for you.

Not using git? [Download the repository as a ZIP](https://github.com/Harvard-Undergraduate-OpenBio/openbio-datathon-2026/archive/refs/heads/main.zip) and unzip it. Links to each individual file are in the [data package README](data/README.md#how-to-get-the-data).

## Optional: Check the Download

Skip this section on Colab. It is for teams that downloaded the data to their own computer (Option B or the ZIP) and want to confirm that every file arrived complete.

A download can be cut off or damaged without any warning, and a damaged data file causes confusing errors later in the notebook. To rule that out, the data package lists a fingerprint for each file, called a SHA-256 checksum, in [`provenance/checksums.sha256`](data/provenance/checksums.sha256). The command below recomputes the fingerprint of each file on your computer and compares it with that list. Open a terminal in `track-01/data` and run the line for your system:

```bash
sha256sum -c provenance/checksums.sha256       # Linux or Windows WSL
shasum -a 256 -c provenance/checksums.sha256   # macOS
```

Every line should end in `OK`, which means your copy matches the released files exactly. If a line says `FAILED`, download the repository again or ask on [Slack](https://join.slack.com/t/openbiodatathon/shared_invite/zt-4fwud5ffn-9CAX0OqyjtwbE0Hlx5QV1A).

## You Are Ready When

- The workflow notebook opens.
- The first two code cells run without errors and print the size of each data file.

Stuck? Ask on [Slack](https://join.slack.com/t/openbiodatathon/shared_invite/zt-4fwud5ffn-9CAX0OqyjtwbE0Hlx5QV1A). Setup problems are a common issue and may be quick to fix.
