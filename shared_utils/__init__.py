"""Shared utilities library for cross-repo demo."""

from .calculator import Calculator
from .formatter import format_currency, format_percentage

__version__ = "1.0.0"
__all__ = ["Calculator", "format_currency", "format_percentage"]
