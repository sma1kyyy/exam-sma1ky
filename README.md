# AI Realty Selector

[![CI](https://github.com/sma1kyyy/exam-sma1ky/actions/workflows/ci.yml/badge.svg)](https://github.com/sma1kyyy/exam-sma1ky/actions/workflows/ci.yml)
[![Python](https://img.shields.io/badge/Python-3.10%2B-3776AB?logo=python&logoColor=white)](https://www.python.org/)

A small, testable Python CLI that filters and ranks real-estate records by explicit user constraints.

This repository was prepared as a technical assignment and demonstrates a complete, intentionally simple workflow:

`CSV ingestion → validation/conversion → filtering → ranking → readable CLI output`

## What it demonstrates

- deterministic rule-based logic instead of an unsubstantiated ML claim;
- separation between data loading, selection logic and CLI interaction;
- automated tests executed in GitHub Actions;
- reproducible local setup and explicit limitations;
- clear communication of what is production-ready and what is not.

## Features

- load records from CSV;
- filter by city, maximum budget and minimum area;
- rank matches by distance to requested constraints;
- return up to N results;
- run interactively from the command line;
- handle empty-result cases with a readable message.

## Project structure

```text
.
├── ai_realty_selector.py    # loading, filtering, ranking and CLI
├── realty_data.csv          # demo dataset
├── exam/                    # assignment material
├── tests/                   # automated tests
├── submission.html          # formatted assignment report
└── test_submission_notes.md # verification notes and limitations
```

## Run locally

Requires Python 3.10+.

```bash
python -m pip install -r requirements-dev.txt
python ai_realty_selector.py
```

Example input:

```text
Город: Сочи
Максимальный бюджет: 15000000
Минимальная площадь: 45
Количество вариантов: 3
```

Run the test suite:

```bash
python -m pytest -q
```

CI runs the same test command on pushes and pull requests with Python 3.12.

## Algorithm

1. Read CSV records.
2. Convert numeric fields to `float`.
3. Apply city, budget and area constraints.
4. Rank matching records by distance to the requested limits.
5. Return no more than N records.

This is a demo rule-based selector, not an ML model or an investment recommendation.

## Limitations

The dataset is educational and contains 15 rows. The project does not verify listing freshness, legal status or price accuracy. Further production work would include stronger input validation, external data validation, structured logging and a service/API layer.

## Author

Kirill Kulikov — [GitHub](https://github.com/sma1kyyy)
