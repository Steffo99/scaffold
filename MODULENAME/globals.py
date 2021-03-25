# Module docstring
"""
This module contains the global variables to make the backend work, such as a reference to the config file.
"""

# Special imports
from __future__ import annotations
import royalnet.royaltyping as t

# External imports
import logging
import pathlib
import royalnet.scrolls as s

# Internal imports
# from . import something

# Special global objects
log = logging.getLogger(__name__)


# Code
# TODO: Change the config prefix here
config: s.Scroll = s.Scroll.from_file("MODULENAME", pathlib.Path("config.toml"))


# Objects exported by this module
__all__ = (
    "config",
)
