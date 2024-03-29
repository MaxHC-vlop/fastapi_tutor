from logging.config import fileConfig

from app.config import settings
from app.database import Base
from app.hotels.models import Hotels
from app.users.models import Users
from app.bookings.models import Bookings
from app.rooms.models import Rooms

from sqlalchemy import engine_from_config
from sqlalchemy import pool

from alembic import context


config = context.config

config.set_main_option("sqlalchemy.url", f"{settings.db_url}?async_fallback=True")


if config.config_file_name is not None:
    fileConfig(config.config_file_name)

target_metadata = Base.metadata


def run_migrations_offline() -> None:
    url = config.get_main_option("sqlalchemy.url")
    context.configure(
        url=url,
        target_metadata=target_metadata,
        literal_binds=True,
        dialect_opts={"paramstyle": "named"},
    )

    with context.begin_transaction():
        context.run_migrations()


def run_migrations_online() -> None:
    connectable = engine_from_config(
        config.get_section(config.config_ini_section, {}),
        prefix="sqlalchemy.",
        poolclass=pool.NullPool,
    )

    with connectable.connect() as connection:
        context.configure(
            connection=connection, target_metadata=target_metadata
        )

        with context.begin_transaction():
            context.run_migrations()


if context.is_offline_mode():
    run_migrations_offline()
else:
    run_migrations_online()
