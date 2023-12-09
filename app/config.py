from dataclasses import dataclass

from environs import Env

env = Env()
env.read_env()


@dataclass(frozen=True, slots=True)
class Settings:
    db_url: str = env.str(
        'DATABASE_URL',
    )


settings = Settings()
