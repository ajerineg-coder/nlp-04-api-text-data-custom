# API Text Data Analysis

Author: Addie Gemmell

Date: November 2026

## Project Overview

I wanted to explore how text data from an API can be
organized and analyzed to identify patterns. My project
focuses on comment lengths and email domains.

## Phase 4: Technical Modification

I added a derived feature called body_line_breaks to
count the number of line breaks in each post.
This provides another way to analyze text formatting.

## Phase 5: Custom Application

I used the JSONPlaceholder comments API:

https://jsonplaceholder.typicode.com/comments

The original API contained posts with user IDs,
titles, and body text. The comments API contains
post IDs, comment IDs, names, email addresses,
and body text.

## EVTL Process

- Extract: Retrieve comments and save the raw JSON.
- Validate: Check that all required fields exist
  and have the expected data types.
- Transform: Use Polars to organize the data
  and calculate three derived features.
- Load: Save the processed records to a CSV file.

## Derived Features

- comment_length: Number of characters in each comment.
- email_domain: Domain extracted from the email address.
- is_dot_com: Whether the email ends in .com.

## Results

The pipeline successfully processed 500 comments
with eight columns.

| Metric | Result |
| --- | ---: |
| Average comment length | 161.53 |
| Minimum comment length | 78 |
| Maximum comment length | 263 |
| .com domains | 38 |
| Other domains | 462 |

### Email Domain Distribution

```text
.com    | ##                        7.6%
Other   | #######################  92.4%
```

## Interpretation

I found that only 7.6% of the email addresses
ended in .com. Comment lengths also varied
considerably throughout the dataset.

In financial fraud analysis, similar techniques
could help identify patterns in email addresses
and written communications. However, this dataset
contains fictional information, and an email domain
alone is not an indicator of fraud.

## Run the Project

```bash
uv run python -m nlp.pipeline_api_json_phase4
uv run python -m nlp.pipeline_api_json_addie
```

## Project Links

- [GitHub Repository](https://github.com/ajerineg-coder/nlp-04-api-text-data-custom)
- [Custom Pipeline](https://github.com/ajerineg-coder/nlp-04-api-text-data-custom/blob/main/src/nlp/pipeline_api_json_addie.py)
- [Raw JSON](https://github.com/ajerineg-coder/nlp-04-api-text-data-custom/blob/main/data/raw/addie_comments_raw.json)
- [Processed CSV](https://github.com/ajerineg-coder/nlp-04-api-text-data-custom/blob/main/data/processed/addie_comments_processed.csv)

## Project Resources

- [Project Instructions](project-instructions.md)
- [Glossary](glossary.md)
- [Professional Python Guide](https://denisecase.github.io/pro-analytics-02/)
- [Professional Python Project Explainer](https://pup-pack.github.io/professional-python-project-explainer/)
