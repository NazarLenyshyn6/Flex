"""
This module defines the root CLI command group `ui-gen` for UI generation tools.

This is the main entry point for all CLI-based operations, including:
- UI generation workflows
- MCP server integration
- Claude Code configuration and management

The root group supports a global `--verbose` flag to enable detailed output
across all subcommands.
"""


import click

@click.group("ui-gen")
@click.option(
    "-v", 
    "--verbose", 
    is_flag=True, 
    help="Enable verbose output"
    )
@click.pass_context
def ui_gen_group(ctx, verbose):
    """
    \b
    Root command group for UI generation CLI tools.

    This group acts as the main entry point for all subcommands related to
    modular UI generation, MCP server integration, and Claude Code workflows.

    All CLI operations start from this group.
    """
    ctx.ensure_object(dict)
    ctx.obj['VERBOSE'] = verbose
    
    
if __name__ == "__main__":
    ui_gen_group()