"""
This module defines the `generate` CLI command used to trigger UI prompt generation
via Claude Code, supporting both manual and (in future) automatic modes.

It registers the `generate` command to the root CLI group using a custom
`@register_to_group` decorator and routes execution to appropriate generator logic.
"""

import click

from cli.commands.root import ui_gen_group
from cli.utils.command_registry import register_to_group
from cli.utils.result_formatter import ResultFormatter
from gen_engine.generator import manual_generator


@register_to_group(ui_gen_group)
@click.command()
@click.option(
    "--mode", 
    type=click.Choice(["manual", "auto"], case_sensitive=False), 
    default="manual", 
    prompt="Generation mode",
    help="Generation mode: 'manual' for explicit prompt construction, 'auto' (TBD) for intelligent generation."
)
@click.option(
    "--server-name", 
    prompt="Server name",
    help="Name of the MCP server to invoke via Claude CLI."
)
@click.option(
    "--server-prompt", 
    prompt="Server prompt",
    help="System-level instruction or behavior modifier for the Claude agent."
)
@click.option(
    "--user-prompt", 
    prompt="User prompt",
    default="",
    help="User input prompt to include in the generation context (can be empty)."
)
@click.option(
    "--allowed-tools", 
    prompt=True,
    default="Bash,Edit,Replace,Bash(docker*),url,Bash(ls),Bash(cp),Bash(npm),Bash(next),Read,List",
    help="Comma-separated list of tool names the Claude agent is allowed to use."
)
@click.pass_context
def generate(ctx, 
             mode, 
             server_name, 
             server_prompt, 
             user_prompt, 
             allowed_tools):
    """
    \b
    CLI entrypoint for generating user interfaces via Claude Code.

    Depending on the selected mode, this command constructs a structured generation
    request and invokes the appropriate generator. In 'manual' mode, the user provides 
    the full prompt context. In 'auto' mode (not yet implemented), generation will be inferred.
    
    Command result is formatted using `ResultFormatter` with verbosity determined by context.
    """
    if mode == "manual":
        result = manual_generator(
            server_name=server_name,
            server_prompt=server_prompt,
            user_prompt=user_prompt,
            allowed_tools=allowed_tools
        )
        if result is not None:
            ResultFormatter(verbose=ctx.obj.get('VERBOSE', False))(result)
    else:
        click.echo("Auto mode is under development. Stay tuned!")
    