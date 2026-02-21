import os
from dotenv import load_dotenv
from typing import List

# Load environment variables from .env file
load_dotenv()


class Settings:
    """
    Application configuration settings.
    Loads values from environment variables with sensible defaults.
    """

    # App settings
    APP_NAME: str = os.getenv("APP_NAME", "Linux Command Executor API")
    APP_VERSION: str = os.getenv("APP_VERSION", "1.0.0")
    DEBUG: bool = os.getenv("DEBUG", "False").lower() == "true"

    # Security settings
    MAX_COMMAND_LENGTH: int = int(os.getenv("MAX_COMMAND_LENGTH", 500))
    COMMAND_TIMEOUT: int = int(os.getenv("COMMAND_TIMEOUT", 5))

    # Allowed commands (comma-separated in .env)
    ALLOWED_COMMANDS: List[str] = (
        [cmd.strip() for cmd in os.getenv("ALLOWED_COMMANDS", "").split(",") if cmd.strip()]
        or ["ls", "pwd", "whoami", "date", "echo"]
    )


# Create a single settings instance
settings = Settings()