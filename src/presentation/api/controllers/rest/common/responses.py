from __future__ import annotations

from pydantic import BaseModel


class Ok(BaseModel):
    success: bool = True


class OkResponse[T](Ok):
    data: T


class Id[T](BaseModel):
    id: T

    @classmethod
    def create(cls, value: T) -> Id[T]:
        return Id(id=value)
