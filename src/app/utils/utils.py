"""Utils Package."""

from typing import List

from model import Filter


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
