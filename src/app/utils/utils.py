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


def generate_query(filters: List[Filter]) -> str:
    from conf.constraints import SQL_PATH

    query = open_file(f"{SQL_PATH}/FIND_PROPERTIES.sql")

    format_query = " ".join(
        [f'AND {filter.name.value} = "{filter.value}"' for filter in filters]
    )
    query = query.format(filter_query=format_query)
    return query


def open_json_file(path: str) -> Any:
    with open(path, "r") as file:
        data = json.load(file)
    return data


def validate_json() -> Any:
    from conf.constraints import JSON_PATH

    json = open_json_file(f"{JSON_PATH}/filters.json")
    schema = open_json_file(f"{JSON_PATH}/filters_validator_schema.json")
    try:
        validate(instance=json, schema=schema)
        logger.info("JSON Body Validado")
    except ValidationError as e:
        logger.error(f"Error validando JSON {e.message}")
    return json
