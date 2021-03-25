# Module docstring
"""
This module contains the FastAPI dependencies necessary to make the Auth0-based authentication system work.
"""

# Special imports
from __future__ import annotations
import royalnet.royaltyping as t

# External imports
import logging
import pydantic as p
import fastapi_cloudauth.auth0 as faca
import dataclasses
import sqlalchemy.orm as so
import datetime
import fastapi as f
import sqlalchemy.sql as ss

# Internal imports
from . import globals
from . import database

# Special global objects
log = logging.getLogger(__name__)


# Code
class Auth0AccessClaims(p.BaseModel):
    iss: str
    sub: str
    aud: t.Union[t.List[str], str]
    iat: int
    exp: int
    azp: str
    scope: str
    permissions: t.List[str]

    # You can extend this with custom fields:
    # ryg_name: str = p.Field(..., alias="https://meta.ryg.one/name")
    # ryg_picture: p.HttpUrl = p.Field(..., alias="https://meta.ryg.one/picture")


class Auth0User(faca.Auth0CurrentUser):
    user_info = Auth0AccessClaims


CurrentAuth0User = Auth0User(domain=globals.config["authzero.domain"])


@dataclasses.dataclass()
class LoginSession:
    cu: Auth0AccessClaims
    session: so.Session


def dep_ls(
        cu: Auth0AccessClaims = f.Depends(CurrentAuth0User),
        session: so.Session = f.Depends(database.dep_session),
):
    db_user: t.Optional[database.User] = session.execute(
        ss.select(database.User).where(database.User.sub == cu.sub)
    ).scalar()
    if db_user is None:
        db_user = database.User(
            sub=cu.sub,
            last_update=datetime.datetime.now(),
            name=cu.ryg_name,
            picture=cu.ryg_picture,
        )
        session.add(db_user)
    else:
        db_user.update(
            sub=cu.sub,
            last_update=datetime.datetime.now(),
            name=cu.ryg_name,
            picture=cu.ryg_picture,
        )
    session.commit()
    return LoginSession(cu=cu, session=session)


# Objects exported by this module
__all__ = (
    "Auth0AccessClaims",
    "Auth0User",
    "CurrentAuth0User",
    "LoginSession",
    "dep_ls",
)
