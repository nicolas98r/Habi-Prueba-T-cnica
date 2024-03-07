"""Main Package."""

import threading
from http.server import HTTPServer
import requests
import time
from handler import PropertyHandler
from utils import Logger, open_json_file
from conf.constraints import URL_HOST, URL_PORT, JSON_PATH
from typing import Optional

logger = Logger()


def run_server(
    server_class=HTTPServer, handler_class=PropertyHandler, port=URL_PORT
) -> None:
    """Run the HTTPServer.

    Keyword Arguments:
        server_class -- Server class. (default: {HTTPServer})
        handler_class -- Handler class. (default: {PropertyHandler})
        port -- Server Port. (default: {8080})
    """

    server_address = ("", port)
    httpd = server_class(server_address, handler_class)
    logger.info(f"Iniciando Servidor en el Puerto: {port}")
    httpd.serve_forever()


def send_request(request_delay: Optional[int] = 5) -> None:
    time.sleep(request_delay)
    url = f"{URL_HOST}:{URL_PORT}"
    body = open_json_file(f"{JSON_PATH}/filters.json")
    response = requests.post(url, data=body)
    if response.status_code == 200:
        logger.info(
            f"Solicitud POST exitosa\n Respuesta del Servidor: {response.json()}"
        )
    else:
        logger.error(
            "Error al enviar la solicitud POST. \n"
            f"Código de estado: {response.status_code}"
        )


if __name__ == "__main__":
    run_server()
