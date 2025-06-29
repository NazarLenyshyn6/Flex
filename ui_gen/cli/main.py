"""
This module defines main entry point for the UI Generation CLI.
"""

from cli.commands.root import ui_gen_group
from cli.commands.mcp import mcp_group
from cli.commands.generate import generate

if __name__ == "__main__":
    ui_gen_group()