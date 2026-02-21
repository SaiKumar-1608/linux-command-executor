from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from app.api import api_router
from app.config import settings
from app.utils import logger


def create_application() -> FastAPI:
    """
    Application factory function.
    Creates and configures the FastAPI app instance.
    """

    app = FastAPI(
        title=settings.APP_NAME,
        version=settings.APP_VERSION,
        debug=settings.DEBUG,
    )

    # Enable CORS (allow frontend access)
    app.add_middleware(
    CORSMiddleware,
    allow_origins=[
        "https://linux-command-executor.vercel.app",
    ],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

    # Include API routes
    app.include_router(api_router)

    # Root endpoint
    @app.get("/")
    async def root():
        return {
            "message": "Linux Command Executor API is running",
            "version": settings.APP_VERSION,
        }

    # Startup event
    @app.on_event("startup")
    async def startup_event():
        logger.info("Application started successfully")

    # Shutdown event
    @app.on_event("shutdown")
    async def shutdown_event():
        logger.info("Application shutting down")

    return app


# Create app instance
app = create_application()
