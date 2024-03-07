"""Model Package."""

import json
from dataclasses import dataclass, field
from enum import Enum
from typing import Any, List


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

    @staticmethod
    def to_json(properties: List["Property"]) -> Any:
        """Covert a List of Properties to JSON.

        Arguments:
            properties:  List["Property"] -- List of Properties.

        Returns:
            Any: JSON Properties.
        """
        return json.dumps([vars(property) for property in properties])


class FilterType(Enum):
    """Filter Type Enum."""

    YEAR = "year"
    CITY = "city"
    STATUS = "status"


@dataclass
class Filter:
    """Filter Dataclass."""

    name: FilterType
    value: Any

    @staticmethod
    def to_list_filter(filters: Any) -> List["Filter"]:
        """Covert a JSON to a List of Filters.

        Arguments:
            filters:  Any -- JSON Filters.

        Returns:
            List[Filter] -- List of Filters.
        """
        answer = []
        for filter in filters:
            for key, value in filter.items():
                answer.append(Filter(FilterType(key), value))
        return answer
