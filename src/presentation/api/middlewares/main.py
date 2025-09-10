from fastapi import FastAPI
from starlette.middleware.cors import CORSMiddleware

from .exception_middleware import ExceptionHandlerMiddleware
from .process_time_middleware import ProcessTimeMiddleware


def setup_middlewares(app: FastAPI) -> None:
    app.add_middleware(ExceptionHandlerMiddleware)
    app.add_middleware(ProcessTimeMiddleware)
    app.add_middleware(
        CORSMiddleware,
        allow_origins=['*'],
        allow_credentials=True,
        allow_methods=['*'],
        allow_headers=['*'],
    )
