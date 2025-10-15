from dataclasses import dataclass
from typing import Tuple, Dict, Any


@dataclass(frozen=True)
class Restaurant:
    id: str
    name: str
    zone: str


@dataclass(frozen=True)
class MenuItem:
    id: str
    rest_id: str
    name: str
    price: int
    prep_time: int


@dataclass(frozen=True)
class Order:
    id: str
    rest_id: str
    items: Tuple[Tuple[str, int], ...]
    total: int
    ts: str
    status: str

    def __hash__(self):
        return hash((self.id, self.rest_id, self.items, self.total, self.ts, self.status))


@dataclass(frozen=True)
class Courier:
    id: str
    name: str
    vehicle: str
    zone: str

    def __hash__(self):
        return hash((self.id, self.name, self.vehicle, self.zone))


@dataclass(frozen=True)
class Slot:
    id: str
    courier_id: str
    start: str
    end: str


@dataclass(frozen=True)
class Route:
    id: str
    courier_id: str
    orders: Tuple[str, ...]
    distance: int
    duration: int


@dataclass(frozen=True)
class Event:
    id: str
    ts: str
    name: str
    payload: Dict[str, Any]


@dataclass(frozen=True)
class Rule:
    id: str
    kind: str
    payload: Dict[str, Any]