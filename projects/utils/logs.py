import logging

logger = logging.getLogger(__name__)
logger.setLevel(logging.INFO)

format = logging.Formatter(
    "[%(process)d] [%(asctime)s] [%(levelname)s] [%(name)s] [%(module)s] [%(lineno)d] [%(funcName)s] [%(message)s]",
    datefmt="%d-%b-%y %H:%M:%S",
)

ch = logging.StreamHandler()
ch.setFormatter(format)
logger.addHandler(ch)
