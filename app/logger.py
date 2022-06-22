import os
import sys
import logging

BASE_DIR = os.path.abspath(os.path.join(os.path.dirname(__file__), '..'))


class Logger():

    class CustomFormatter(logging.Formatter):

        grey = '\x1b[38;20m'
        yellow = '\x1b[33;20m'
        red = '\x1b[31;20m'
        bold_red = '\x1b[31;1m'
        reset = '\x1b[0m'
        format = '%(asctime)s [%(levelname)s] %(message)s'

        FORMATS = {
            logging.DEBUG: grey + format + reset,
            logging.INFO: grey + format + reset,
            logging.WARNING: yellow + format + reset,
            logging.ERROR: red + format + reset,
            logging.CRITICAL: bold_red + format + reset
        }

        def format(self, record):
            log_fmt = self.FORMATS.get(record.levelno)
            formatter = logging.Formatter(log_fmt)
            return formatter.format(record)

    def get_logger(self):
        handler = logging.StreamHandler(sys.stdout)
        handler.setFormatter(Logger.CustomFormatter())
        logger = logging.getLogger(__name__)
        logger.setLevel(logging.INFO)
        logger.addHandler(handler)
        return logger
