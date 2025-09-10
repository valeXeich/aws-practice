from traceback import print_exc

from fastapi.exceptions import RequestValidationError
from fastapi.responses import ORJSONResponse
from starlette import status
from starlette.middleware.base import BaseHTTPMiddleware, RequestResponseEndpoint
from starlette.requests import Request
from starlette.responses import Response

from src.application.common.exceptions import (
    DomainException,
    DuplicateException,
    ForbiddenException,
    NotFoundException,
)


class ExceptionHandlerMiddleware(BaseHTTPMiddleware):
    async def dispatch(self, request: Request, call_next: RequestResponseEndpoint) -> Response:
        self.app.add_exception_handler(RequestValidationError, _unprocessable_entity_exception_handler)

        try:
            response = await call_next(request)
        except Exception as e:
            print_exc()
            return self._handle(e)

        return response

    def _handle(self, exc: Exception) -> ORJSONResponse:
        if isinstance(exc, NotFoundException):
            return ORJSONResponse(exc.info, status_code=status.HTTP_404_NOT_FOUND)

        if isinstance(exc, DuplicateException):
            return ORJSONResponse(exc.info, status_code=status.HTTP_409_CONFLICT)

        if isinstance(exc, ForbiddenException):
            return ORJSONResponse(exc.info, status_code=status.HTTP_403_FORBIDDEN)

        if isinstance(exc, DomainException):
            return ORJSONResponse(exc.info, status_code=status.HTTP_400_BAD_REQUEST)

        if isinstance(exc, RequestValidationError):
            return ORJSONResponse(
                {
                    'success': False,
                    'code': 'Unprocessable Entity',
                    'message': 'Unprocessable Entity',
                    'details': exc.errors(),
                },
                status_code=status.HTTP_422_UNPROCESSABLE_ENTITY,
            )

        return ORJSONResponse(
            {
                'success': False,
                'code': 'Internal Error',
                'message': 'Something went wrong',
            },
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
        )


async def _unprocessable_entity_exception_handler(request: Request, exc: RequestValidationError) -> Response:
    return ORJSONResponse(
        {
            'success': False,
            'code': 'Unprocessable Entity',
            'message': 'Unprocessable Entity',
            'details': exc.errors(),
        },
        status_code=status.HTTP_422_UNPROCESSABLE_ENTITY,
    )
