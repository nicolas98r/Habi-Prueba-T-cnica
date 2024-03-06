"""Constraints Package."""

import os
from dotenv import load_dotenv
from utils import Logger

secrets_path = ".env"
logger = Logger()


if not os.path.exists(secrets_path):
    logger.error("Error cargando el archivo .env")
    raise Exception("No existe el archivo .env")

load_dotenv(secrets_path)

# DB Connection Constants
DB_HOST = os.environ.get("DB_HOST")
DB_PORT = os.environ.get("DB_PORT")
DB_SCHEMA = os.environ.get("DB_SCHEMA")
DB_USER = os.environ.get("DB_USER")
DB_PASSWORD = os.environ.get("DB_PASSWORD")
