import os
from loguru import logger as _logger

# Ensure logs directory exists
LOG_DIR = "logs"
os.makedirs(LOG_DIR, exist_ok=True)

LOG_FILE_PATH = os.path.join(LOG_DIR, "execution.log")

# Remove default logger
_logger.remove()

# Console logging
_logger.add(
    sink=lambda msg: print(msg, end=""),
    level="INFO",
    format="<green>{time:YYYY-MM-DD HH:mm:ss}</green> | "
           "<level>{level}</level> | "
           "{message}"
)

# File logging with rotation and retention
_logger.add(
    LOG_FILE_PATH,
    level="INFO",
    rotation="1 MB",       # Rotate when file reaches 1MB
    retention="7 days",    # Keep logs for 7 days
    compression="zip",     # Compress old logs
    format="{time:YYYY-MM-DD HH:mm:ss} | "
           "{level} | "
           "{message}"
)

# Export logger
logger = _logger