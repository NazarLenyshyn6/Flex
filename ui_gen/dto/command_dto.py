"""
This module defines data structures for handling and styling the results of
executed MCP commands via the `claude` CLI.

It includes:
- `CommandExecutionResult`: An immutable result wrapper for command execution,
  capturing the command string, stdout, stderr, and success status.
- `ResultStyle`: A configurable terminal style descriptor used for rendering
  results with optional color and formatting using the `click` library.

These structures support CLI tooling and decorators that execute structured commands
and want to report results in a clean, styled, and testable format.
"""


from typing import Literal, Optional
from dataclasses import dataclass


ClickColor = Literal[
    "black",
    "red",
    "green",
    "yellow",
    "blue",
    "magenta",
    "cyan",
    "white",
]


@dataclass(frozen=True)
class CommandExecutionResult:
    """
    Represents the result of executing an MCP command via the `claude` CLI.

    This data structure is used to standardize output from the `@execute_command` decorator,
    which wraps functions that generate MCP CLI commands. It encapsulates the success status,
    the executed command, and any captured standard output or error messages.

    Attributes:
        success: "True" if the command executed successfully (exit code 0), "False" otherwise.
        command: The exact command that was attempted (e.g., 'claude mcp list').
        output: Captured standard output from the command, if any.
        error: Captured standard error from the command, or exception message if failed.

    Note:
        This class is immutable (`frozen=True`) and intended for structured reporting
        of MCP command executions, not for general subprocess handling.
    """
    success: str
    command: str
    output: str
    error: str
    
    
@dataclass
class ResultStyle:
    """
    Represents terminal text formatting options for command result output.

    Attributes:
        fg: Foreground (text) color.
        bg: Background color.
        bold: Whether to display text in bold.
        underline: Whether to underline the text.

    Used to control the styling of different parts of a CommandExecutionResult
    when printed to the terminal.
    """
    
    fg: Optional[ClickColor] = None
    bg: Optional[ClickColor] = None
    bold: bool = False
    underline: bool = False