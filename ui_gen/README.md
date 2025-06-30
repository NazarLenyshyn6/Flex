# ui-gen - User Interface Generation Framework

A modular framework for structured prompt composition, MCP (Model Context Protocol) server management, and command-line automation with Claude Code integration.

## Overview

ui-gen provides a foundation for building AI-powered development tools through three core engines:

- **Prompt Engine**: Type-safe prompt composition with modular components and stores
- **MCP Engine**: FastMCP server factory and registry for Claude Code integration  
- **CLI Engine**: Command-line interface built on Click framework with rich terminal output

**⚠️ Critical Dependency**: ui-gen requires Claude Code CLI for all operations. Without working Claude Code, this framework provides zero functionality.

Core architecture provides functional CLI and MCP management with prompt composition system.

## Installation & Setup

### ⚠️ CRITICAL: Claude Code Required

**ui-gen framework is entirely dependent on Claude Code CLI**. All MCP operations, generation commands, and prompt execution require Claude Code to be properly installed and configured.

### Prerequisites

- **Python**: 3.12 or higher (required by setup.py)
- **Claude Code CLI**: **ABSOLUTELY REQUIRED** - The entire framework is built around Claude Code integration and will not work without it

### Complete Setup Process

#### 1. Environment Setup
Ensure Python 3.12+ and pip are installed on your system.

#### 2. Claude Code Installation & Configuration (CRITICAL STEP)
**This is the most important step - the entire framework depends on this being correct.**

1. **Install Claude Code CLI**:
   - Visit: https://docs.anthropic.com/claude/docs/claude-code
   - Follow the official installation instructions for your platform
   - Complete the authentication setup with your Anthropic API key

2. **Verify Claude Code Installation**:
   ```bash
   # Test basic functionality
   claude --help
   
   # Test authentication (should not show auth errors)
   claude --version
   
   # Test MCP functionality specifically
   claude mcp --help
   claude mcp list
   ```

3. **Critical Configuration Check**:
   ```bash
   # This command MUST work for ui-gen to function
   # If this fails, ui-gen will not work at all
   claude mcp list
   ```

   **Expected output**: Either a list of servers or "No servers configured"
   **Failure signs**: Authentication errors, command not found, permission errors

4. **Troubleshoot Claude Code Issues**:
   - Ensure API key is properly configured
   - Check permissions and network connectivity
   - Test with simple commands before proceeding

**DO NOT PROCEED** until `claude mcp list` works correctly.

#### 3. Project Dependencies
Install all required dependencies (78 packages total):
```bash
# Core dependencies include:
# - click==8.2.1 (CLI framework)
# - pydantic==2.11.5 (data validation)
# - mcp==1.9.3 (FastMCP integration)
# - Additional packages for HTTP, AWS, ML, and development tools
pip install -r requirements.txt
```

#### 4. Development Installation
```bash
# Install in editable mode for development
pip install -e .

# This creates the 'ui-gen' command entry point
# configured in setup.py as cli.main:ui_gen_group
```

#### 5. Verify Complete Installation
```bash
# Test CLI functionality
ui-gen --help
ui-gen --verbose --help

# CRITICAL: Test MCP commands (these MUST work)
ui-gen mcp --help
ui-gen mcp list-servers

# Test generation commands
ui-gen generate --help

# Full integration test - this should complete without errors
ui-gen --verbose mcp list-servers
```

**If any of these commands fail**, the problem is most likely with Claude Code configuration, not ui-gen itself.

### Package Configuration

**Entry Point**: `ui-gen` command configured in setup.py as `cli.main:ui_gen_group`

**Dependencies**: 78 packages including:
- `click==8.2.1` (CLI framework)  
- `pydantic==2.11.5` (data validation)
- `mcp==1.9.3` (FastMCP integration)
- Additional packages for HTTP, AWS, ML, and development tools

## Architecture

ui-gen implements a **dependency inversion architecture** with three core engines built on abstraction layers:

### Core Engines

1. **Prompt Engine** (`prompt_engine/`) - **Component-Based Prompt Assembly**
   - **PromptComponent Interface**: Abstract enum base for type-safe component taxonomy
   - **PromptStore<T> Abstraction**: Generic storage layer with frontend/backend separation
   - **PromptComposer**: Registry-based assembly engine for dynamic prompt composition
   - **Specialized Stores**: Type-specific implementations (`TaskContextStore`, `ModalityStore`, `TechConstraintStore`, `OutputControlStore`, `RefinementStore`)

2. **MCP Engine** (`mcp_engine/`) - **Server Factory & Lifecycle Management**
   - **MCPFactory**: Builder pattern for FastMCP server configuration with fluent API
   - **MCP Registry**: Server lifecycle management through Claude Code CLI integration
   - **Built-in MCP Server**: Basic pre-configured server with essential UI generation capabilities

3. **CLI Engine** (`cli/`) - **Command Interface & Execution**
   - **Command Groups**: Hierarchical command structure with auto-registration
   - **Result Formatting**: Structured output with verbose/concise modes and terminal styling
   - **Interactive Workflows**: Parameter prompting with validation and error handling

### Supporting Modules

4. **Generation Engine** (`gen_engine/`) - **Command Generation & Execution**
   - **Manual Generator**: Claude CLI command builder with MCP server integration and tool restrictions
   - **Auto Generator**: Placeholder for future intelligent generation capabilities

5. **Data Transfer Objects** (`dto/`) - **Structured Communication**
   - **CommandExecutionResult**: Immutable result wrapper for standardized subprocess output
   - **ResultStyle**: Terminal styling configuration with color and formatting options

6. **Utilities** (`utils/`) - **Infrastructure Services**
   - **subprocess_command_executor**: Decorator pattern for timeout-aware command execution with structured error handling


## Usage

### CLI Commands

```bash
# Main command with global verbose flag
ui-gen --help
ui-gen --verbose [subcommand]

# MCP server management
ui-gen mcp add-server --server-name "name" --server-path "/path/to/server.py"
ui-gen mcp remove-server --server-name "name"
ui-gen mcp list-servers

# Generation commands
ui-gen generate --mode manual --server-name "server" --server-prompt "prompt" --user-prompt "input" --allowed-tools "tools"
ui-gen generate --mode auto  # Shows "under development" message
```

### Prompt Composition

```python
from prompt_engine.prompt_composer import PromptComposer
from prompt_engine.prompt_component import (
    TaskContextComponent,
    ModalityComponent,
    TechConstraintComponent,
    OutputControlComponent,
    RefinementComponent
)

# Compose prompts with registered components
components = [TaskContextComponent.UI_GENERATION]
frontend_prompt = PromptComposer.compose_frontend_prompt(components)
backend_prompt = PromptComposer.compose_backend_prompt(components)
```

### MCP Server Creation

```python
from mcp_engine.mcp_factory import MCPFactory

# Create MCP server with prompt components
server = (MCPFactory()
    .add_frontend_generation_prompt(
        name="ui_generator",
        description="Generate UI components",
        prompt_components=[TaskContextComponent.UI_GENERATION]
    )
    .get_mcp_server()
)

# Run server
if __name__ == "__main__":
    server.run()
```

### Command Execution

```python
from utils.command_executor import subprocess_command_executor

# Subprocess command execution
@subprocess_command_executor(capture_output=True)
def my_command() -> List[str]:
    return ["echo", "hello world"]

result = my_command()  # Returns CommandExecutionResult
```


## Module Documentation

Individual module documentation:

- **[Prompt Engine](prompt_engine/README.md)**: Component-based prompt composition
- **[MCP Engine](mcp_engine/README.md)**: FastMCP server factory and registry  
- **[CLI Engine](cli/README.md)**: Command-line interface and utilities

## File Structure

```
ui_gen/
├── README.md                   # This file
├── setup.py                   # Package configuration
├── requirements.txt            # Dependencies (78 packages)
├── cli/                       # Command-line interface
│   ├── README.md              # CLI documentation
│   ├── main.py                # Entry point
│   ├── commands/              # Command implementations
│   └── utils/                 # CLI utilities
├── prompt_engine/             # Prompt composition system
│   ├── README.md              # Prompt engine documentation
│   ├── prompt_component.py    # Component enumerations
│   ├── prompt_composer.py     # Assembly engine
│   ├── prompt_store.py        # Abstract storage base
│   └── prompt_stores/         # Component-specific stores
├── mcp_engine/                # MCP server management
│   ├── README.md              # MCP engine documentation
│   ├── mcp_factory.py         # Server factory
│   ├── mcp_registry.py        # Server lifecycle
│   └── builtin_mcp.py         # Basic built-in MCP server
├── gen_engine/                # Generation commands
│   ├── README.md              # Generation engine documentation
│   └── generator.py           # Manual/auto generators
├── dto/                       # Data transfer objects
│   └── command_dto.py         # Result structures
└── utils/                     # Shared utilities
    └── command_executor.py    # Subprocess decorator
```

## Dependencies

Core dependencies from requirements.txt:
- **click==8.2.1**: CLI framework
- **pydantic==2.11.5**: Data validation  
- **mcp==1.9.3**: FastMCP integration
- **typing-extensions**: Extended type hints
- Additional packages for HTTP, AWS, ML, and development

## Integration Points

The architecture demonstrates **dependency inversion** through these abstraction-based integrations:

1. **CLI → MCP Engine**: Command layer depends on `MCPFactory` and registry abstractions, not concrete implementations
2. **CLI → Generation Engine**: Interface layer uses `subprocess_command_executor` abstraction for consistent execution patterns
3. **MCP Factory → Prompt Engine**: Builder depends on `PromptComponent` and `PromptComposer` interfaces, enabling dynamic server configuration
4. **Prompt Composer → Prompt Stores**: Assembly engine depends on `PromptStore<T>` abstraction, not specific store implementations
5. **All Modules → Command Execution**: Standardized through `CommandExecutionResult` contract and decorator pattern

## User Responsibilities

**All Claude Code setup, environment configuration, and MCP server management is entirely the user's responsibility.**

### Critical User Requirements:

#### Claude Code Responsibility:
- **Authentication**: Proper API key configuration and Claude Code login setup
- **Network Access**: Ensuring Claude Code can connect to Anthropic's services
- **Permissions**: Correct file system and CLI permissions for Claude Code operation
- **Version Compatibility**: Using a compatible Claude Code version

#### Configuration Management Responsibility:
- **Environment Setup**: Managing environment variables, dependency versions, and system configuration
- **MCP Registration**: Ensuring proper MCP server registration with correct server names
- **Path Accuracy**: Providing accurate server paths that exist and are accessible
- **Parameter Validation**: Supplying correct server names, prompts, and tool configurations

### Failure Responsibility & User Fault:

**95% of ui-gen failures are Claude Code configuration issues.** Common failure scenarios:

1. **`ui-gen mcp list-servers` fails** → User's Claude Code MCP configuration is broken
2. **`ui-gen generate` fails** → User's Claude Code CLI is not properly set up
3. **Authentication errors** → User's API key or login configuration is incorrect
4. **Server not found errors** → User provided wrong server names or paths
5. **Command timeouts** → User's network or Claude Code connectivity issues

### Explicit User Fault Conditions:

**The following failures are ENTIRELY the user's fault:**
- **Wrong server names**: Providing server names that don't exist or are misspelled
- **Invalid file paths**: Specifying paths to servers that don't exist or are inaccessible  
- **Incorrect tool configurations**: Supplying malformed or invalid tool allowlists
- **Broken Claude Code setup**: Having non-functional Claude Code authentication or installation
- **Network/permission issues**: Claude Code blocked by firewalls, permissions, or network policies
- **Parameter mistakes**: Typos in commands, incorrect flags, or malformed inputs

**Warning**: The framework will fail silently or with cryptic errors when given incorrect parameters. It is designed for automation and assumes all user inputs are correct.

**Responsibility Disclaimer**: If the system fails due to user-provided incorrect configuration, wrong parameters, invalid paths, or broken Claude Code setup, this is entirely the user's fault. Do not troubleshoot ui-gen internals - verify your inputs and Claude Code configuration first.
