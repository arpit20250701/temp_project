"""Top-level package for temp_project."""

__all__ = [
    "__version__",
    "__author__",
    "__email__",
    "cli",
    "health",
]

__author__ = """Yeshwanth Reddy"""
__email__ = "1992chinna@gmail.com"
__version__ = "0.1.0"

from .__pre_init__ import cli
from .health import *
