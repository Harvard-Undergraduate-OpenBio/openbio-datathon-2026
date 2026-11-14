# Step 4: Submit

[![Back](https://img.shields.io/badge/Back-3_Workflow-13deba?style=flat-square)](3-workflow.md)
[![Rubric](https://img.shields.io/badge/Docs-Judging_Rubric-0fe995?style=flat-square)](../docs/rubric.md)
[![How to Submit](https://img.shields.io/badge/Docs-How_to_Submit-13deba?style=flat-square)](../submissions/README.md)

Both tracks hand in the same four deliverables. This page covers what each one needs for Track 1.

**Deadline: Sunday, November 15 at 6:00 PM EST.**

## Write Your Hypothesis

A hypothesis is a testable explanation for what you found. Fill in the [hypothesis card](templates/hypothesis-card.md). A strong one:

- Starts from a specific result ("these genes are higher in cases and the browser places most of them in cell type Y")
- Proposes a mechanism and names at least one other explanation, such as gestational age or cell mix
- Suggests a concrete experiment or analysis that could prove it wrong
- Uses careful language: "suggests" or "consistent with," not "proves"

The [limitations page](reference/limitations.md) lists what this kind of data can and cannot show.

## What to Hand In

| # | Deliverable | Where it lives |
|---|---|---|
| 1 | Reproducible code that runs top to bottom, with a README | `README.md` and `notebooks/` |
| 2 | A recorded presentation of five minutes or less | Unlisted YouTube video, linked in your README |
| 3 | A written science communication article about your work, following the [HUDP article guide](../docs/article-guide.md), with at least four graphs | `docs/article.md` and `figures/` |
| 4 | One headline visual showing your single most important finding to a non-specialist, used in both the video and the article | `figures/headline.png` |

Track 1 also asks for two working documents: the [analysis plan](templates/analysis-plan.md) you filled in during Step 3 and one [hypothesis card](templates/hypothesis-card.md) per team.

## 1. Code: Your Submission Folder

Judges will rerun your notebook top to bottom from the provided files. Make a folder named after your team and fill it from the [templates](templates):

| Item | Template | Purpose |
|---|---|---|
| `README.md` | [team-readme.md](templates/team-readme.md) | Team name and members, research question, video link and how to run the code |
| `notebooks/` | Your copy of the [workflow notebook](notebooks/track01_workflow.ipynb) | The analysis itself. An R Markdown file or a script also works |
| `figures/` | | Exported graphs as PNG, including your headline visual |
| `docs/article.md` | [article.md](templates/article.md) | Your science communication article |
| `docs/analysis-plan.md` | [analysis-plan.md](templates/analysis-plan.md) | The plan you filled in during Step 3 |
| `docs/hypothesis-card.md` | [hypothesis-card.md](templates/hypothesis-card.md) | One per team |

Before you submit:

- Restart the notebook and run all cells from the top. Fix anything that breaks.
- On Colab, save the notebook with **File > Download > Download .ipynb**. Your graphs are in the file panel on the left, under `openbio-datathon-2026/track-01/notebooks/results`. Right-click each one to download it.
- Fill in every section of the README and cite every dataset you used ([citations](reference/citations.md)).

## 2. Recorded Presentation

One recording, five minutes at most. Every team member must appear or speak at least once. Use any screen recorder (Zoom, Google Meet, Loom or your laptop's built-in recorder). An outline is in [`templates/presentation-outline.md`](templates/presentation-outline.md).

| Section | Time | Cover |
|---|---|---|
| Introduction | 0:00 to 0:45 | Your question, why it matters for preeclampsia, which data you used |
| Methodology | 0:45 to 1:45 | The comparison you chose and why, your thresholds, how you handled confounders such as gestational age |
| Results | 1:45 to 3:45 | Graphs, including your PCA and volcano plots where they fit. Samples per group, how many genes passed, what the gene browser showed |
| Discussion | 3:45 to 5:00 | Your hypothesis, your limitations and a follow-up experiment or analysis that could test it |

**Upload:** put the recording on YouTube as an unlisted video and paste the link into your README. The [upload steps](../submissions/README.md#upload-your-video) take a few minutes.

**Slide tips:** put names, dataset sources and the repository link on a final slide or in the video description. Check the audio, and make sure graphs are readable at normal video resolution.

## 3. Science Communication Article

Write it from the [article template](templates/article.md) and follow the [article guide](../docs/article-guide.md). The guidelines come from the [Harvard Undergraduate Data Project (HUDP)](https://www.hudp.org/). The template already has the guide's outline.

The main requirements:

| What | Requirement |
|---|---|
| Structure | Introduction, data and methods, insights, unanswered questions, conclusions with limitations and next steps, links to data and code |
| Data and methods | A short paragraph at most. Say where the data came from and anything that limits your insights, such as the small number of samples |
| Graphs | At least four, each with a title, axis labels and a caption. Your headline visual counts as one |
| Language | Written for a general reader, with every term and statistical concept explained |
| Claims | Each one backed by data, with limitations stated |
| Title | A short title and a subtitle that adds detail |
| Credits | Authors, links to outside sources, a link to your repository and acknowledgements |

Where the four graphs come from: the notebook draws a PCA plot and a volcano plot, and it saves the volcano plot to `results/volcano.png`. A PCA plot colored by a second variable, such as gestational age, makes a third graph. To save a PCA plot, add this line just before the `plt.show()` in the PCA cell and rerun it:

```python
plt.savefig(RESULTS_DIR / "pca.png", dpi=300, bbox_inches="tight")
```

Change the file name each time so one graph does not overwrite another. For a fourth graph, show one gene from your results in every sample. Paste this into a new cell at the end of the notebook, after you have run the test and set your thresholds:

```python
gene = hits.index[0]   # or a gene name from your results, in quotes
log_cpm = np.log2(counts.div(counts.sum(axis=0), axis=1) * 1e6 + 1)
fig, ax = plt.subplots(figsize=(5, 4))
for position, level in enumerate([CONTROL, CASE]):
    samples = comp_meta.index[comp_meta[GROUP_COLUMN] == level]
    ax.scatter([position] * len(samples), log_cpm.loc[gene, samples])
ax.set_xticks([0, 1])
ax.set_xticklabels([CONTROL, CASE])
ax.set_xlim(-0.5, 1.5)
ax.set_ylabel("Gene activity (log2 counts per million)")
ax.set_title(f"{gene} in each sample")
plt.savefig(RESULTS_DIR / "top_gene.png", dpi=300, bbox_inches="tight")
plt.show()
```

Copy the graphs you use into your `figures/` folder. Add a graph to the article with `![Short description of the graph](../figures/my_graph.png)`.

## 4. Headline Visual

One graph that shows your single most important finding to a non-specialist. Save it as `figures/headline.png` and use the same image in the video and the article. A good headline visual:

- Has a title that states the finding in plain words
- Labels axes in everyday language, with units
- Shows every sample or the spread of the data, so readers see more than an average
- Is readable at normal video resolution

## How to Submit

Submit before **Sunday, November 15 at 6:00 PM EST**, in one of two ways:

- **Devpost:** put your folder in a GitHub repository and add its link and your video link to a project on [Devpost](https://openbio-datathon.devpost.com/).
- **Pull request:** add your folder to `submissions/your-team-name/` in a fork of this repository and open a pull request.

The [submission instructions](../submissions/README.md#how-to-submit) walk through both.

## How You Are Judged

See the [rubric](../docs/rubric.md). Clear reasoning and honest limits score better than a long list of significant genes.
