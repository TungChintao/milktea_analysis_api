# app/libs/extensions.py
from contextlib import contextmanager

from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate


db = SQLAlchemy()
migrate = Migrate()