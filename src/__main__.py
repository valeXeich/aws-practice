from src.presentation.api.config import Config
from src.presentation.api.main import run_app

if __name__ == '__main__':
    config = Config()
    run_app(config.api)
