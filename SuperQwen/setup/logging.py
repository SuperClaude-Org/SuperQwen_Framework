import logging
from rich.logging import RichHandler

def setup_logger():
    """Sets up a logger for the application."""
    logging.basicConfig(
        level="INFO",
        format="%(message)s",
        datefmt="[%X]",
        handlers=[RichHandler(rich_tracebacks=True, show_path=False)]
    )
    log = logging.getLogger("rich")
    return log

logger = setup_logger()
