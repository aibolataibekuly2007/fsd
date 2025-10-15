import pytest
from core.transforms import add_order, assign_slot, total_revenue, load_seed
from core.domain import Order, Slot


def test_add_order_immutability():
    """Тест что add_order не изменяет оригинальный tuple"""
    order1 = Order("o1", "r1", (("m1", 1),), 1000, "2024-01-15 10:00:00", "placed")
    order2 = Order("o2", "r1", (("m2", 1),), 1500, "2024-01-15 11:00:00", "placed")

    original = (order1,)
    new_orders = add_order(original, order2)

    assert len(original) == 1
    assert len(new_orders) == 2


def test_assign_slot():
    """Тест назначения слота"""
    slot1 = Slot("s1", "c1", "10:00", "12:00")
    slot2 = Slot("s2", "c1", "13:00", "15:00")

    original = (slot1,)
    new_slots = assign_slot(original, slot2)

    assert len(new_slots) == 2
    assert new_slots[1].id == "s2"


def test_total_revenue():
    """Тест расчета общей выручки"""
    orders = (
        Order("o1", "r1", (("m1", 1),), 1000, "2024-01-15 10:00:00", "delivered"),
        Order("o2", "r1", (("m2", 1),), 1500, "2024-01-15 11:00:00", "delivered"),
        Order("o3", "r1", (("m1", 2),), 2000, "2024-01-15 12:00:00", "placed")
    )

    revenue = total_revenue(orders)
    assert revenue == 4500


def test_load_seed():
    """Тест загрузки seed данных"""
    test_data = {
        "restaurants": [{"id": "r1", "name": "Test", "zone": "center"}],
        "menu_items": [{"id": "m1", "rest_id": "r1", "name": "Item", "price": 1000, "prep_time": 10}],
        "orders": [{"id": "o1", "rest_id": "r1", "items": [["m1", 1]], "total": 1000, "ts": "2024-01-15 10:00:00",
                    "status": "placed"}],
        "couriers": [{"id": "c1", "name": "Alice", "vehicle": "bike", "zone": "center"}],
        "slots": [{"id": "s1", "courier_id": "c1", "start": "10:00", "end": "12:00"}]
    }

    restaurants, menu_items, orders, couriers, slots = load_seed(test_data)

    assert len(restaurants) == 1
    assert len(orders) == 1
    assert restaurants[0].name == "Test"


def test_revenue_empty_orders():
    """Тест выручки с пустым списком заказов"""
    orders = ()
    revenue = total_revenue(orders)
    assert revenue == 0