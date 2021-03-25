# Module docstring
"""

"""

# Special imports
from __future__ import annotations
import royalnet.royaltyping as t

# External imports
import logging
import pydantic as p
import datetime

# Internal imports
# from . import something

# Special global objects
log = logging.getLogger(__name__)


# Code
class Model(p.BaseModel):
    pass


class ORMModel(Model):
    class Config(p.BaseConfig):
        orm_mode = True


class UserEditable(ORMModel):
    pass


class UserBasic(UserEditable):
    sub: str
    last_update: datetime.datetime


class UserFull(UserBasic):
    pass


# TODO: Append your models here!
...


# Objects exported by this module
__all__ = (
    "UserEditable",
    "UserBasic",
    "UserFull",
)
