from functools import reduce
from typing import Tuple
from .domain import Order, Slot
from .transforms import add_order, assign_slot, total_revenue


class DeliveryService:
    def __init__(self, orders: Tuple[Order, ...], slots: Tuple[Slot, ...]):
        self.orders = orders
        self.slots = slots

    def place_order(self, order: Order) -> 'DeliveryService':
        new_orders = add_order(self.orders, order)
        return DeliveryService(new_orders, self.slots)

    def assign_courier_slot(self, slot: Slot) -> 'DeliveryService':
        new_slots = assign_slot(self.slots, slot)
        return DeliveryService(self.orders, new_slots)

    def get_revenue(self) -> int:
        return total_revenue(self.orders)

    def get_orders_by_status(self, status: str) -> Tuple[Order, ...]:
        return tuple(filter(lambda o: o.status == status, self.orders))