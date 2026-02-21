import subprocess
from app.config import settings


def execute_command(command: str) -> str:
    try:
        result = subprocess.run(
            ["bash", "-c", command],  # force Linux-style execution
            capture_output=True,
            text=True,
            timeout=settings.COMMAND_TIMEOUT
        )

        if result.returncode != 0:
            return result.stderr.strip() or "Command execution failed"

        return result.stdout.strip() or "Command executed successfully (no output)"

    except subprocess.TimeoutExpired:
        raise RuntimeError("Command execution timed out")

    except Exception as e:
        raise RuntimeError(str(e))