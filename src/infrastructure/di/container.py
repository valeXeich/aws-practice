from dishka import AsyncContainer, Provider, Scope, make_async_container
from sqlalchemy.ext.asyncio import AsyncSession

from src.infrastructure.db.database import Database
from src.presentation.api.config import Config


def get_container() -> AsyncContainer:
    raise NotImplementedError()


class MainProvider(Provider):
    def __init__(self, config: Config, database: Database, scope: Scope) -> None:
        super().__init__(scope)
        self._config = config
        self._database = database

    # provides = ()


def setup_providers(config: Config, database: Database) -> list[Provider]:
    provider = MainProvider(config, database, Scope.APP)
    provider.provide(database.get_session, provides=AsyncSession, scope=Scope.REQUEST)

    providers = [provider]
    return providers


def setup_di(config: Config, database: Database) -> AsyncContainer:
    providers = setup_providers(config, database)
    container = make_async_container(*providers)
    return container
