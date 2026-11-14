# Article Guide

[![Track 1 Submit](https://img.shields.io/badge/Track_1-4_Submit-0fe995?style=flat-square)](../track-01/4-submit.md)
[![Track 2 Submit](https://img.shields.io/badge/Track_2-4_Submit-13deba?style=flat-square)](../track-02/4-submit.md)

How to write a data article that a general reader can follow and trust.

> **Source:** these guidelines come from the [Harvard Undergraduate Data Project (HUDP)](https://www.hudp.org/). They are adapted from the HUDP Article Guide (2025-2026), which builds on HUDP's public [Good Practices](https://docs.hodp.org/docs/good-practices/) page. HUDP's materials also use the initials HODP. The advice is HUDP's. The examples are rewritten for this datathon, and the parts about HUDP's own bootcamp and website are left out.

## Who This Is For

| Track | How to use this guide |
|---|---|
| Track 1 | Required. Your [science communication article](../track-01/4-submit.md#3-science-communication-article) follows this guide |
| Track 2 | Required. Your [science communication article](../track-02/4-submit.md#3-science-communication-article) follows this guide |

## What the Article Is For

HUDP's core purpose is to make data and its insights accessible. For your article that means:

- Explain where your data is from, what it contains and how you drew your insights from it.
- Use everyday terms where you can, explain specialized concepts and do not assume much prior knowledge.
- Back your insights with rigorous analysis, so readers can trust the work and check it.
- Tell a story.

HUDP's first piece of advice is to work on a question that means something to you. You will not want to dig into the details of your data if you do not care about the question.

## Outline

HUDP articles typically follow this format. It is a loose outline, so adjust it to fit your story.

| # | Section | What goes in it |
|---|---|---|
| 1 | Introduction | The question you set out to answer and why it matters to the reader. Tell them what they are in for |
| 2 | The data and your methods | What your data is and where you got it. Keep it to a short paragraph. If your methods limit how far your insights can be trusted, say so here. Move extra detail to an appendix |
| 3 | Insights, data and discussion | The bulk of the article. Answer your question with results shown both in numbers and in graphs |
| 4 | Unanswered questions | What the data could not answer, or where your results are inconclusive. This can also sit inside section 3 |
| 5 | Conclusions, limitations and next steps | What the data showed, where that leaves your original question and what you would do next |
| 6 | Links to data and code | A link to your repository. Make sure privacy is protected |

In the insights section:

- Put each graph in the text where you discuss it.
- Explain what each result means. A number or a test result on its own is not enough.
- Say briefly how you got a result if it took more than a count or an average.
- Point out unexpected results and key trends.
- You may suggest a reason behind a result. Keep it tied to the data and say when you are speculating.

For published examples, read some of [HUDP's projects](https://www.hudp.org/projects/).

## Know Your Data First

You are responsible for understanding your data, handling it properly and reporting your findings honestly.

- **Check where the data comes from.** HUDP's example is a news story that counted kidnappings from a database of news reports. The database counted mentions in the news, not separate events, so the totals were far too high.
- **Ask who is in the data and who is missing.** Data points often stand for real people. How were they collected, and what biases could that carry? The [data biography](https://gijn.org/2017/03/27/data-biographies-getting-to-know-your-data/) framework walks through these questions.
- **"Interview" the data** for the who, what, when, where, why and how.
- **Keep the original columns when you clean.** Add new columns instead of overwriting.
- **Choose between the mean and the median.** Use the median when there are outliers and the mean when the values are roughly normally distributed. If the two differ a lot, look closer, because that gap could be the story.
- **Look for patterns and outliers that tell a story.**

Before you start, ask what you want readers to take away. You do not need to know the answer yet. That is what the analysis is for.

## Logic

- Each idea should follow from the one before it.
- Back every claim with data, either linked or shown in a graph.
- Give your data context by explaining where it came from. Always answer "so what?"
- Caveat your conclusions. Explain the limits of your analysis and state future directions.
- Leave out opinions and proposed solutions that go beyond your data. You can speculate about a specific trend if you say it is speculation.

## Writing Style

- Aim for a tone that is conversational and friendly yet polished.
- Discuss your subject in a straightforward, accessible way. Do not assume readers share your background.
- Avoid memes, gifs and snark.
- Keep your analysis to a high technical standard, and explain every term and statistical concept in the text.
- Be consistent. Whatever convention you pick for a term or for capitalization, use it throughout. HUDP suggests the [AP style summary](https://www.bu.edu/com/files/2021/04/WC_apstyle.pdf) when you are unsure.
- Use bold and italics sparingly.

## Graphs

**How many:** at least four. Most HUDP articles have 5 to 10. HUDP strongly prefers graphs and charts over tables and lists.

**Every graph needs:**

- A specific, concise, capitalized title
- Axis labels written the same way
- A legend only when there is more than one data series
- A caption
- A source in parentheses in the caption, if the image is not your own

HUDP also encourages [alt text](https://accessibility.huit.harvard.edu/describe-content-images), a short description for readers who cannot see the image.

**Pick the chart type on purpose:**

| Chart | Best for |
|---|---|
| Line chart | Trends over time in numerical data |
| Bar chart | Categories |
| Horizontal bar chart | Sorted data |

Do not give every bar a different color. The size of the bar carries the message.

**Make it quick to read:**

- A reader should get the main point within a second.
- Avoid clutter. Aim for five or fewer categories in each graph.
- Use large images at high resolution.
- Put each graph after the text it belongs to, not beside it.

## Numbers in the Text

- Be only as precise as the point needs. "Nearly 6 in 10" often reads better than "59.7%".
- Every number in the article should be an important one. Apply the "so what?" test.
- Give each number a clear, descriptive unit, such as "about 1 in every 6 women in our sample".

## Title, Pull Quotes and Credits

- **Title and subtitle.** The title is short and engaging and captures the gist. The subtitle adds detail.
- **Authors.** List all main authors.
- **Pull quotes (optional).** Choose 3 to 5 sentences that hold insights you do not want a reader to miss, and put them in bold. Keep them concise.
- **Links.** Hyperlink every outside source in the text where you use it.
- **Data and code.** Link the repository that holds your data and analysis code. Do not include personally identifiable data.
- **Acknowledgements.** Thank anyone who supported your project.

## Checklist

- [ ] Title, subtitle and authors
- [ ] The six outline sections, with data and methods kept to a short paragraph
- [ ] At least four graphs, each with a title, axis labels and a caption
- [ ] Every term and statistical concept explained
- [ ] Every claim backed by data, with conclusions caveated
- [ ] Limitations and unanswered questions stated
- [ ] Outside sources hyperlinked and borrowed images credited
- [ ] Link to your repository
- [ ] Acknowledgements

## Credit

Harvard Undergraduate Data Project (HUDP). HUDP Article Guide (2025-2026). https://www.hudp.org/

Related public material: Hu A, Srinivasan S and Kwan M. Good Practices. HODP Docs. https://docs.hodp.org/docs/good-practices/
