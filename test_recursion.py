import pytest
from core.recursion import split_route, collect_orders_by_zone
from core.domain import Route, Order, Restaurant


def test_split_route_basic():
    """Тест базового разбиения маршрута"""
    route = Route("rt1", "c1", ("o1", "o2", "o3"), 10, 30)

    result = split_route(route)

    assert len(result) == 3
    assert result[0] == "Order o1 -> Courier c1"
    assert result[1] == "Order o2 -> Courier c1"


def test_split_route_empty():
    """Тест разбиения пустого маршрута"""
    route = Route("rt1", "c1", (), 0, 0)

    result = split_route(route)
    assert result == ()


def test_collect_orders_by_zone():
    """Тест сбора заказов по зоне"""
    restaurants = (
        Restaurant("r1", "Restaurant 1", "north"),
        Restaurant("r2", "Restaurant 2", "south"),
    )

    orders = (
        Order("o1", "r1", (("m1", 1),), 1000, "2024-01-15 10:00:00", "placed"),
        Order("o2", "r2", (("m2", 1),), 1500, "2024-01-15 11:00:00", "placed"),
        Order("o3", "r1", (("m1", 2),), 2000, "2024-01-15 12:00:00", "placed"),
    )

    result = collect_orders_by_zone(orders, restaurants, "north")

    assert len(result) == 2
    assert all(order.rest_id == "r1" for order in result)


def test_collect_orders_empty():
    """Тест сбора заказов с пустыми данными"""
    restaurants = (Restaurant("r1", "Restaurant 1", "north"),)
    orders = ()

    result = collect_orders_by_zone(orders, restaurants, "north")
    assert result == ()


def test_recursive_depth():
    """Тест глубины рекурсии"""
    route = Route("rt1", "c1", ("o1", "o2", "o3", "o4", "o5"), 15, 45)

    result = split_route(route)
    assert len(result) == 5