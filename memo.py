from functools import lru_cache
from typing import Dict, Any, Tuple
from .domain import Order, Courier
import time


@lru_cache(maxsize=128)
def compute_route_cost_cached(route_id: str, order_ids: Tuple[str, ...], courier_ids: Tuple[str, ...]) -> Dict[
    str, Any]:
    """Дорогая функция вычисления стоимости маршрута с кэшированием"""
    time.sleep(0.1)  # Имитация сложных вычислений

    total_orders = len(order_ids)
    total_distance = sum(len(order_id) * 2 for order_id in order_ids)
    total_duration = sum(len(order_id) for order_id in order_ids) * 3
    base_cost = total_orders * 100

    # Упрощенный расчет стоимости
    cost = base_cost + total_distance * 2 + total_duration * 5

    return {
        "distance": total_distance,
        "duration": total_duration,
        "cost": cost,
        "orders_count": total_orders,
        "route_id": route_id
    }


def compute_route_cost(route_id: str, orders: Tuple[Order, ...], couriers: Tuple[Courier, ...]) -> Dict[str, Any]:
    """Обертка для работы с объектами Order и Courier"""
    order_ids = tuple(order.id for order in orders)
    courier_ids = tuple(courier.id for courier in couriers)
    return compute_route_cost_cached(route_id, order_ids, courier_ids)


def measure_performance(route_id: str, orders: Tuple[Order, ...], couriers: Tuple[Courier, ...]):
    """Замер производительности до/после кэширования"""
    # Очищаем кэш для чистоты эксперимента
    compute_route_cost_cached.cache_clear()

    # Первый вызов (без кэша)
    start = time.time()
    result1 = compute_route_cost(route_id, orders, couriers)
    time1 = time.time() - start

    # Второй вызов (с кэшем)
    start = time.time()
    result2 = compute_route_cost(route_id, orders, couriers)
    time2 = time.time() - start

    return {
        "first_call_time": time1,
        "cached_call_time": time2,
        "speedup": time1 / time2 if time2 > 0 else 0,
        "result": result1
    }