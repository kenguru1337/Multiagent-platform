"""
logging_conf.py — настройка логирования.
"""

import logging


def setup_logging(level="INFO"):
    logging.basicConfig(
        level=getattr(logging, level),
        format="%(asctime)s [%(levelname)s] %(name)s: %(message)s"
    )
    logger = logging.getLogger("multiagent")
    return logger


# Создаём логгер по умолчанию
logger = setup_logging()
