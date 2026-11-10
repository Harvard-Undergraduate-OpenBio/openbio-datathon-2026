# FAQ

## General

**Who can participate?**
The datathon is open to undergraduate students at Harvard and affiliated institutions. Teams of two to four are recommended.

**Do I need prior bioinformatics experience?**
No. Each track guide ([Track 1](../track-01/README.md), [Track 2](../track-02/README.md)) explains the biology and statistics as you go, and the notebooks do the coding mechanics. Some Python experience helps.

**What should I bring?**
A laptop. Google Colab works in the browser with no installation. See Setup for [Track 1](../track-01/1-setup.md) or [Track 2](../track-02/1-setup.md).

## Track 1

**Do I need to download raw data?**
No. Everything is in the prepared package. See [Setup](../track-01/1-setup.md).

**Which comparison should we run?**
That is your choice. Pick a question from the [starter questions](../track-01/starter-questions.md) and justify your comparison.

**Which methods or tools should we use?**
The [workflow notebook](../track-01/notebooks/track01_workflow.ipynb) uses DESeq2, a standard method for this kind of data. You may use any other method if you document it.

**Is the single-cell extension required?**
No. The bulk core is required for every team. The gene browser is required for at least three genes.

**Can I use additional datasets?**
Yes, if they are public and cited. Start with the resources in the [data catalog](../track-01/reference/data-catalog.md).

## Track 2

**Do we have to use all three datasets?**
No. Use one dataset or combine insights across them. The datasets cannot be joined row by row because they describe different people and different scales.

**Which language should we use?**
Python. The starter notebooks in [`track-02/team/notebooks/`](../track-02/team/notebooks) run on Google Colab.

**Why does Track 2 need a private team repository?**
Judges rerun your code from your repository, and your repository is part of the submission. See [Setup](../track-02/1-setup.md).

**Can we treat Dataset 2 results as real findings?**
No. Dataset 2 is synthetic. Present any model built on it as a methods exercise. See [responsible use](../track-02/reference/limitations.md).

**Which statistical method should we use?**
Logistic or linear regression covers most questions, and the [workflow](../track-02/3-workflow.md) explains when to use each. Other methods are fine if you justify them.

## Submissions

**What format should my submission be?**
Track 1: a reproducible notebook or script, two to four figures, a brief written interpretation and a completed hypothesis card. See [Track 1: Submit](../track-01/4-submit.md).
Track 2: a team repository, a recorded presentation of five minutes or less, a science communication article and one headline visual. See [Track 2: Submit](../track-02/4-submit.md).

**How are submissions judged?**
See the [rubric](rubric.md). Track 2 judging criteria will be announced.
