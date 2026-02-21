from fastapi import APIRouter, HTTPException, Request
from fastapi.responses import JSONResponse
from app.models.schemas import CommandRequest, CommandResponse
from app.security.validator import validate_command
from app.services.command_executor import execute_command
from app.utils.logger import logger

router = APIRouter()


@router.get("/health")
async def health_check():
    """
    Health check endpoint.
    Used to verify if the service is running.
    """
    return {"status": "ok", "message": "Command Executor API is running"}


@router.post("/execute", response_model=CommandResponse)
async def run_command(payload: CommandRequest, request: Request):
    """
    Executes a validated Linux command and returns output.
    """

    client_ip = request.client.host

    command = payload.command.strip()

    if not command:
        raise HTTPException(status_code=400, detail="Command cannot be empty")

    try:
        # 🔐 Validate command (whitelist based)
        validate_command(command)

        # ⚙️ Execute command
        output = execute_command(command)

        # 📝 Log successful execution
        logger.info(f"[SUCCESS] IP: {client_ip} | Command: {command}")

        return CommandResponse(output=output)

    except ValueError as ve:
        # Validation error
        logger.warning(f"[BLOCKED] IP: {client_ip} | Command: {command} | Reason: {str(ve)}")
        raise HTTPException(status_code=403, detail=str(ve))

    except Exception as e:
        # Unexpected error
        logger.error(f"[ERROR] IP: {client_ip} | Command: {command} | Error: {str(e)}")
        raise HTTPException(status_code=500, detail="Internal Server Error")