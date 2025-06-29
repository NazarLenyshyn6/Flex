"""
This module defines utility functions for managing MCP servers via the Claude Code CLI tool.

Each function constructs a specific MCP-related command (add, remove, list) and executes it 
through the `subprocess_command_executor` decorator, which handles execution logic and returns 
a standardized `CommandExecutionResult`.

Functions:
- add_mcp_server: Registers a new MCP server.
- remove_mcp_server: Removes a registered MCP server.
- list_mcp_servers: Lists all registered MCP servers.
"""


from pathlib import Path

from utils.command_executor import subprocess_command_executor


@subprocess_command_executor(capture_output=True)
def add_mcp_server(
    server_name: str, 
    server_path: str
    ):  
    """
    Constructs a CLI command to register a new MCP server with Claude Code.

    Args:
        server_name: The identifier to assign to the MCP server.
        server_path: Path to the Python file that launches the server.
        
    Raises:
        FileNotFoundError: If the given server_path does not exist.
        
    Returns:
        list[str]: CLI command to register the MCP server.
    """
    if not Path(server_path).exists():
        raise FileNotFoundError(f"Cannot register server: path does not exist → '{server_path}'")
    return ["claude", "mcp", "add", server_name, "--", "python", server_path]
    
    
@subprocess_command_executor(capture_output=True)
def remove_mcp_server(server_name: str):
    """
    Constructs a CLI command to remove an MCP server from Claude Code.

    Args:
        server_name (str): The identifier of the MCP server to remove.

    Returns:
        list[str]: CLI command to remove the MCP server.
    """
    return ["claude", "mcp", "remove", server_name]
  
    
@subprocess_command_executor(capture_output=True)
def list_mcp_servers():
    """
    Constructs a CLI command to list all registered MCP servers in Claude Code.

    Returns:
        list[str]: CLI command to list all MCP servers.
    """
    return ["claude", "mcp", "list"]
