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
    help="""
    Generation mode: 'manual' for explicit control over the Claude Code generation process, 
    'auto' for automated prompt generation (under development).
    """
)
@click.option(
    "--server-name", 
    prompt="Server name",
    help="MCP server name used to locate the predefined prompt for system-level instruction for the Claude agent."
)
@click.option(
    "--server-prompt", 
    prompt="Server prompt",
    help="Predefined prompt name used as a system-level instruction for the Claude agent."
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
    Generate user interfaces via Claude Code.

    Depending on the selected mode, this command builds a structured generation
    request and invokes the corresponding generator. In 'manual' mode, the user 
    has full control over the Claude Code generation process. In 'auto' mode 
    (currently not implemented), the entire generation workflow will be automated.

    Command output is formatted using `ResultFormatter`, with verbosity controlled by the CLI context.
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
    