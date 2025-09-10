from fastapi import APIRouter, FastAPI

from .v1.healthcheck.router import router as healthcheck_router

__all__ = ['setup_controllers']


def setup_controllers(app: FastAPI) -> None:
    router_v1 = APIRouter(prefix='/v1')
    router_v1.include_router(healthcheck_router)
    app.include_router(router_v1)
