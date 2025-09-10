import logging

import uvicorn
from fastapi import FastAPI
from fastapi.responses import ORJSONResponse

from src.infrastructure.db.database import Database
from src.infrastructure.di.container import get_container, setup_di
from src.presentation.api.config import APIConfig, Config
from src.presentation.api.controllers.rest import setup_controllers
from src.presentation.api.middlewares import setup_middlewares

logger = logging.getLogger(__name__)


def create_app() -> FastAPI:
    logger.info('Creating FastAPI app')

    config = Config()

    container = setup_di(config, Database(config.db))

    app = FastAPI(
        title='AWS-Practice',
        version='1.0.0',
        default_response_class=ORJSONResponse,
    )

    app.dependency_overrides[get_container] = lambda: container
    setup_middlewares(app)
    setup_controllers(app)

    return app


def run_app(config: APIConfig) -> None:
    logger.info('Running API')
    uvicorn.run(
        'src.presentation.api.main:create_app',
        host=config.host,
        port=config.port,
        reload=config.reload,
        reload_dirs=config.reload_dirs,
        factory=True,
    )
