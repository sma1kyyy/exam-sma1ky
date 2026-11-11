from ai_realty_selector import select


def test_select_filters_city_and_budget():
    rows = [
        {"city": "Сочи", "price_per_m2": "100000", "name": "A"},
        {"city": "Сочи", "price_per_m2": "400000", "name": "B"},
        {"city": "Москва", "price_per_m2": "100000", "name": "C"},
    ]

    result = select(rows, city="сочи", budget=5_000_000, area=30)

    assert [row["name"] for row in result] == ["A"]
    assert result[0]["estimated_total"] == "3,000,000"


def test_select_returns_closest_candidates_first():
    rows = [
        {"city": "Сочи", "price_per_m2": "100000", "name": "cheap"},
        {"city": "Сочи", "price_per_m2": "110000", "name": "closest"},
        {"city": "Сочи", "price_per_m2": "50000", "name": "far"},
    ]

    result = select(rows, city="Сочи", budget=3_500_000, area=30)

    assert [row["name"] for row in result] == ["closest", "cheap", "far"]
