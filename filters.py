from typing import Callable
from .domain import Order, Restaurant, MenuItem

def by_restaurant(rest_id: str) -> Callable[[Order], bool]:
    def filter_func(order: Order) -> bool:
        return order.rest_id == rest_id
    return filter_func

def by_zone(zone: str) -> Callable[[Restaurant], bool]:
    def filter_func(restaurant: Restaurant) -> bool:
        return restaurant.zone == zone
    return filter_func

def by_price_range(min_price: int, max_price: int) -> Callable[[MenuItem], bool]:
    def filter_func(item: MenuItem) -> bool:
        return min_price <= item.price <= max_price
    return filter_func

def by_time_range(start: str, end: str) -> Callable[[Order], bool]:
    def filter_func(order: Order) -> bool:
        return start <= order.ts <= end
    return filter_func