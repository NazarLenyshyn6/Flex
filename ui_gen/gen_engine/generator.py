"""
This module defines prompt generator command builders for use with the Claude CLI.

It provides manual and automatic generation utilities, where each function constructs 
a command suitable for interactive or automated invocation via Claude’s MCP interface.

Functions:
- manual_generator: Constructs and executes a manual Claude command using user and server prompts.
- auto_generator: Placeholder for future implementation of automatic prompt generation.
"""


from typing import List

from utils.command_executor import subprocess_command_executor


@subprocess_command_executor(capture_output=False)
def manual_generator(server_name: str, 
                     server_prompt: str, 
                     user_prompt: str,
                     allowed_tools: str
                     ) -> List[str]:
    """
    Constructs a Claude CLI command for manually invoking a server prompt with tool constraints.

    Args:
        server_name: Name of the MCP server to target.
        server_prompt: The system-level prompt that guides Claude's behavior.
        user_prompt: The actual prompt provided by the end user.
        allowed_tools: A string of tool names or identifiers Claude is allowed to use.

    Returns:
        list[str]: The full CLI command to execute via Claude.
    """
    prompt = f"/{server_name}:{server_prompt} (MCP) {user_prompt}"
    return ["claude", prompt, allowed_tools]


def auto_generator():
    """
    Constructs a Claude CLI command for automatically generating a prompt.

    This function is a placeholder for future implementation of prompt auto-generation logic.

    Returns:
        TBD
    """