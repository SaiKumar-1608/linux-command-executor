from app.config import settings
import re


FORBIDDEN_PATTERNS = [
    r";", r"&&", r"\|\|", r"\|",
    r">", r"<", r"\$\(", r"`"
]

FORBIDDEN_KEYWORDS = [
    "rm", "shutdown", "reboot",
    "kill", "sudo", "mkfs", "dd"
]


def validate_command(command: str) -> None:

    if not command.strip():
        raise ValueError("Command cannot be empty")

    if len(command) > settings.MAX_COMMAND_LENGTH:
        raise ValueError("Command exceeds maximum allowed length")

    base_command = command.strip().split()[0]

    if base_command not in settings.ALLOWED_COMMANDS:
        raise ValueError("Command not allowed")

    for keyword in FORBIDDEN_KEYWORDS:
        if keyword in command:
            raise ValueError("Command contains restricted keyword")

    for pattern in FORBIDDEN_PATTERNS:
        if re.search(pattern, command):
            raise ValueError("Command contains forbidden shell operators")