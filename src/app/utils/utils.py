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
    with open(path, "r") as file:
        data = file.read()
    return data


def generate_query(query: str, filters: List[Filter]) -> str:
    format_query = " ".join(
        [f'AND {filter.name.value} = "{filter.value}"' for filter in filters]
    )
    query = query.format(filter_query=format_query)
    return query


def open_json_file(path: str) -> Any:
    with open(path, "r") as file:
        data = json.load(file)
    return data


def validate_json(json: Any, schema: Any) -> Any:
    try:
        validate(instance=json, schema=schema)
        logger.info("JSON Body Validado")
    except ValidationError as e:
        logger.error(f"Error validando JSON {e.message}")
    return json
