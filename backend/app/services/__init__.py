"""
Services package initializer.

This module exposes business logic functions
for command execution and other service operations.
"""

from app.services.command_executor import execute_command

__all__ = [
    "execute_command",
]