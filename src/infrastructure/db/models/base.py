import uuid
from datetime import datetime
from typing import Self

from sqlalchemy import BIGINT, MetaData, TIMESTAMP
from sqlalchemy.dialects.postgresql import UUID
from sqlalchemy.orm import DeclarativeBase, registry

convention = {
    'ix': 'ix_%(column_0_label)s',  # INDEX
    'uq': 'uq_%(table_name)s_%(column_0_N_name)s',  # UNIQUE
    'ck': 'ck_%(table_name)s_%(constraint_name)s',  # CHECK
    'fk': 'fk_%(table_name)s_%(column_0_N_name)s_%(referred_table_name)s',  # FOREIGN KEY
    'pk': 'pk_%(table_name)s',  # PRIMARY KEY
}

mapper_registry = registry(
    metadata=MetaData(naming_convention=convention),
    type_annotation_map={
        int: BIGINT,
        datetime: TIMESTAMP(timezone=True),
        uuid.UUID: UUID(as_uuid=True),
    },
)


class Base(DeclarativeBase):
    __abstract__ = True

    registry = mapper_registry
    metadata = mapper_registry.metadata

    @classmethod
    async def from_entity[M: Self, E](cls, entity: E) -> M: ...

    async def to_entity[E](self) -> E: ...
