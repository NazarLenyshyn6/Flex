"""
This module is designed to integrate with MCP command execution workflows
and support consistent, customizable CLI feedback.

It provides the `ResultFormatter` class, which formats and prints
`CommandExecutionResult` objects with optional verbosity and rich terminal styling.
"""


from typing import Optional
from dataclasses import dataclass

import click
from pydantic import validate_call

from dto.command_dto import CommandExecutionResult, ResultStyle


@dataclass
class ResultFormatter:
    """
    Formats and prints CommandExecutionResult objects using `click.secho`.

    This class provides two modes of output:
    - Basic output via `__call__()` when `verbose` is False (shows only output or error).
    - Verbose output via `__call__()` when `verbose` is True, with styled sections.

    Styles can be customized per result section using `ResultStyle`.

    Example:
        result = CommandExecutionResult(...)
        formatter = ResultFormatter(verbose=False)
        formatter(result)  # simple

        formatter = ResultFormatter(verbose=True)
        formatter(result)  # styled and detailed
    """
    
    verbose: bool
    
    @staticmethod
    def _format_verbose(message: str, style: ResultStyle):
        """
        Print a styled message to the terminal using click.secho.

        Args:
            message: The message to print.
            style: Styling options for the message.
        """
        click.secho(
            message=message,
            fg=style.fg,
            bg=style.bg,
            bold=style.bold,
            underline=style.underline
            )
        
    @validate_call()
    def __call__(self,
                 result: Optional[CommandExecutionResult],
                 success_style: ResultStyle = ResultStyle("cyan"), 
                 command_style: ResultStyle = ResultStyle("yellow"), 
                 output_style: ResultStyle = ResultStyle("green"),
                 error_style: ResultStyle = ResultStyle("red")
                 ):
        """
        Format and display a CommandExecutionResult either simply or verbosely.

        Args:
            result: The result to format.
            success_style: Style for the success line in verbose mode.
            command_style: Style for the command line in verbose mode.
            output_style: Style for the output line in verbose mode.
            error_style: Style for the error line in verbose mode.
        """
        if not result:
            return
        if self.verbose:
            self._format_verbose(f"Successful: {result.success}", success_style)
            self._format_verbose(f"Command: {result.command}", command_style)
            self._format_verbose(f"Output: {result.output}", output_style)
            self._format_verbose(f"Error: {result.error}", error_style)
        else:
            if result.success == "True":
                click.echo(result.output)
            else:
                click.echo(result.error)