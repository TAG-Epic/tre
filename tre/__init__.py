from copy import copy
from logging import DEBUG, Formatter, Logger, StreamHandler
from colorama import Fore, Style, init
from sys import stdout

init()

LEVEL_COLORS = {
    "CRITICAL": Fore.RED,
    "ERROR": Fore.LIGHTRED_EX,
    "WARNING": Fore.YELLOW,
    "INFO": Fore.GREEN,
    "DEBUG": Fore.LIGHTBLUE_EX,
}

class ColoredLevelFormatter(Formatter):
    def __init__(self, *args, **kwargs) -> None:
        super().__init__(*args, **kwargs, datefmt="%H:%M:%S")

    def format(self, record):
        # We will be modifying the record, so make a copy
        record = copy(record)

        record.levelname = LEVEL_COLORS[record.levelname] + record.levelname

        return super().format(record)

def setup(logger: Logger):
    out = StreamHandler(stdout)
    out.setLevel(DEBUG)

    formatting = f"{Style.BRIGHT}[%(asctime)s][%(name)s][%(filename)s:%(lineno)03d][%(levelname)s{Fore.WHITE}]{Style.RESET_ALL} %(message)s"

    out.setFormatter(ColoredLevelFormatter(formatting))
    logger.addHandler(out)
