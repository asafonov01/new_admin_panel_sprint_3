import logging

from logs_format import LOGS_FORMAT

def get_logger():
    logging.basicConfig(
        level=logging.INFO,
        encoding='utf-8',
        format=LOGS_FORMAT,
    )
    logger = logging.getLogger(__file__)
    return logger