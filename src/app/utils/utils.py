"""Utils Package."""

from . import Logger
from typing import List
from model import Filter
import json
from jsonschema import validate
from jsonschema.exceptions import ValidationError
from typing import Any

logger = Logger()


def open_file(path: str) -> str:
    """Open a file.

    Arguments:
        path: str -- File path.

    Returns:
        str -- File converted to str.
    """
    with open(path, "r") as file:
        data = file.read()
    return data


def generate_query(query: str, filters: List[Filter]) -> str:
    """Format a query according to filters.

    Arguments:
        query: str -- Base query.
        filters: List[Filter] -- List of Filters.

    Returns:
        str -- Formatted query.
    """
    formatted_query = " ".join(
        [f'AND {filter.name.value} = "{filter.value}"' for filter in filters]
    )
    query = query.format(filter_query=formatted_query)
    return query


def open_json_file(path: str) -> Any:
    """Open a JSON file.

    Arguments:
        path: str -- JSON file path.

    Returns:
        Any -- File converted to JSON.
    """
    with open(path, "r") as file:
        data = json.load(file)
    return data


def validate_json(json: Any, schema: Any) -> Any:
    """Validate a JSON according to schema.

    Arguments:
        json -- JSON File.
        schema -- JSON Schema File.

    Returns:
        Any -- Returns the JSON if it is valid.
    """
    try:
        validate(instance=json, schema=schema)
        logger.info("JSON Body Validado")
    except ValidationError as e:
        logger.error(f"Error validando JSON {e.message}")
    return json
