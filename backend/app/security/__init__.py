"""
Security package initializer.

This module exposes security-related utilities
such as command validation.
"""

from app.security.validator import validate_command

__all__ = [
    "validate_command",
]