from abc import ABC, abstractmethod
from dataclasses import dataclass
from typing import Any


class ApplicationError(ABC, Exception):
    @property
    def message(self) -> str:
        return 'An application error occurred'

    @property
    @abstractmethod
    def code(self) -> str:
        raise NotImplementedError()

    @property
    def info(self) -> dict[str, Any]:
        return {'success': False, 'code': self.code, 'message': self.message}


@dataclass(eq=False)
class DuplicateException(ApplicationError):
    value: Any

    @property
    def message(self) -> str:
        return f'{self.value} already exists, please check your input.'

    @property
    def code(self) -> str:
        return 'Duplicate'


@dataclass(eq=False)
class NotFoundException(ApplicationError):
    value: Any | None = None

    @property
    def message(self) -> str:
        return f'The requested resource: {self.value} was not found.'

    @property
    def code(self) -> str:
        return 'Not found'


@dataclass(eq=False)
class ForbiddenException(ApplicationError):
    @property
    def message(self) -> str:
        return 'Access denied: you do not have the required permissions.'

    @property
    def code(self) -> str:
        return 'Forbidden'


@dataclass(eq=False)
class InvalidOperationException(ApplicationError):
    msg: str

    @property
    def message(self) -> str:
        return self.msg

    @property
    def code(self) -> str:
        return 'Invalid operation'


@dataclass(eq=False)
class DomainException(ABC, Exception):
    @property
    @abstractmethod
    def message(self) -> str:
        raise NotImplementedError()

    @property
    def code(self) -> str:
        return 'Domain'

    @property
    def info(self) -> dict[str, Any]:
        return {'success': False, 'code': self.code, 'message': self.message}
