"""Connection Package."""

import mysql.connector as mysql
from conf import DB_HOST, DB_SCHEMA, DB_PASSWORD, DB_PORT, DB_USER


class DBConnection:
    """DBConnection Class."""

    _instance = None
    _con = None

    def __new__(cls, *args, **kwargs):
        if not cls._instance:
            cls._instance = super().__new__(cls, *args, **kwargs)
            cls._con = mysql.connect(
                host=DB_HOST,
                user=DB_USER,
                passwd=DB_PASSWORD,
                database=DB_SCHEMA,
                port=DB_PORT,
            )
        return cls._instance
