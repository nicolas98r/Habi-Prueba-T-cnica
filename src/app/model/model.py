"""Model Package"""

from dataclasses import dataclass, field
from enum import Enum


class Status(Enum):
    """State of Property Enum."""

    PRE_SALE = "pre_venta"
    FOR_SALE = "en_venta"
    SOLD = "vendido"


@dataclass
class Property:
    """Property Dataclass."""

    address: str = field(metadata={"required": True})
    city: str
    status: Status
    price: int = field(default=0)
    description: str = field(default="", metadata={"required": False})


class FilterType(Enum):
    """Filter Type Enum."""

    YEAR = "year"
    CITY = "city"
    STATUS = "s.name"


@dataclass
class Filter:
    """Filter Dataclass."""

    name: FilterType
    value: any
