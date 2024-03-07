"""Controller Package."""

from typing import Any

from model import Filter, Property
from conf import DBConnection
from conf.constraints import DB_HOST, DB_PORT, DB_SCHEMA, SQL_PATH
from utils import Logger, generate_query, open_file

logger = Logger()


class PropertyController:

    def __init__(self) -> None:
        try:
            self._con = DBConnection()
            logger.info(f"Conectado a la BD: {DB_HOST}:{DB_PORT}/{DB_SCHEMA}")

        except TypeError as error:
            logger.error(f"Error conectando a la BD: {error}")

    def find_properties(self, body: Any) -> Any:
        filters = Filter.to_list_filter(body.get("filters", []))
        query = open_file(f"{SQL_PATH}/FIND_PROPERTIES.sql")
        formated_query = generate_query(query, filters)
        properties = self._con.execute(formated_query)
        return Property.to_json(properties)
