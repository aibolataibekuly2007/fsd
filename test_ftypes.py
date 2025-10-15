import pytest
from core.ftypes import Maybe, Either, safe_order, validate_order, assign_courier
from core.domain import Order, Courier


def test_maybe_just():
    """Тест Maybe.Just"""
    maybe = Maybe.just("test value")
    assert maybe.is_just() == True
    assert maybe.is_nothing() == False
    assert maybe.value == "test value"


def test_maybe_nothing():
    """Тест Maybe.Nothing"""
    maybe = Maybe.nothing()
    assert maybe.is_just() == False
    assert maybe.is_nothing() == True


def test_either_right():
    """Тест Either.Right"""
    either = Either.right("success")
    assert either.is_right() == True
    assert either.is_left() == False
    assert either.value == "success"


def test_either_left():
    """Тест Either.Left"""
    either = Either.left("error")
    assert either.is_right() == False
    assert either.is_left() == True
    assert either.error == "error"


def test_safe_order_found():
    """Тест safe_order когда заказ найден"""
    orders = (
        Order("o1", "r1", (("m1", 1),), 1000, "2024-01-15 10:00:00", "placed"),
        Order("o2", "r1", (("m2", 1),), 1500, "2024-01-15 11:00:00", "placed"),
    )

    result = safe_order(orders, "o1")
    assert result.is_just() == True
    assert result.value.id == "o1"


def test_safe_order_not_found():
    """Тест safe_order когда заказ не найден"""
    orders = (
        Order("o1", "r1", (("m1", 1),), 1000, "2024-01-15 10:00:00", "placed"),
    )

    result = safe_order(orders, "nonexistent")
    assert result.is_nothing() == True


def test_validate_order_success():
    """Тест успешной валидации заказа"""
    order = Order("o1", "r1", (("m1", 1),), 5000, "2024-01-15 10:00:00", "placed")
    couriers = (Courier("c1", "Alice", "bike", "north"),)

    result = validate_order(order, (), couriers)
    assert result.is_right() == True


def test_validate_order_failure():
    """Тест неудачной валидации заказа"""
    order = Order("o1", "r1", (("m1", 1),), 15000, "2024-01-15 10:00:00", "placed")  # Слишком дорогой
    couriers = (Courier("c1", "Alice", "bike", "north"),)

    result = validate_order(order, (), couriers)
    assert result.is_left() == True


def test_assign_courier_success():
    """Тест успешного назначения курьера"""
    order = Order("o1", "r1", (("m1", 1),), 3000, "2024-01-15 10:00:00", "placed")
    courier = Courier("c1", "Alice", "car", "north")

    result = assign_courier(order, courier)
    assert result.is_right() == True


def test_assign_courier_failure():
    """Тест неудачного назначения курьера"""
    order = Order("o1", "r1", (("m1", 1),), 6000, "2024-01-15 10:00:00", "placed")  # Тяжелый заказ
    courier = Courier("c1", "Alice", "bike", "north")  # Не подходит для тяжелых заказов

    result = assign_courier(order, courier)
    assert result.is_left() == True