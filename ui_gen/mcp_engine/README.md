# MCP Engine

A **builder pattern factory system** implementing **dependency inversion principles** for FastMCP (Model Context Protocol) server construction and lifecycle management with type-safe prompt integration.

## Architecture Overview

The MCP Engine implements an **abstraction-first approach** where high-level server construction depends on interfaces (`PromptComponent`, `PromptComposer`) rather than concrete implementations, enabling dynamic server configuration and extensible prompt systems.

## Core Abstractions

### 1. **MCPFactory** (`mcp_factory.py`) - **Builder Pattern with Dependency Inversion**

**Core Abstraction**: Fluent API for FastMCP server construction
- **Interface Contract**: Builder pattern depending on `PromptComponent` and `PromptComposer` abstractions
- **Dependency Inversion**: Depends on prompt interfaces, not concrete prompt implementations
- **Extension Points**: Configurable dependencies and pluggable prompt composition strategies

**Key Interface Methods:**
- `add_frontend_generation_prompt(name, description, prompt_components: List[PromptComponent])`: Leverages `PromptComposer` abstraction
- `add_backend_generation_prompt(name, description, prompt_components: List[PromptComponent])`: Uses same abstraction layer
- `get_mcp_server() -> FastMCP`: Returns configured server instance

**Abstraction Benefits**:
- **Type Safety**: Pydantic validation with `PromptComponent` enum constraints
- **Composability**: Dynamic server configuration through component assembly
- **Extensibility**: New prompt types supported without factory changes

### 2. **MCP Registry** (`mcp_registry.py`) - **Command Execution Abstraction**

**Core Abstraction**: Server lifecycle management through standardized command execution
- **Interface Contract**: Functions decorated with `@subprocess_command_executor` for consistent execution patterns
- **Dependency Inversion**: Depends on `CommandExecutionResult` abstraction, not specific execution implementations
- **Extension Points**: Pluggable command execution with timeout and error handling

**Key Interface Functions:**
- `add_mcp_server(server_name: str, server_path: str) -> CommandExecutionResult`: File system validation + Claude CLI integration
- `remove_mcp_server(server_name: str) -> CommandExecutionResult`: Server deregistration with error handling
- `list_mcp_servers() -> CommandExecutionResult`: Server enumeration with structured output

**Abstraction Benefits**:
- **Consistent Interface**: All functions return `CommandExecutionResult` for uniform error handling
- **Validation Layer**: Path existence validation before Claude CLI invocation
- **Timeout Handling**: Configurable execution timeouts through decorator abstraction

### 3. **Built-in MCP Server** (`builtin_mcp.py`) - **Basic Implementation**

**Core Abstraction**: Pre-configured server demonstrating `MCPFactory` usage patterns
- **Interface Implementation**: Uses `MCPFactory` builder pattern with standard prompt components
- **Dependency on Abstractions**: Leverages `PromptComponent` enums and `PromptComposer` for configuration
- **Extension Example**: Shows how to create servers using the abstraction layer

**Configuration Pattern**:
- Single frontend generation prompt using `TaskContextComponent.UI_GENERATION`
- Demonstrates `MCPFactory` fluent API usage
- Serves as template for custom server implementations

### 4. **Powerful Built-in MCP Server** (`powerful_builtin_mcp.py`) - **Enterprise Implementation**

**Core Abstraction**: Comprehensive server showcasing full framework capabilities
- **Interface Utilization**: Extensive use of `MCPFactory` with multiple prompt component combinations
- **Abstraction Leverage**: Demonstrates composition of various `PromptComponent` types for specialized use cases
- **Scalability Pattern**: Shows how abstraction layer supports complex server configurations

**Architecture Demonstration**:
- **16 specialized prompts**: Each using different `PromptComponent` combinations
- **Multi-modal support**: `ModalityComponent.IMAGE_TEXT`, `ModalityComponent.SKETCH`, etc.
- **Technology constraints**: Various `TechConstraintComponent` configurations
- **Output control**: Different `OutputControlComponent` and `RefinementComponent` combinations

## Architectural Benefits

**Dependency Inversion Implementation**:
- **Factory Pattern**: `MCPFactory` depends on `PromptComponent` abstractions, not concrete component implementations
- **Command Abstraction**: Registry functions depend on `CommandExecutionResult` interface, not specific execution mechanisms
- **Composition Over Inheritance**: Server configuration through component composition rather than class hierarchies

**Extension Points**:
- **New Prompt Types**: Add new `PromptComponent` enums without modifying factory logic
- **Custom Servers**: Implement servers using `MCPFactory` abstraction without understanding internal composition
- **Execution Strategies**: Replace command execution implementation while maintaining `CommandExecutionResult` contract

**Type Safety & Validation**:
- **Compile-time Safety**: `PromptComponent` enum constraints prevent invalid configurations
- **Runtime Validation**: Pydantic validation ensures proper server construction
- **Interface Contracts**: Clear contracts between factory, registry, and execution layers

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
            ModalityComponent.IMAGE,
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
# Run the basic built-in server
python -m mcp_engine.builtin_mcp

# Run the powerful enterprise server (recommended)
python -m mcp_engine.powerful_builtin_mcp

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
            ModalityComponent.IMAGE,
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


## Powerful Built-in Server

The enterprise-grade server (`powerful_builtin_mcp.py`) provides 16 specialized prompts for comprehensive UI development:

### Available Prompts

1. **screenshot_text_to_compiled_ui** - Multi-modal input (image + text) to compiled Next.js components
2. **nextjs_image_to_component** - Generate components from UI screenshots
3. **nextjs_sketch_to_component** - Convert wireframes to components
4. **nextjs_spec_to_component** - Build from markdown specifications
5. **nextjs_component_library** - Create reusable component libraries
6. **nextjs_form_builder** - Generate dynamic forms from JSON schemas
7. **nextjs_accessibility_audit** - WCAG compliance and accessibility fixes
8. **nextjs_performance_optimizer** - Performance and bundle optimization
9. **nextjs_responsive_enhancer** - Responsive design capabilities
10. **nextjs_theme_generator** - Design systems and themes
11. **nextjs_test_generator** - Comprehensive test suites
12. **nextjs_error_boundary** - Robust error handling
13. **nextjs_i18n_setup** - Internationalization setup
14. **nextjs_migration_assistant** - Framework migration support
15. **nextjs_doc_generator** - Documentation and Storybook stories
16. **nextjs_automation_dashboard** - Admin panels and dashboards

### Usage

```python
# Run the powerful server
python -m mcp_engine.powerful_builtin_mcp

# Or import programmatically
from mcp_engine.powerful_builtin_mcp import mcp_server
mcp_server.run()
```

## File Structure

```
mcp_engine/
├── __init__.py                 # Package initialization (empty)
├── mcp_factory.py             # FastMCP server factory with fluent API
├── mcp_registry.py            # MCP server management via Claude Code CLI
├── builtin_mcp.py             # Basic pre-configured built-in server
├── powerful_builtin_mcp.py    # Enterprise server with 16 specialized prompts
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