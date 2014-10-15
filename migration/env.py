from __future__ import with_statement
from alembic import context
from sqlalchemy import engine_from_config, pool

config = context.config

from parsidan import model

target_metadata = model.metadata


def run_migrations_offline():
    url = config.get_section_option('app:main', "sqlalchemy.url")
    context.configure(url=url, version_table='migrate_version')

    with context.begin_transaction():
        context.run_migrations()


def run_migrations_online():
    engine = engine_from_config(
                config.get_section('app:main'),
                prefix='sqlalchemy.',
                poolclass=pool.NullPool)

    connection = engine.connect()
    context.configure(
                connection=connection,
                target_metadata=target_metadata,
                version_table='migrate_version'
                )

    try:
        with context.begin_transaction():
            context.run_migrations()
    finally:
        connection.close()

if context.is_offline_mode():
    run_migrations_offline()
else:
    run_migrations_online()

