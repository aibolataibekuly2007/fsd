from functools import reduce
from typing import Tuple
from .domain import Order, Slot, Restaurant, MenuItem, Courier


def load_seed(data: dict) -> tuple:
    restaurants = tuple(Restaurant(**r) for r in data.get('restaurants', []))
    menu_items = tuple(MenuItem(**m) for m in data.get('menu_items', []))

    # Преобразуем items из list в tuple для хеширования
    orders_data = []
    for o in data.get('orders', []):
        items_tuple = tuple(tuple(item) for item in o['items'])
        order = Order(
            id=o['id'],
            rest_id=o['rest_id'],
            items=items_tuple,
            total=o['total'],
            ts=o['ts'],
            status=o['status']
        )
        orders_data.append(order)
    orders = tuple(orders_data)

    couriers = tuple(Courier(**c) for c in data.get('couriers', []))
    slots = tuple(Slot(**s) for s in data.get('slots', []))

    return restaurants, menu_items, orders, couriers, slots


def add_order(orders: Tuple[Order, ...], new_order: Order) -> Tuple[Order, ...]:
    return orders + (new_order,)


def assign_slot(slots: Tuple[Slot, ...], new_slot: Slot) -> Tuple[Slot, ...]:
    return slots + (new_slot,)


def total_revenue(orders: Tuple[Order, ...]) -> int:
    return reduce(lambda acc, order: acc + order.total, orders, 0)


def filter_orders(orders: Tuple[Order, ...], predicate) -> Tuple[Order, ...]:
    return tuple(filter(predicate, orders))


def map_orders(orders: Tuple[Order, ...], mapper) -> Tuple:
    return tuple(map(mapper, orders))