# Module docstring
"""
This module contains the SQLAlchemy objects that the backend uses to access a PostgreSQL database.
"""

# Special imports
from __future__ import annotations
import royalnet.royaltyping as t

# External imports
import logging
import sqlalchemy as s
import sqlalchemy.orm as so
import datetime
import royalnet.alchemist as ra

# Internal imports
from . import globals

# Special global objects
log = logging.getLogger(__name__)
now = datetime.datetime.now


# Code
Base = so.declarative_base()
engine = s.create_engine(globals.config["database.uri"])
Session = s.orm.sessionmaker(bind=engine)


def init_db() -> None:
    """
    Initialize the database, creating the database itself and the tables that are missing.
    """
    log.debug("Creating the tables based on the declarative base metadata...")
    Base.metadata.create_all(bind=engine)
    log.debug("Database initialization complete!")


def dep_session():
    with Session(future=True) as session:
        yield session



class User(Base, ra.ColRepr, ra.Updatable):
    __tablename__ = "users"

    sub = s.Column("sub", s.String, primary_key=True)
    last_update = s.Column("last_update", s.DateTime)


# TODO: append your tables here
...


# Objects exported by this module
__all__ = (
    "Base",
    "engine",
    "Session",
    "init_db",
    "dep_session",
    "User",
)
