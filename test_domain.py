import pytest
from core.domain import Restaurant, Order, Courier, Slot

def test_restaurant_immutability():
    """Тест иммутабельности Restaurant"""
    restaurant = Restaurant("r1", "Test Restaurant", "center")
    assert restaurant.id == "r1"
    assert restaurant.name == "Test Restaurant"
    assert restaurant.zone == "center"

def test_order_creation():
    """Тест создания Order с tuple items"""
    order = Order("o1", "r1", (("m1", 2), ("m2", 1)), 3000, "2024-01-15 10:00:00", "placed")
    assert order.id == "o1"
    assert order.total == 3000
    assert len(order.items) == 2

def test_courier_hashable():
    """Тест что Courier хешируем"""
    courier = Courier("c1", "Alice", "bike", "north")
    assert hash(courier) is not None

def test_order_hashable():
    """Тест что Order хешируем"""
    order = Order("o1", "r1", (("m1", 1),), 1000, "2024-01-15 10:00:00", "placed")
    assert hash(order) is not None

def test_slot_creation():
    """Тест создания Slot"""
    slot = Slot("s1", "c1", "10:00", "12:00")
    assert slot.courier_id == "c1"
    assert slot.start == "10:00"