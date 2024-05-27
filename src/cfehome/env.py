import pathlib
from decouple import Config, RepositoryEnv, config
from functools import lru_cache

BASE_DIR = pathlib.Path(__file__).parent.parent
ROOT_DIR = BASE_DIR.parent
ENV_FILE_NAME = ".env"
ENV_FILE_DIR = BASE_DIR / ENV_FILE_NAME
ENV_ROOT_DIR = ROOT_DIR / ENV_FILE_NAME


@lru_cache
def get_config():
    if ENV_FILE_DIR.exists():
        return Config(RepositoryEnv(str(ENV_FILE_DIR)))
    if ENV_ROOT_DIR.exists():
        return Config(RepositoryEnv(str(ENV_ROOT_DIR)))
    return config


config = get_config()

