"""This module provides utilities functions"""

import platform
from pathlib import Path
import logging
from logging.handlers import RotatingFileHandler


def get_os_version() -> str:
    """Fectch and return the os version"""
    # Getting the os name
    os_name = platform.system()

    # Getting the os version by os_name
    if os_name.lower() == "windows":
        return platform.release()
    elif os_name.lower() == "linux":
        try:
            version = platform.freedesktop_os_release()
            if "VERSION_ID" in version:
                return version["VERSION_ID"]
            elif "VERSION" in version:
                return version["VERSION"]
        except AttributeError:
            return platform.release()
    else:
        return platform.release()


def get_logging(file: Path, maxbytes: int, backupcount: int) -> logging:
    """Create a logger object, Rotating file handler to save logs
    in a file if it does not exist will create it"""
    logger = logging.getLogger()
    logger.setLevel(logging.INFO)
    handler = RotatingFileHandler(file, maxBytes=maxbytes, backupCount=backupcount)
    formater = logging.Formatter(
        "[%(asctime)s] %(levelname)s - %(message)s", datefmt="%Y-%m-%d %H:%M:%S"
    )
    handler.setFormatter(formater)
    if not logger.handlers:
        logger.addHandler(handler)
    return logger
