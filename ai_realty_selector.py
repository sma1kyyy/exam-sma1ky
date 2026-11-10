"""Small transparent selector for the AI-realty internship task.

Run: python ai_realty_selector.py
The input data is intentionally kept in a CSV so every price and deadline can
be checked against its source before submission.
"""
from __future__ import annotations

import csv
from pathlib import Path


DATA = Path(__file__).with_name("realty_data.csv")


def load_rows() -> list[dict[str, str]]:
    with DATA.open(encoding="utf-8-sig", newline="") as fh:
        return list(csv.DictReader(fh))


def select(rows: list[dict[str, str]], city: str, budget: float, area: float) -> list[dict[str, str]]:
    candidates = []
    for row in rows:
        if row["city"].casefold() != city.casefold():
            continue
        price = float(row["price_per_m2"])
        estimated = price * area
        if estimated <= budget:
            candidates.append((budget - estimated, row | {"estimated_total": f"{estimated:,.0f}"}))
    candidates.sort(key=lambda item: item[0])
    return [row for _, row in candidates[:3]]


def main() -> None:
    rows = load_rows()
    city = input("Город: ").strip()
    budget = float(input("Budget in rubles: ").replace(" ", ""))
    area = float(input("Area in square meters: ").replace(",", "."))
    result = select(rows, city, budget, area)
    if not result:
        print("Подходящих ЖК в таблице не найдено.")
        return
    for index, row in enumerate(result, 1):
        print(f"{index}. {row['name']} — {row['class']} — {row['estimated_total']} ₽")
        print(f"   Застройщик: {row['developer']}; сдача: {row['delivery']}")
        print(f"   Источник: {row['source']}")


if __name__ == "__main__":
    main()

