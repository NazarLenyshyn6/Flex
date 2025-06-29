"""
This module defines CLI commands to manage MCP server integration with Claude Code.

Provides the `mcp` command group with subcommands to add, remove, and list MCP
servers as part of their integration lifecycle with the Claude Code platform.

Supports verbose output for detailed command execution feedback.
"""


import click

from cli.commands.root import ui_gen_group
from cli.utils.command_registry import register_to_group
from cli.utils.result_formatter import ResultFormatter
from mcp_engine.mcp_registry import add_mcp_server as add_server
from mcp_engine.mcp_registry import remove_mcp_server as remove_server
from mcp_engine.mcp_registry import list_mcp_servers as list_servers


@register_to_group(ui_gen_group)
@click.group("mcp")
def mcp_group():
    """
    \b
    Manage MCP server integration with Claude Code.

    Includes commands to add, remove, and list MCP servers integrated
    with Claude Code.
    """
    ...


@register_to_group(mcp_group)
@click.command("add-server")
@click.option(
    "--server-name", 
    prompt="Server name",
    help="Unique identifier for the MCP server."
    )
@click.option(
    "--server-path", 
    prompt="Server path",
    help="File system path to the Python script that launches the MCP server."
    )
@click.pass_context
def add_mcp_server(ctx, server_name, server_path):
    """
    \b
    Register a new MCP server with Claude Code.
    
    Outputs command execution results with optional verbose formatting.
    """
    result = add_server(server_name=server_name, server_path=server_path)
    ResultFormatter(verbose=ctx.obj.get('VERBOSE'))(result)


@register_to_group(mcp_group)
@click.command("remove-server")
@click.option(
    "--server-name", 
    prompt="Server name",
    help="Unique identifier for the MCP server."
    )
@click.pass_context
def remove_mcp_server(ctx, server_name):
    """
    \b
    Remove an MCP server from Claude Code.

    Outputs command execution results with optional verbose formatting.
    """
    result = remove_server(server_name=server_name)
    ResultFormatter(verbose=ctx.obj.get('VERBOSE'))(result)


@register_to_group(mcp_group)
@click.command("list-servers")
@click.pass_context
def list_mcp_servers(ctx):
    """
    \b
    List all MCP servers currently available in Claude Code.

    Outputs command execution results with optional verbose formatting.
    """
    result = list_servers()
    ResultFormatter(verbose=ctx.obj.get('VERBOSE'))(result)