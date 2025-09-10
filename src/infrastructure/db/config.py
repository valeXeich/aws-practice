from pydantic import BaseModel


class DBConfig(BaseModel):
    host: str
    port: int
    username: str
    password: str
    echo: bool

    @property
    def url(self):
        return f'postgresql+asyncpg://{self.username}:{self.password}@{self.host}:{self.port}/postgres'
