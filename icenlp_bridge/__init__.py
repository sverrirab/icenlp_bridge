"""Top-level package for Python bridge for IceNLP."""

__author__ = """Sverrir Á. Berg"""
__email__ = 'sab@keilir.com'
__version__ = '0.1.0'

__all__ = [
    "parse",
    "init",
]

from .bridge import parse, init
