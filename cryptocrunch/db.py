import sqlite3
import os

from pathlib import Path

import click

from flask import current_app, g
from flask.cli import with_appcontext

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
RESOURCES_DIR = os.path.join(BASE_DIR, 'resources')


def get_db():
    if 'db' not in g:
        g.db = sqlite3.connect(
            current_app.config['DATABASE'],
            detect_types=sqlite3.PARSE_DECLTYPES,
            check_same_thread=False
        )
        g.db.row_factory = sqlite3.Row
    return g.db


def close_db(e=None):
    db = g.pop('db', None)
    if db is not None:
        db.close()


def init_db():
    db = get_db()
    expression = 'create_*.sql'
    for file in Path(RESOURCES_DIR).glob(expression):
        with file.open('r') as ddl:
            db.executescript(ddl.read())


@click.command('init-db')
@with_appcontext
def init_db_command():
    init_db()
    click.echo('Initialized the database')


def drop_db():
    db = get_db()
    expression = 'drop_*.sql'
    for file in Path(RESOURCES_DIR).glob(expression):
        with file.open('r') as ddl:
            db.executescript(ddl.read())


@click.command('drop-db')
@with_appcontext
def drop_db_command():
    drop_db()
    click.echo('Dropped the database')


def init_app(app):
    app.teardown_appcontext(close_db)
    app.cli.add_command(init_db_command)
    app.cli.add_command(drop_db_command)
