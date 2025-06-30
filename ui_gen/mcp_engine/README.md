# MCP Engine

A factory system for building and managing FastMCP (Model Context Protocol) servers with integrated prompt generation capabilities.

## Overview

The MCP Engine provides a toolkit for creating MCP servers that leverage the structured prompt system from the prompt_engine. It handles server configuration, command execution, and prompt registration with built-in validation and error handling.

## Architecture

### Core Components

#### 1. **MCPFactory** (`mcp_factory.py`)
Factory pattern implementation for building and configuring FastMCP servers:

- **Server Construction**: Initializes FastMCP instances with custom dependencies
- **Prompt Integration**: Seamlessly integrates with PromptComposer for dynamic prompt assembly
- **Fluent API**: Supports method chaining for clean configuration syntax
- **Type Safety**: Full Pydantic validation for all inputs and configurations
- **Dual Layer Support**: Supports both frontend and backend generation prompts

**Key Methods:**
- `add_frontend_generation_prompt()`: Adds frontend-specific prompts using PromptComposer
- `add_backend_generation_prompt()`: Adds backend-specific prompts using PromptComposer
- `get_mcp_server()`: Returns the configured FastMCP instance

#### 2. **MCP Registry** (`mcp_registry.py`)
Command execution system for managing MCP servers via Claude Code CLI:

- **CLI Integration**: Built-in support for `claude mcp` commands
- **Server Management**: Add, remove, and list MCP servers
- **Path Validation**: Ensures server paths exist before registration
- **Subprocess Execution**: Decorated functions for structured command execution

**Key Functions:**
- `add_mcp_server(server_name, server_path)`: Registers a new MCP server
- `remove_mcp_server(server_name)`: Removes a registered MCP server  
- `list_mcp_servers()`: Lists all registered MCP servers

#### 3. **Built-in Server** (`builtin_mcp.py`)
Pre-configured server implementation:

- **Pre-configured Setup**: Out-of-the-box server with UI generation focus
- **Component Integration**: Uses TaskContext, Modality, TechConstraint, and OutputControl components
- **Framework Support**: Configured for modern web development frameworks

## Key Features

- **FastMCP Integration**: Native support for FastMCP server architecture
- **Prompt Engine Bridge**: Integration with structured prompt composition
- **Command Execution**: Subprocess decorator for MCP command handling
- **Type Safety**: Full Pydantic validation throughout the system
- **CLI Integration**: Built-in support for Claude Code CLI operations
- **Fluent Configuration**: Method chaining for clean server setup
- **Path Validation**: File existence checks before server registration

## Usage

### Basic Server Creation

```python
from mcp_engine.mcp_factory import MCPFactory
from prompt_engine.prompt_component import (
    TaskContextComponent,
    ModalityComponent,
    TechConstraintComponent,
    OutputControlComponent
)

# Create frontend server
mcp_server = (MCPFactory()
    .add_frontend_generation_prompt(
        name="ui_generator",
        description="Generates frontend UI from images",
        prompt_components=[
            TaskContextComponent.UI_GENERATION,
            ModalityComponent.IMAGE_TEXT,
            TechConstraintComponent.NEXTJS,
            OutputControlComponent.STRICT_COMPLIANCE
        ]
    )
    .get_mcp_server()
)

# Create backend server
backend_server = (MCPFactory()
    .add_backend_generation_prompt(
        name="api_generator", 
        description="Generates backend API implementations",
        prompt_components=[
            TaskContextComponent.UI_GENERATION,
        ]
    )
    .get_mcp_server()
)

# Start the server
if __name__ == "__main__":
    mcp_server.run()
```

### MCP Server Management

```python
from mcp_engine.mcp_registry import add_mcp_server, remove_mcp_server, list_mcp_servers

# Register a new MCP server with Claude Code
result = add_mcp_server(
    server_name="my_prompt_server",
    server_path="/path/to/my_server.py"
)

# List all registered servers
servers_result = list_mcp_servers()

# Remove a server
removal_result = remove_mcp_server("my_prompt_server")
```

### Built-in Server

```python
# Run the built-in server
python -m mcp_engine.builtin_mcp

# Or create a custom server
from mcp_engine.mcp_factory import MCPFactory
from prompt_engine.prompt_component import (
    TaskContextComponent,
    ModalityComponent,
    TechConstraintComponent,
    OutputControlComponent
)

server = (MCPFactory()
    .add_frontend_generation_prompt(
        name="ui_generator",
        description="UI generation system",
        prompt_components=[
            TaskContextComponent.UI_GENERATION,
            ModalityComponent.IMAGE_TEXT,
            TechConstraintComponent.NEXTJS,
            OutputControlComponent.STRICT_COMPLIANCE
        ]
    )
    .get_mcp_server()
)

if __name__ == "__main__":
    server.run()
```

### Factory with Dependencies

```python
from mcp_engine.mcp_factory import MCPFactory

# Create factory with custom dependencies
factory = MCPFactory(dependencies=["requests", "pydantic", "custom-package"])

server = (factory
    .add_frontend_generation_prompt(
        name="advanced_ui",
        description="Advanced UI generation with custom dependencies",
        prompt_components=[
            TaskContextComponent.UI_GENERATION,
            ModalityComponent.IMAGE_TEXT,
            TechConstraintComponent.NEXTJS
        ]
    )
    .get_mcp_server()
)
```

## Error Handling

The system provides comprehensive error handling:

### File System Validation
```python
# Path validation in mcp_registry
try:
    result = add_mcp_server("test_server", "/path/to/server.py")
    if result.success == "True":
        print("Server registered successfully")
except FileNotFoundError as e:
    print(f"Registration failed: {e}")
```

### Command Execution Handling
```python
# Subprocess execution through decorator
from mcp_engine.mcp_registry import list_mcp_servers

result = list_mcp_servers()  # Returns CommandExecutionResult

if result.success == "True":
    print("Command executed successfully")
    print(result.output)
else:
    print(f"Command failed: {result.error}")
```

### Prompt Composition
```python
# Server creation with prompt composition
server = (MCPFactory()
    .add_frontend_generation_prompt(
        name="ui_generator",
        description="UI generation server",
        prompt_components=[
            TaskContextComponent.UI_GENERATION,
            ModalityComponent.IMAGE_TEXT,
            TechConstraintComponent.NEXTJS
        ]
    )
    .get_mcp_server()
)
```

## Best Practices

1. **Server Lifecycle**: Always validate server paths before registration
2. **Dependency Management**: Specify all required dependencies in MCPFactory
3. **Prompt Composition**: Use appropriate prompt components for your use case
4. **Component Selection**: Choose components that match your generation requirements
5. **Error Handling**: Always check CommandExecutionResult.success before proceeding
6. **Server Configuration**: Configure servers with appropriate prompt components

## Integration Patterns

### With Prompt Engine

```python
# Leverage prompt composition for dynamic server configuration
from prompt_engine.prompt_composer import PromptComposer
from mcp_engine.mcp_factory import MCPFactory

components = [
    TaskContextComponent.UI_GENERATION,
    ModalityComponent.IMAGE_TEXT
]

# Direct prompt composition
frontend_prompt = PromptComposer.compose_frontend_prompt(components)

# Or use factory integration
server = (MCPFactory()
    .add_frontend_generation_prompt("dynamic", "Dynamic prompt", components)
    .get_mcp_server()
)
```


## File Structure

```
mcp_engine/
├── __init__.py                 # Package initialization (empty)
├── mcp_factory.py             # FastMCP server factory with fluent API
├── mcp_registry.py            # MCP server management via Claude Code CLI
├── builtin_mcp.py             # Pre-configured built-in server
└── README.md                  # This documentation
```

## Dependencies

- **FastMCP**: Core MCP server implementation (`mcp.server.fastmcp`)
- **Pydantic**: Data validation and settings management  
- **Pathlib**: File system path handling
- **Typing**: Type annotations and validation
- **Prompt Engine**: Structured prompt composition system
- **Utils**: Command execution utilities (`utils.command_executor`)

## Claude Code Integration

The MCP Engine integrates with Claude Code:

1. **Server Registration**: Registration with Claude Code CLI via `claude mcp add`
2. **Protocol Compliance**: MCP protocol compatibility through FastMCP
3. **CLI Integration**: Support for `claude mcp` commands (add, remove, list)
4. **Path Validation**: Ensures server files exist before registration