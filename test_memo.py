import pytest
import time
from core.memo import compute_route_cost, measure_performance
from core.domain import Order, Courier


def test_compute_route_cost_basic():
    """Тест базового вычисления стоимости маршрута"""
    orders = (
        Order("o1", "r1", (("m1", 1),), 1000, "2024-01-15 10:00:00", "placed"),
        Order("o2", "r1", (("m2", 1),), 1500, "2024-01-15 11:00:00", "placed"),
    )

    couriers = (
        Courier("c1", "Alice", "bike", "north"),
        Courier("c2", "Bob", "car", "south"),
    )

    result = compute_route_cost("route1", orders, couriers)

    assert "distance" in result
    assert "duration" in result
    assert "cost" in result
    assert result["orders_count"] == 2


def test_memoization_performance():
    """Тест производительности мемоизации"""
    orders = (
        Order("o1", "r1", (("m1", 1),), 1000, "2024-01-15 10:00:00", "placed"),
        Order("o2", "r1", (("m2", 1),), 1500, "2024-01-15 11:00:00", "placed"),
    )

    couriers = (
        Courier("c1", "Alice", "bike", "north"),
    )

    performance = measure_performance("test_route", orders, couriers)

    assert performance["first_call_time"] > 0
    assert performance["cached_call_time"] > 0
    assert performance["speedup"] > 1  # Кэшированный вызов должен быть быстрее


def test_identical_inputs_same_output():
    """Тест что одинаковые входные данные дают одинаковый результат"""
    orders = (
        Order("o1", "r1", (("m1", 1),), 1000, "2024-01-15 10:00:00", "placed"),
    )

    couriers = (
        Courier("c1", "Alice", "bike", "north"),
    )

    result1 = compute_route_cost("route1", orders, couriers)
    result2 = compute_route_cost("route1", orders, couriers)

    assert result1 == result2


def test_different_inputs_different_output():
    """Тест что разные входные данные дают разный результат"""
    orders1 = (
        Order("o1", "r1", (("m1", 1),), 1000, "2024-01-15 10:00:00", "placed"),
    )

    orders2 = (
        Order("o1", "r1", (("m1", 1),), 1000, "2024-01-15 10:00:00", "placed"),
        Order("o2", "r1", (("m2", 1),), 1500, "2024-01-15 11:00:00", "placed"),
    )

    couriers = (
        Courier("c1", "Alice", "bike", "north"),
    )

    result1 = compute_route_cost("route1", orders1, couriers)
    result2 = compute_route_cost("route2", orders2, couriers)

    assert result1["orders_count"] == 1
    assert result2["orders_count"] == 2


def test_cache_clear():
    """Тест очистки кэша"""
    orders = (
        Order("o1", "r1", (("m1", 1),), 1000, "2024-01-15 10:00:00", "placed"),
    )

    couriers = (
        Courier("c1", "Alice", "bike", "north"),
    )

    from core.memo import compute_route_cost_cached
    compute_route_cost_cached.cache_clear()

    # После очистки кэша функция должна работать корректно
    result = compute_route_cost("route1", orders, couriers)
    assert result is not None