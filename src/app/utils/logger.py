"""Logger Package."""

import logging


class Logger:
    """Logger Singleton."""

    _instance = None
    _logger = None

    def __new__(cls, *args, **kwargs):
        if not cls._instance:
            cls._instance = super().__new__(cls, *args, **kwargs)
            cls._logger = logging.getLogger("App Logger")
            cls._logger.setLevel(logging.INFO)
            stream = logging.StreamHandler()
            stream.setFormatter(
                logging.Formatter("%(asctime)s [%(levelname)s] %(message)s")
            )
            cls._logger.addHandler(stream)
        return cls._instance

    def info(self, message: str) -> None:
        """Send a message at the INFO level.

        Arguments:
            message:str -- Message to send.
        """
        self._logger.info(message)

    def error(self, message: str) -> None:
        """Send a message at the ERROR level.

        Arguments:
            message:str -- Message to send.
        """
        self._logger.error(message)
