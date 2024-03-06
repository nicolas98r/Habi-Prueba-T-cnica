"""Main Package."""

from http.server import HTTPServer
from handler import PropertyHandler
from conf.connection import DBConnection
from conf import DB_HOST, DB_PORT, DB_SCHEMA
from utils import Logger

logger = Logger()


def run(server_class=HTTPServer, handler_class=PropertyHandler, port=8080) -> None:
    """Run the HTTPServer.

    Keyword Arguments:
        server_class -- Server class. (default: {HTTPServer})
        handler_class -- Handler class. (default: {PropertyHandler})
        port -- Server Port. (default: {8080})
    """
    try:
        DBConnection()
        logger.info(f"Conectado a la BD: {DB_HOST}:{DB_PORT}/{DB_SCHEMA}")

    except TypeError as error:
        logger.error(f"Error conectando a la BD: {error}")

    server_address = ("", port)
    httpd = server_class(server_address, handler_class)
    logger.info(f"Iniciando Servidor en el Puerto: {port}")
    httpd.serve_forever()


if __name__ == "__main__":
    run()
