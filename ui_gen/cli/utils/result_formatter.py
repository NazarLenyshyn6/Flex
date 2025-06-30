"""
This module is designed to support consistent, customizable CLI feedback.

It provides the `ResultFormatter` class, which formats and prints
`CommandExecutionResult` objects with optional verbosity and rich terminal styling.
"""


from typing import Optional
from dataclasses import dataclass

import click
from pydantic import validate_call

from dto.command_dto import (
    CommandExecutionResult, 
    ResultStyle
    )


@dataclass
class ResultFormatter:
    """
    Formats and prints CommandExecutionResult objects using `click.secho`.

    This class provides two modes of output:
    - Basic output via `__call__()` when `verbose` is False (shows only output or error).
    - Verbose output via `__call__()` when `verbose` is True, with styled sections.

    Styles can be customized per result section using `ResultStyle`.
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
                 success_style: ResultStyle = ResultStyle("green", bold=True), 
                 failure_style: ResultStyle = ResultStyle("red", bold=True),
                 command_style: ResultStyle = ResultStyle("cyan"), 
                 output_style: ResultStyle = ResultStyle("white"),
                 error_style: ResultStyle = ResultStyle("red", bold=True)
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
            style = success_style if result.success == "True" else failure_style
            status_emoji = "✅" if result.success == "True" else "❌"
            status_text = "Success" if result.success == "True" else "Failure"
            
            self._format_verbose(f"{status_emoji} Status: {status_text}", style)
            self._format_verbose(f"📄 Command: {result.command}", command_style)
            self._format_verbose(f"📤 Output: {result.output if result.output else 'None'}", output_style)
            self._format_verbose(f"🚫 Error: {result.error}", error_style)
        else:
            if result.success == "True":
                click.echo(result.output)
            else:
                click.echo(result.error)