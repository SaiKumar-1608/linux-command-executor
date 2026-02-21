from fastapi import APIRouter
from app.api.routes import router as command_router

api_router = APIRouter()

# Include command routes
api_router.include_router(
    command_router,
    prefix="/api",
    tags=["Command Execution"]
)