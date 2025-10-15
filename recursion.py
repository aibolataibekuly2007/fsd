from typing import Tuple
from .domain import Route, Order, Restaurant

def split_route(route: Route) -> Tuple[str, ...]:
    def _split_recursive(orders: Tuple[str, ...], acc: Tuple[str, ...]) -> Tuple[str, ...]:
        if not orders:
            return acc
        current = f"Order {orders[0]} -> Courier {route.courier_id}"
        return _split_recursive(orders[1:], acc + (current,))
    return _split_recursive(route.orders, ())

def collect_orders_by_zone(orders: Tuple[Order, ...], restaurants: Tuple[Restaurant, ...], zone: str) -> Tuple[Order, ...]:
    def _collect_recursive(remaining_orders: Tuple[Order, ...], acc: Tuple[Order, ...]) -> Tuple[Order, ...]:
        if not remaining_orders:
            return acc
        current_order = remaining_orders[0]
        restaurant = next((r for r in restaurants if r.id == current_order.rest_id), None)
        if restaurant and restaurant.zone == zone:
            return _collect_recursive(remaining_orders[1:], acc + (current_order,))
        return _collect_recursive(remaining_orders[1:], acc)
    return _collect_recursive(orders, ())