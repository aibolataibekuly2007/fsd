from typing import Generic, TypeVar, Callable, Any
from dataclasses import dataclass

T = TypeVar('T')
E = TypeVar('E')
U = TypeVar('U')


# Maybe monad
class Maybe(Generic[T]):
    @classmethod
    def just(cls, value: T) -> 'Maybe[T]':
        return Just(value)

    @classmethod
    def nothing(cls) -> 'Maybe[T]':
        return Nothing()

    def is_just(self) -> bool:
        return isinstance(self, Just)

    def is_nothing(self) -> bool:
        return isinstance(self, Nothing)


@dataclass(frozen=True)
class Just(Maybe[T]):
    value: T


@dataclass(frozen=True)
class Nothing(Maybe[T]):
    pass


# Either monad
class Either(Generic[E, T]):
    @classmethod
    def right(cls, value: T) -> 'Either[E, T]':
        return Right(value)

    @classmethod
    def left(cls, error: E) -> 'Either[E, T]':
        return Left(error)

    def is_right(self) -> bool:
        return isinstance(self, Right)

    def is_left(self) -> bool:
        return isinstance(self, Left)


@dataclass(frozen=True)
class Right(Either[E, T]):
    value: T


@dataclass(frozen=True)
class Left(Either[E, T]):
    error: E


# Функциональные операции
def safe_order(orders: tuple, oid: str) -> Maybe:
    order = next((o for o in orders if o.id == oid), None)
    return Maybe.just(order) if order else Maybe.nothing()


def validate_order(order, rules: tuple, couriers: tuple) -> Either:
    if order.total > 10000:  # Пример правила
        return Either.left({"error": "Order too expensive"})
    return Either.right(order)


def assign_courier(order, courier) -> Either:
    # Упрощенная проверка - в реальном приложении была бы сложная логика
    if order.total > 5000 and courier.vehicle == "bike":
        return Either.left({"error": "Heavy order cannot be delivered by bike"})
    return Either.right(order)