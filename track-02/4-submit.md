# Step 4: Submit

[![Back](https://img.shields.io/badge/Back-3_Workflow-13deba?style=flat-square)](3-workflow.md)
[![Rubric](https://img.shields.io/badge/Docs-Judging_Rubric-0fe995?style=flat-square)](../docs/rubric.md)

## The Four Deliverables

| # | Deliverable | Where it lives |
|---|---|---|
| 1 | Reproducible code in your team GitHub repository, with a README, clear markdown explanations and a cleaning log | `track-02/team/` |
| 2 | A recorded presentation of five minutes or less | Link in your team README |
| 3 | A written science communication article about your work, following the [HUDP article guide](../docs/article-guide.md) | `track-02/team/docs/article.md` |
| 4 | One headline visual showing your single most important finding to a non-specialist, used in both the video and the article | `track-02/team/figures/headline.png` |

Every deliverable must include a short statement that your work is not medical advice or a diagnostic tool.

## 1. Code: Your Team Repository

Judges will rerun your notebooks top to bottom from the provided files. Your [`team/`](team) folder already has the layout they expect:

| Item | Purpose |
|---|---|
| `README.md` | Team name and members, research question, how to run the code and a list of files |
| `notebooks/` | Analysis notebooks in the order they run (`01_cleaning`, `02_analysis`) |
| `src/` (optional) | Reusable functions, such as cleaning helpers |
| `figures/` | Exported graphs, including your headline visual |
| `docs/cleaning_log.md` | Each cleaning rule applied and the number of records affected |
| `docs/article.md` | Your science communication article |
| `requirements.txt` | Python packages and versions needed to run the notebooks |
| `.gitignore` | Keeps raw data, credentials and temporary files out of the repository |

Before you submit:

- Restart the notebooks and run all cells from the top. Fix anything that breaks.
- Check that `docs/cleaning_log.md` lists every rule with a count.
- Fill in every section of the [team README](team/README.md).

## 2. Recorded Presentation

One recording, five minutes at most. Every team member must appear or speak at least once. Use any screen recorder (Zoom, Google Meet, Loom or your laptop's built-in recorder). An outline is in [`team/docs/presentation-outline.md`](team/docs/presentation-outline.md).

| Section | Time | Cover |
|---|---|---|
| Introduction | 0:00 to 0:45 | Your question, why it matters for women's cardiovascular health, which datasets you used |
| Methodology | 0:45 to 1:45 | Cleaning decisions, variables you used or created and how you encoded them, your method and why, how you checked your work |
| Results | 1:45 to 3:45 | Graphs, including a regression graph where it fits. Sample size, key summary statistics, effect sizes with confidence intervals and model metrics |
| Discussion | 3:45 to 5:00 | What your findings mean for women's cardiovascular health, your limitations and what you would improve with more time or resources |

**Slide tips:** put names, dataset sources and the repository link on a final slide or in the video description. Check the audio, and make sure graphs are readable at normal video resolution.

## 3. Science Communication Article

Write it in [`team/docs/article.md`](team/docs/article.md) and follow the [article guide](../docs/article-guide.md). The guidelines come from the [Harvard Undergraduate Data Project (HUDP)](https://www.hudp.org/). The template already has the guide's outline.

The main requirements:

| What | Requirement |
|---|---|
| Structure | Introduction, data and methods, insights, unanswered questions, conclusions with limitations and next steps, links to data and code |
| Data and methods | A short paragraph at most. Say where the data came from and anything that limits your insights, such as synthetic data |
| Graphs | At least four, each with a title, axis labels and a caption. Your headline visual counts as one |
| Language | Written for a general reader, with every term and statistical concept explained |
| Claims | Each one backed by data, with limitations stated |
| Title | A short title and a subtitle that adds detail |
| Credits | Authors, links to outside sources, a link to your team repository and acknowledgements |

Where the four graphs come from: `02_analysis.ipynb` saves your headline visual and your model graph (`forest_plot.png` or `regression_line.png`) to `team/figures/`. To save any other graph from a notebook, add this line just before its `plt.show()`:

```python
plt.savefig(FIGURES / "my_graph.png", dpi=200, bbox_inches="tight")
```

Add a graph to the article with `![Short description of the graph](../figures/my_graph.png)`.

## 4. Headline Visual

See [workflow step 7](3-workflow.md#7-make-a-headline-visual). The same image goes in the video and the article.

## How to Submit

Share your private team repository with the organizers and submit your video link. Exact submission steps and the deadline will be announced.
