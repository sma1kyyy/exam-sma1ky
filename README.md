# AI Realty Selector

[![CI](https://github.com/sma1kyyy/exam-sma1ky/actions/workflows/ci.yml/badge.svg)](https://github.com/sma1kyyy/exam-sma1ky/actions/workflows/ci.yml)

A small, testable Python CLI that filters and ranks real-estate records by user constraints.

This repository was prepared as a technical assignment and demonstrates a complete, intentionally simple workflow: CSV ingestion → validation/conversion → filtering → ranking → readable CLI output.

## What it demonstrates

- deterministic rule-based filtering rather than an unsubstantiated ML claim;
- clear separation between data loading, selection logic and CLI interaction;
- automated tests and GitHub Actions CI;
- explicit limitations and production follow-ups.

## Features

- load records from CSV;
- filter by city, maximum budget and minimum area;
- rank matching records by closeness to the requested constraints;
- return up to N results;
- run interactively from the command line.

## Structure

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

Python 3.10+:

```bash
python ai_realty_selector.py
```

Example:

```text
Город: Сочи
Максимальный бюджет: 15000000
Минимальная площадь: 45
Количество вариантов: 3
```

Run tests:

```bash
python -m pip install -r requirements-dev.txt
python -m pytest -q
```

## Algorithm

1. Read CSV records.
2. Convert numeric fields to `float`.
3. Apply city, budget and area constraints.
4. Rank matching records by distance to the requested limits.
5. Return no more than N records.

This is a demo rule-based selector, not an ML model or an investment recommendation.

## Limitations

The dataset is educational and contains 15 rows. The project does not verify listing freshness, legal status or price accuracy. Input validation and empty-result handling are intentionally listed as production follow-ups.

## Author

Kirill Kulikov — [GitHub](https://github.com/sma1kyyy)
