import logging


def get_logger():

    logger = logging.getLogger(__name__)

    logger.setLevel(logging.INFO)

    # Prevent duplicate logs
    if not logger.handlers:

        file_handler = logging.FileHandler(
            "logs/test.log"
        )

        formatter = logging.Formatter(
            "%(asctime)s - %(levelname)s - %(message)s"
        )

        file_handler.setFormatter(
            formatter
        )

        logger.addHandler(
            file_handler
        )

    return logger