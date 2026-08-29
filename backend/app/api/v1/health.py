"""
Health check and root endpoints.
"""

from fastapi import APIRouter

from app.core.config import settings

router = APIRouter(
    tags=["Health"],
)


@router.get(
    "/",
    summary="Root Endpoint",
    description="Returns a welcome message for the MoveMate AI Backend.",
)
async def root() -> dict[str, str]:
    """
    Root endpoint.

    Returns:
        Welcome message.
    """
    return {
        "message": f"Welcome to {settings.APP_NAME} 🚀",
    }


@router.get(
    "/health",
    summary="Health Check",
    description="Returns the current health status of the backend service.",
)
async def health_check() -> dict[str, str]:
    """
    Health check endpoint.

    Used by monitoring systems, load balancers,
    Docker, Kubernetes, and deployment platforms
    to verify that the service is running.

    Returns:
        Current application status.
    """
    return {
        "status": "healthy",
        "service": settings.APP_NAME,
        "version": settings.APP_VERSION,
    }