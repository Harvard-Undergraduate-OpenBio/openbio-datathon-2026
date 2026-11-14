# Submissions

[![Track 1 Submit](https://img.shields.io/badge/Track_1-4_Submit-0fe995?style=flat-square)](../track-01/4-submit.md)
[![Track 2 Submit](https://img.shields.io/badge/Track_2-4_Submit-13deba?style=flat-square)](../track-02/4-submit.md)
[![Rubric](https://img.shields.io/badge/Docs-Judging_Rubric-0fe995?style=flat-square)](../docs/rubric.md)

Both tracks hand in the same four deliverables and submit the same way.

**Deadline: Sunday, November 15 at 6:00 PM EST.**

## What to Hand In

| # | Deliverable | Where it lives |
|---|---|---|
| 1 | Reproducible code that runs top to bottom, with a README | `README.md` and `notebooks/` |
| 2 | A recorded presentation of five minutes or less | Unlisted YouTube video, linked in your README |
| 3 | A written science communication article about your work, following the [HUDP article guide](../docs/article-guide.md), with at least four graphs | `docs/article.md` and `figures/` |
| 4 | One headline visual showing your single most important finding to a non-specialist, used in both the video and the article | `figures/headline.png` |

Each track also asks for its own working documents: the analysis plan and hypothesis card for Track 1, the cleaning log for Track 2.

What each deliverable must contain is on your track's submit page ([Track 1](../track-01/4-submit.md), [Track 2](../track-02/4-submit.md)).

## Your Submission Folder

Every team hands in one folder with this layout:

```
your-team-name/
├── README.md                 Team, track, research question, video link, how to run
├── notebooks/                Analysis notebooks or scripts, in the order they run
├── figures/                  At least four graphs, including headline.png
└── docs/
    ├── article.md            Science communication article
    ├── analysis-plan.md      Track 1 only
    ├── hypothesis-card.md    Track 1 only
    └── cleaning_log.md       Track 2 only
```

- **Track 1:** build the folder from the templates in [`track-01/templates/`](../track-01/templates).
- **Track 2:** you already have it. It is the [`track-02/team/`](../track-02/team) folder in your team repository.

## Upload Your Video

Upload the recording to YouTube as an **unlisted** video, so nobody on your team has to store or send a large file. Unlisted means only people with the link can watch it.

1. Sign in to [YouTube Studio](https://studio.youtube.com) and click **Create**, then **Upload videos**.
2. Choose your file. For the audience question, pick **No, it's not made for kids**.
3. On the **Visibility** step, choose **Unlisted**. Judges cannot open a Private video.
4. Save, copy the video link and paste it into your README.

YouTube's [upload guide](https://support.google.com/youtube/answer/57407) shows each step.

## How to Submit

Choose one of the two options, whichever your team finds easier.

### Option 1: Devpost

1. Put your submission folder in a GitHub repository. Track 2 teams already have one. Track 1 teams can create a new repository on github.com, then drag the folder's contents onto **Add file > Upload files**.
2. Make sure judges can open the repository. The simplest way is to make it public when you are done (**Settings > General > Change visibility**). To keep it private, ask on [Slack](https://join.slack.com/t/openbiodatathon/shared_invite/zt-4fwud5ffn-9CAX0OqyjtwbE0Hlx5QV1A) which organizer accounts to add as collaborators.
3. Join the datathon on [Devpost](https://openbio-datathon.devpost.com/) and start a project.
4. In the project description, name your track and summarize your finding in a few sentences. Add your repository link, your YouTube link and your headline visual.
5. Submit the project before the deadline.

### Option 2: Pull Request

1. [Fork this repository](https://docs.github.com/en/pull-requests/collaborating-with-pull-requests/working-with-forks/fork-a-repo).
2. In your fork, add your folder as `submissions/your-team-name/`. On github.com, open the `submissions` folder, choose **Add file > Upload files** and drag your team folder onto the page.
3. Open a pull request to this repository titled `Submission: [Team Name], Track [1 or 2]` before the deadline.

Pull requests to this repository are public, so anyone can read your submission.

## Before You Submit

- [ ] The notebooks run top to bottom after a restart.
- [ ] The README has your team, track, research question and video link.
- [ ] The video is five minutes or less and its link opens in a private browser window.
- [ ] The article has at least four graphs, each with a title, axis labels and a caption.
- [ ] Every dataset is cited and your limitations are stated.

Questions? Ask on [Slack](https://join.slack.com/t/openbiodatathon/shared_invite/zt-4fwud5ffn-9CAX0OqyjtwbE0Hlx5QV1A).
