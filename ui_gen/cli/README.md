# CLI Interface

A comprehensive command-line interface for UI generation and MCP server management built on Click framework. The CLI provides a scalable, modular architecture for managing prompt-based code generation workflows and Claude Code MCP server integration with rich terminal output formatting and subprocess command execution.

## Overview

The CLI system provides a unified command interface for interacting with the prompt engine, MCP engine, and generation engine components. It offers structured command organization, automatic registration patterns, and comprehensive result formatting for both simple and verbose output modes. The system supports interactive prompts, timeout-aware command execution, and comprehensive error handling designed for both interactive use and automation workflows.

## Architecture

### Core Components

#### 1. **Root Command Group** (`commands/root.py`)
Main entry point for the CLI application:

- **Command Group**: `ui-gen` - Root command group for all operations
- **Global Options**: `--verbose/-v` flag for detailed output across all subcommands
- **Context Management**: Click context object for passing state between commands
- **Entry Point**: Main CLI entry point for all UI generation workflows

#### 2. **MCP Command Group** (`commands/mcp.py`)
Specialized command group for MCP server management:

- **Server Management**: Add, remove, and list MCP servers in Claude Code
- **Interactive Prompts**: Built-in prompts for server name and path inputs
- **Result Integration**: Seamless integration with MCP engine command execution
- **Verbose Support**: Conditional verbose formatting based on global flag

#### 3. **Generate Commands** (`commands/generate.py`)
UI generation command implementations with Claude Code integration:

- **Manual Generation**: Manual prompt generation via Claude CLI
- **Auto Generation**: Automatic generation capabilities
- **Mode Selection**: Interactive mode selection with validation
- **Tool Restrictions**: Configurable tool allowlist for Claude agent safety
- **Server Integration**: Direct MCP server invocation through Claude Code
- **Subprocess Execution**: Timeout-aware command execution with comprehensive error handling

**Key Methods:**
- `generate()`: Main CLI command with interactive prompts for all parameters
- `manual_generator()`: Constructs Claude CLI commands with tool restrictions
- `auto_generator()`: Automatic generation capabilities

#### 4. **Command Registry** (`utils/command_registry.py`)
Decorator-based command registration system:

- **Auto-Registration**: `@register_to_group` decorator for automatic command registration
- **Scalable Architecture**: Reduces boilerplate and centralizes registration logic
- **Type Safety**: Type-aware decorator with Click command/group support
- **Modular Design**: Enables distributed command definition across modules

#### 5. **Result Formatter** (`utils/result_formatter.py`)
Comprehensive output formatting system with terminal styling:

- **Dual Modes**: Basic and verbose output formatting with context awareness
- **Styled Output**: Customizable colors and formatting using Click's secho
- **DTO Integration**: Native support for CommandExecutionResult formatting
- **Terminal Support**: Rich terminal output with 8-color support and text formatting
- **Pydantic Validation**: Built-in validation for formatting parameters
- **Context Awareness**: Respects global verbose flag from Click context

**Key Methods:**
- `__call__()`: Main formatting method with customizable styles
- `_format_verbose()`: Internal styled message formatting
- Built-in styles: success (cyan), command (yellow), output (green), error (red)

#### 6. **Main Entry Point** (`main.py`)
Application bootstrap and entry point:

- **CLI Initialization**: Main entry point for the application
- **Command Loading**: Automatic loading of command groups
- **Module Integration**: Coordinates all CLI components

## Key Features

- **Hierarchical Commands**: Multi-level command structure with groups and subcommands
- **Interactive Prompts**: Built-in user input prompts for required parameters with Click validation
- **Verbose Output**: Context-aware detailed command execution feedback with terminal styling
- **Auto-Registration**: Decorator-based command registration system with type safety
- **MCP Integration**: Native support for MCP server management operations via Claude CLI
- **Subprocess Execution**: Timeout-aware command execution with comprehensive error handling
- **Claude Code Integration**: Direct integration with Claude Code CLI for prompt generation
- **Tool Restrictions**: Configurable tool allowlists for Claude agent safety
- **Error Handling**: Structured error reporting with CommandExecutionResult DTOs
- **Terminal Styling**: Rich terminal output with 8-color support and text formatting
- **Context Passing**: Shared state management across command hierarchy with Click context
- **Path Validation**: Automatic file system validation for MCP server registration

## Usage


### Basic Commands

```bash
# Show help for main command
ui-gen --help

# Enable verbose output globally
ui-gen --verbose [command]

# Show MCP command help
ui-gen mcp --help
```

### MCP Server Management

```bash
# Add a new MCP server (interactive prompts)
ui-gen mcp add-server

# Add server with parameters
ui-gen mcp add-server --server-name "my_server" --server-path "/path/to/server.py"

# Remove an MCP server
ui-gen mcp remove-server --server-name "my_server"

# List all registered MCP servers
ui-gen mcp list-servers

# Verbose output for detailed command execution
ui-gen --verbose mcp list-servers
```

### UI Generation Commands

```bash
# Generate UI using manual mode (interactive prompts)
ui-gen generate

# Generate with specific parameters
ui-gen generate --mode manual --server-name "my_server" --server-prompt "Generate a React component" --user-prompt "Create a login form" --allowed-tools "Bash,Edit,Read"

# Generate with verbose output
ui-gen --verbose generate --mode manual

# Auto mode
ui-gen generate --mode auto
```

**Default Allowed Tools:**
```
Bash,Edit,Replace,Bash(docker*),url,Bash(ls),Bash(cp),Bash(npm),Bash(next),Read,List
```

**Generate Command Parameters:**
- `--mode`: Generation mode (`manual` or `auto`) - defaults to `manual` if not specified
- `--server-name`: MCP server identifier - required, will prompt if not provided
- `--server-prompt`: System-level instruction for Claude - required, will prompt if not provided  
- `--user-prompt`: User input prompt - optional, will prompt with empty default
- `--allowed-tools`: Comma-separated tool allowlist - defaults to predefined list if not specified

## Advanced Usage

### Custom Command Registration

```python
from cli.commands.root import ui_gen_group
from cli.utils.command_registry import register_to_group
import click

# Register a new command to the root group
@register_to_group(ui_gen_group)
@click.command("custom")
@click.option("--param", help="Custom parameter")
def custom_command(param):
    """Custom command description."""
    click.echo(f"Custom command executed with param: {param}")

# Register a new command group
@register_to_group(ui_gen_group)
@click.group("custom-group")
def custom_group():
    """Custom command group."""
    pass

@register_to_group(custom_group)
@click.command("sub-command")
def sub_command():
    """Sub-command within custom group."""
    click.echo("Sub-command executed")
```

### Custom Result Formatting

```python
from cli.utils.result_formatter import ResultFormatter, ResultStyle
from dto.command_dto import CommandExecutionResult

# Create a custom result
result = CommandExecutionResult(
    success="True",
    command="claude mcp list",
    output="Server1: /path/to/server1.py\nServer2: /path/to/server2.py",
    error=""
)

# Basic formatting (context-aware)
formatter = ResultFormatter(verbose=False)
formatter(result)

# Verbose formatting with custom styles
formatter = ResultFormatter(verbose=True)
formatter(
    result,
    success_style=ResultStyle(fg="green", bold=True),
    command_style=ResultStyle(fg="blue", underline=True),
    output_style=ResultStyle(fg="cyan"),
    error_style=ResultStyle(fg="red", bold=True)
)
```

### Advanced Command Execution

```python
from gen_engine.generator import manual_generator
from utils.command_executor import subprocess_command_executor

# Use the generator with subprocess execution
@subprocess_command_executor(capture_output=False)
def custom_generator(server_name: str, prompt: str) -> List[str]:
    """Custom command generator."""
    return ["claude", f"/{server_name}:{prompt}", "Bash,Edit,Read"]

# Execute with timeout and error handling
result = custom_generator("my_server", "Generate a component")
```

### Context Usage

```python
import click
from cli.utils.command_registry import register_to_group
from cli.commands.root import ui_gen_group

@register_to_group(ui_gen_group)
@click.command("context-aware")
@click.pass_context
def context_aware_command(ctx):
    """Command that uses global context."""
    if ctx.obj.get('VERBOSE'):
        click.echo("Verbose mode enabled")
    else:
        click.echo("Standard mode")
```

## Output Formatting

### Basic Output

```bash
# Success case - shows only output
$ ui-gen mcp list-servers
Server1: /path/to/server1.py
Server2: /path/to/server2.py

# Error case - shows only error
$ ui-gen mcp add-server --server-name "test" --server-path "/invalid/path"
Error: Cannot register server: path does not exist → '/invalid/path'
```

### Verbose Output

```bash
# Verbose success case - shows all details with colors
$ ui-gen --verbose mcp list-servers
Successful: True
Command: claude mcp list
Output: Server1: /path/to/server1.py
        Server2: /path/to/server2.py
Error: None

# Verbose error case - shows all details with colors
$ ui-gen --verbose mcp add-server --server-name "test" --server-path "/invalid/path"
Successful: False
Command: claude mcp add test -- python /invalid/path
Output: None
Error: Cannot register server: path does not exist → '/invalid/path'
```

## Result Formatting Styles

The system supports customizable terminal styling:

```python
# Available colors
ClickColor = Literal[
    "black", "red", "green", "yellow", 
    "blue", "magenta", "cyan", "white"
]

# Style options
ResultStyle(
    fg="green",          # Foreground color
    bg="black",          # Background color  
    bold=True,           # Bold text
    underline=True       # Underlined text
)

# Default verbose styles
success_style = ResultStyle(fg="cyan")
command_style = ResultStyle(fg="yellow")
output_style = ResultStyle(fg="green")
error_style = ResultStyle(fg="red")
```

## Error Handling

The CLI provides comprehensive error handling across multiple layers:

### **Subprocess Execution Errors**
```python
# Command execution timeout
CommandExecutionResult(
    success="False",
    command="claude mcp add server_name -- python /path/to/server.py",
    output="",
    error="Command timed out after 120000ms"
)

# Claude CLI not found
CommandExecutionResult(
    success="False",
    command="claude mcp list",
    output="",
    error="Error: 'claude' CLI tool is not installed or not found in PATH"
)

# Command execution failure
CommandExecutionResult(
    success="False",
    command="claude mcp add invalid_server",
    output="",
    error="Command failed with exit code 1: Server validation failed"
)
```

### **File System Validation**
```python
# Path validation in MCP server registration
try:
    result = add_mcp_server("test_server", "/nonexistent/path.py")
except FileNotFoundError as e:
    # Error: "Cannot register server: path does not exist → '/nonexistent/path.py'"
    print(f"Registration failed: {e}")
```

### **Interactive Prompt Handling**
```python
# Missing parameter handling via Click prompts
@click.option("--server-name", prompt="Server name", help="Server identifier")
def command(server_name):
    # Click automatically prompts for missing required parameters
    # Handles KeyboardInterrupt gracefully for user cancellation
    pass
```

### **Generation Command Handling**
```python
# Mode selection handling
if mode == "auto":
    click.echo("Auto mode selected")
    # Auto generation logic
elif mode == "manual":
    click.echo("Manual mode selected")
    # Manual generation logic

# Tool validation
if not allowed_tools:
    click.echo("Using default tool configuration")
```

## Best Practices

1. **Command Organization**: Use command groups to organize related functionality
2. **Interactive Design**: Leverage prompts for required parameters to improve UX
3. **Verbose Support**: Always support verbose output for debugging and automation
4. **Error Messages**: Provide clear, actionable error messages
5. **Context Usage**: Use Click context for shared state across command hierarchy
6. **Auto-Registration**: Use the registration decorator for clean command organization
7. **Consistent Styling**: Use the ResultFormatter for consistent terminal output

## Extension Patterns

### Adding New Command Groups

```python
# 1. Create new command group
@register_to_group(ui_gen_group)
@click.group("new-group")
def new_group():
    """New command group description."""
    pass

# 2. Add commands to the group
@register_to_group(new_group)
@click.command("new-command")
@click.option("--param", help="Parameter description")
@click.pass_context
def new_command(ctx, param):
    """New command description."""
    # Command implementation
    pass
```

### Custom Formatters

```python
class CustomFormatter:
    @staticmethod
    def format_json(result: CommandExecutionResult):
        """Format result as JSON."""
        import json
        output = {
            "success": result.success,
            "command": result.command,
            "output": result.output,
            "error": result.error
        }
        click.echo(json.dumps(output, indent=2))
```

## File Structure

```
cli/
├── __init__.py                 # Package initialization (empty)
├── main.py                    # Main entry point and CLI bootstrap
├── commands/                  # Command implementations
│   ├── __init__.py           # Package initialization (empty)
│   ├── root.py               # Root command group definition
│   ├── mcp.py                # MCP server management commands
│   └── generate.py           # UI generation commands
└── utils/                     # CLI utilities and helpers
    ├── __init__.py           # Package initialization (empty)
    ├── command_registry.py   # Decorator-based command registration
    └── result_formatter.py   # Terminal output formatting system
```

## Integration Patterns

### With MCP Engine

```python
# Direct integration for server lifecycle management
from mcp_engine.mcp_registry import add_mcp_server, remove_mcp_server, list_mcp_servers

# CLI commands delegate to MCP engine functions
@click.command("add-server")
def add_mcp_server_cmd(server_name, server_path):
    result = add_mcp_server(server_name=server_name, server_path=server_path)
    ResultFormatter(verbose=ctx.obj.get('VERBOSE'))(result)
```

### With Generation Engine

```python
# Integration with generation engine for prompt execution
from gen_engine.generator import manual_generator

# Generate command integrates with generator functions
def generate(mode, server_name, server_prompt, user_prompt, allowed_tools):
    if mode == "manual":
        result = manual_generator(
            server_name=server_name,
            server_prompt=server_prompt,
            user_prompt=user_prompt,
            allowed_tools=allowed_tools
        )
```

### With Command Execution System

```python
# Integration with subprocess execution system
from utils.command_executor import subprocess_command_executor

# Automatic timeout and error handling for all command functions
@subprocess_command_executor(capture_output=False)
def manual_generator(server_name: str, server_prompt: str, user_prompt: str, allowed_tools: str) -> List[str]:
    prompt = f"/{server_name}:{server_prompt} (MCP) {user_prompt}"
    return ["claude", prompt, allowed_tools]
```

## File Structure

```
cli/
├── __init__.py                 # Package initialization
├── main.py                    # Main entry point and CLI bootstrap
├── commands/                  # Command implementations
│   ├── __init__.py           # Package initialization
│   ├── root.py               # Root command group with verbose flag
│   ├── mcp.py                # MCP server management commands
│   └── generate.py           # UI generation commands with Claude integration
└── utils/                     # CLI utilities and helpers
    ├── __init__.py           # Package initialization
    ├── command_registry.py   # Decorator-based command registration system
    └── result_formatter.py   # Terminal output formatting with styling
```

## Dependencies

- **Click**: Modern command-line interface framework (`click`)
- **Pydantic**: Data validation and settings management (`pydantic`)
- **Dataclasses**: Structured data objects for configuration
- **Typing**: Type annotations and validation (`typing`, `typing_extensions`)
- **MCP Engine**: Integration with MCP server management (`mcp_engine.mcp_registry`)
- **Generation Engine**: UI generation capabilities (`gen_engine.generator`)
- **DTO Module**: Structured data transfer objects (`dto.command_dto`)
- **Utils Module**: Command execution utilities (`utils.command_executor`)

## Integration Points

The CLI system provides comprehensive integration across the application stack:

1. **MCP Engine**: Direct integration for Claude Code server management operations
2. **Generation Engine**: Prompt composition and execution via Claude CLI integration
3. **Command Execution**: Subprocess management with timeout and error handling
4. **DTO System**: Structured result handling with `CommandExecutionResult` objects
5. **Terminal Interface**: Rich terminal output with color and formatting support
6. **File System**: Path validation and existence checking for server registration
7. **Claude Code CLI**: Native integration with Claude Code MCP protocol and tool restrictions

The CLI provides a robust, extensible interface for managing the entire UI generation and MCP server lifecycle with professional-grade terminal output, comprehensive error handling, and seamless integration across all system components.