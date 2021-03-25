# Module docstring
"""
This module contains the main backend server.
"""

# Special imports
from __future__ import annotations
import typing as t

# External imports
import logging
import uvicorn
import threading
import datetime
import fastapi as f
import fastapi.middleware.cors as cors
import sqlalchemy.orm as so
import sqlalchemy.sql as ss
import requests
import dataclasses
import pkg_resources

# Internal imports
from . import globals
from . import database
from . import models
from . import auth

# Special global objects
log = logging.getLogger(__name__)
# TODO: Change the metadata name here.
app = f.FastAPI(
    title="MODULENAME",
    description="",
    version=pkg_resources.get_distribution("MODULENAME").version,
)
app.add_middleware(
    cors.CORSMiddleware,
    allow_origins=globals.config["api.alloworigins"],
    allow_methods=["*"],
    allow_headers=["*"],
)


# Code
@app.get(
    "/auth",
    summary="Check your user status.",
    response_model=auth.Auth0AccessClaims,
    tags=["Authorization"],
)
def auth_get(
        *,
        ls: auth.LoginSession = f.Depends(auth.dep_ls),
):
    """
    Decode and verify the signature of your current JWT, returning its contents.
    """
    return ls.cu


# TODO: add your API routes here!
...


# Run the API
if __name__ == "__main__":
    database.init_db()
    uvicorn.run(app, port=globals.config["api.port"])
