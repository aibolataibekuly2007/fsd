import pytest
from core.filters import by_restaurant, by_zone, by_price_range, by_time_range
from core.domain import Order, Restaurant, MenuItem


def test_by_restaurant_filter():
    """Тест фильтра по ресторану"""
    order1 = Order("o1", "r1", (("m1", 1),), 1000, "2024-01-15 10:00:00", "placed")
    order2 = Order("o2", "r2", (("m2", 1),), 1500, "2024-01-15 11:00:00", "placed")

    filter_func = by_restaurant("r1")

    assert filter_func(order1) == True
    assert filter_func(order2) == False


def test_by_zone_filter():
    """Тест фильтра по зоне"""
    restaurant1 = Restaurant("r1", "Restaurant 1", "north")
    restaurant2 = Restaurant("r2", "Restaurant 2", "south")

    filter_func = by_zone("north")

    assert filter_func(restaurant1) == True
    assert filter_func(restaurant2) == False


def test_by_price_range_filter():
    """Тест фильтра по диапазону цен"""
    item1 = MenuItem("m1", "r1", "Item 1", 1000, 10)
    item2 = MenuItem("m2", "r1", "Item 2", 2000, 15)
    item3 = MenuItem("m3", "r1", "Item 3", 3000, 20)

    filter_func = by_price_range(1500, 2500)

    assert filter_func(item1) == False
    assert filter_func(item2) == True
    assert filter_func(item3) == False


def test_by_time_range_filter():
    """Тест фильтра по временному диапазону"""
    order1 = Order("o1", "r1", (("m1", 1),), 1000, "2024-01-15 10:30:00", "placed")
    order2 = Order("o2", "r1", (("m2", 1),), 1500, "2024-01-15 14:00:00", "placed")

    filter_func = by_time_range("2024-01-15 09:00:00", "2024-01-15 12:00:00")

    assert filter_func(order1) == True
    assert filter_func(order2) == False


def test_filter_closure_state():
    """Тест что замыкание сохраняет состояние"""
    filter_func = by_restaurant("r1")
    order = Order("o1", "r1", (("m1", 1),), 1000, "2024-01-15 10:00:00", "placed")

    # Фильтр должен "помнить" свой rest_id
    assert filter_func(order) == True