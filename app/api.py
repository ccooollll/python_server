from fastapi import APIRouter
from app.config.engine import app_config
from app.controllers import ping_controller

webhook_route = app_config.server.ROUTE

api_router = APIRouter()

# Include routers from each controller
# TODO for Kubernetes probes
# api_router.include_router(healthcheck_controller.router)
api_router.include_router(ping_controller.router)