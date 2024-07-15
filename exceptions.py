import logging
from logger import logger

class HTTPException(Exception):
    def __init__(self, status_code, message):
        self.status_code = status_code
        self.message = message
        super().__init__(self.message)
        logger.error(f"HTTPException: {status_code} - {message}")
