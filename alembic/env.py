from logging.config import fileConfig

from sqlalchemy import engine_from_config
from sqlalchemy import pool

from alembic import context

#continuare la notitele din caiet/ facem conectarea Base=declarative_base() din file database.py
from app.models import Base

#accesing the envirnment varialbles using settings/ settings in config detine informatia din urls sqlalchemy care este name, password, host, etc, il detine in forma ascunsa
#dupa ce instalez Settings jos la url in loc de username, password scriu {settings.database_username}.. si tot asa mai departe
from app.config import Settings


# this is the Alembic Config object, which provides
# access to the values within the .ini file in use.
config = context.config

# continuarea din alembic.ini file/ dupa ce am schimbat tot aici sterg tabelele din PGAdmin si continui sa le creez prin Alembic


congif.set_main_option("sqlalchemy.url", f'postgresql://{settings.database_username}:{settings.database_password}@{settings.database_hostname}:{settings.database_port}/{settings.database_name}')

# Interpret the config file for Python logging.
# This line sets up loggers basically.
if config.config_file_name is not None:
    fileConfig(config.config_file_name)

# add your model's MetaData object here
# for 'autogenerate' support
# from myapp import mymodel
# target_metadata = mymodel.Base.metadata

# dupa ce am importat Base sus scrim aici pentru a accessa-o
target_metadata = Base.metadata
# 

# other values from the config, defined by the needs of env.py,
# can be acquired:
# my_important_option = config.get_main_option("my_important_option")
# ... etc.


def run_migrations_offline() -> None:
    """Run migrations in 'offline' mode.

    This configures the context with just a URL
    and not an Engine, though an Engine is acceptable
    here as well.  By skipping the Engine creation
    we don't even need a DBAPI to be available.

    Calls to context.execute() here emit the given string to the
    script output.

    """
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
    """Run migrations in 'online' mode.

    In this scenario we need to create an Engine
    and associate a connection with the context.

    """
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
