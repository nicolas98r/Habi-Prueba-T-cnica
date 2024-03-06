"""Controller Package."""

from typing import List

from model import Filter, Property
from conf import DBConnection
from conf.constraints import DB_HOST, DB_PORT, DB_SCHEMA
from utils import Logger, generate_query

logger = Logger()


class PropertyController:

    def __init__(self) -> None:
        try:
            self._con = DBConnection()
            logger.info(f"Conectado a la BD: {DB_HOST}:{DB_PORT}/{DB_SCHEMA}")

        except TypeError as error:
            logger.error(f"Error conectando a la BD: {error}")

    def find_properties(self, filters: List[Filter]) -> List[Property]:
        query = generate_query(filters)
        return self._con.execute(query)
