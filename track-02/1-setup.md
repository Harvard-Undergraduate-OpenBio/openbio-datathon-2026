# Step 1: Setup

[![Back](https://img.shields.io/badge/Back-Track_Overview-13deba?style=flat-square)](README.md)
[![Next](https://img.shields.io/badge/Next-2_The_Data-0fe995?style=flat-square)](2-the-data.md)

By the end of this page your team will have a shared GitHub repository and a notebook that loads the data. Track 2 uses Python. We recommend Google Colab so everyone works in the same environment. The instructional video walks through these steps (link to be added).

## Part A: Create Your Team Repository

Each team keeps its code in its own small GitHub repository, copied from this one. Everyone gets the same folder structure, teammates can work without overwriting each other and judges can rerun your analysis.

**Before you start:** every team member needs a free [GitHub](https://github.com) account and [Git](https://git-scm.com) installed. One person, the team lead, does Steps 1 to 4 and shares the result.

**Step 1. Clone the main repository.**

```bash
git clone https://github.com/Harvard-Undergraduate-OpenBio/openbio-datathon-2026.git cvd-women-<team-name>
cd cvd-women-<team-name>
```

**Step 2. Create your team's empty repository.** On github.com, click **New repository**. Name it `cvd-women-<team-name>` and choose **Private** (you will share it with organizers at submission). Do not add a README, .gitignore or license, because the cloned files already include them.

**Step 3. Point your clone at the team repository.** Keep the main repository as `upstream` so you can pull organizer updates later, and make your new repository `origin`.

```bash
git remote rename origin upstream
git remote add origin https://github.com/<your-username>/cvd-women-<team-name>.git
git push -u origin main
```

To pull organizer updates later: `git pull upstream main`.

**Step 4. Add your teammates.** On GitHub, open the team repository, go to **Settings > Collaborators** and add each teammate by username. Teammates then clone the team repository, not the main one.

Your team's work goes in [`track-02/team/`](team). That folder already has the layout judges expect.

## Part B: Open the Notebooks

### Option A: Google Colab (recommended)

1. Open [Google Colab](https://colab.research.google.com) and choose **File > Open notebook > GitHub**.
2. Sign in to GitHub when asked, tick **Include private repos**, pick your team repository and open `track-02/team/notebooks/01_cleaning.ipynb`.
3. Run the first code cell. It finds the data automatically.

To save your edits back to the team repository, use **File > Save a copy in GitHub**.

### Option B: Your Own Computer

```bash
conda env create -f environment/environment.yml
conda activate openbio-datathon-2026
jupyter lab
```

Then open `track-02/team/notebooks/01_cleaning.ipynb`. No conda? Run `pip install -r track-02/team/requirements.txt`.

## Part C: Loading the Data by Hand

The notebooks load the files for you. If you start a fresh notebook, two ways work on Colab.

**Upload directly.** Click the folder icon in the left sidebar, then the upload icon, and choose the CSV. Files uploaded this way disappear when the session ends.

```python
import pandas as pd
df1 = pd.read_csv("cardiovascular_dataset_OpenBio_Final.csv")
df2 = pd.read_csv("heart_attack_prediction_dataset_OpenBio_Final.csv")
display(df1)
display(df2)
```

**Mount Google Drive.** Upload the files to a `datathon` folder in your Drive, then run the code below and approve the permissions prompt.

```python
from google.colab import drive
drive.mount('/content/drive')
df1 = pd.read_csv('/content/drive/MyDrive/datathon/cardiovascular_dataset_OpenBio_Final.csv')
```

**Tips:**

- If the cardiovascular CSV loads as a single column, the file is semicolon-separated. Use `pd.read_csv(path, sep=';')`.
- Load Tables S1 and S2 with `pd.read_excel` or `pd.read_csv` depending on the format, and inspect the header rows before trusting the column names.

## You Are Ready When

- Every teammate can open the team repository.
- The first two code cells of `01_cleaning.ipynb` run and print the size of each dataset.

Stuck? Ask a mentor or email exec@harvardopenbio.org.
