import logging

logging.basicConfig(
    level=30,
    format="%(filename)s - %(message)s - date: %(asctime)s- function: %(funcName)s",
    filename="Yum.log"
)

logger = logging.getLogger('')