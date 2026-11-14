# FAQ

## General

**Who can participate?**
The datathon is open to undergraduate and graduate students at Harvard and affiliated institutions. Teams of three is ideal. Teams of two and four are acceptable.

**Do I need prior bioinformatics experience?**
No. Each track guide ([Track 1](../track-01/README.md), [Track 2](../track-02/README.md)) explains the biology and statistics as you go, and the notebooks do the coding mechanics. Some Python experience helps. If you are new to coding, expect setup to take patience. Start early and ask on [Slack](https://join.slack.com/t/openbiodatathon/shared_invite/zt-4fwud5ffn-9CAX0OqyjtwbE0Hlx5QV1A) when you get stuck.

**Where do I ask for help?**
On [Slack](https://join.slack.com/t/openbiodatathon/shared_invite/zt-4fwud5ffn-9CAX0OqyjtwbE0Hlx5QV1A). Mentors and organizers answer there during the event. For anything before or after the event, email openbiolaboratory@gmail.com.

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
The format is the same for both tracks: reproducible code with a README, a recorded presentation of five minutes or less, a science communication article that follows the [article guide](article-guide.md) and one headline visual. The article needs at least four graphs. Each track adds its own working documents: an analysis plan and hypothesis card for Track 1, a cleaning log for Track 2. See [Track 1: Submit](../track-01/4-submit.md) or [Track 2: Submit](../track-02/4-submit.md).

**How and when do we submit?**
Before Sunday, November 15 at 6:00 PM EST, either through [Devpost](https://openbio-datathon.devpost.com/) or with a pull request to the `submissions/` folder. See [How to Submit](../submissions/README.md).

**Where do we put the video?**
Upload it to YouTube as an unlisted video and paste the link into your README. Nobody has to store or send the file. See the [upload steps](../submissions/README.md#upload-your-video).

**How are submissions judged?**
See the [rubric](rubric.md). Each track has its own criteria.
