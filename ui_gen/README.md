# UIGen - User Interface Generation Framework

A modular framework for structured prompt composition, MCP (Model Context Protocol) server management, and command-line automation with Claude Code integration.

## Overview

UIGen provides a foundation for building AI-powered development tools through three core engines:

- **Prompt Engine**: Type-safe prompt composition with modular components and stores
- **MCP Engine**: FastMCP server factory and registry for Claude Code integration  
- **CLI Engine**: Command-line interface built on Click framework with rich terminal output

Core architecture provides functional CLI and MCP management with prompt composition system.

## Architecture

UIGen consists of three main engines:

### Core Engines

1. **Prompt Engine** (`prompt_engine/`)
   - **Components**: Enum-based component system (`TaskContextComponent`, `ModalityComponent`, `TechConstraintComponent`, `OutputControlComponent`)
   - **Stores**: Abstract base class with specialized implementations for each component type
   - **Composer**: Dynamic prompt assembly engine with store registry

2. **MCP Engine** (`mcp_engine/`)
   - **Factory**: Fluent API for creating FastMCP servers with Pydantic validation
   - **Registry**: Server lifecycle management via Claude CLI integration
   - **Default Server**: Pre-configured server implementation

3. **CLI Engine** (`cli/`)
   - **Commands**: Root command group with MCP management and generation commands
   - **Utils**: Auto-registration decorators and result formatters

### Supporting Modules

4. **Generation Engine** (`gen_engine/`)
   - **Manual Generator**: Claude CLI command builder
   - **Auto Generator**: Placeholder implementation

5. **Data Transfer Objects** (`dto/`)
   - **CommandExecutionResult**: Structured command results
   - **ResultStyle**: Terminal formatting configuration

6. **Utilities** (`utils/`)
   - **Command Executor**: Subprocess decorator with timeout handling

## Installation & Setup

### Prerequisites

- **Python**: 3.12 or higher (required by setup.py)
- **Claude Code**: Required for MCP server integration and generation commands

### Installation

```bash
# Install dependencies
pip install -r requirements.txt

# Install package in development mode
pip install -e .

# Verify CLI installation
ui-gen --help
```

### Package Configuration

**Entry Point**: `ui-gen` command configured in setup.py as `cli.main:ui_gen_group`

**Dependencies**: 78 packages including:
- `click==8.2.1` (CLI framework)  
- `pydantic==2.11.5` (data validation)
- `mcp==1.9.3` (FastMCP integration)
- Additional packages for HTTP, AWS, ML, and development tools

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
    OutputControlComponent
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
│   └── default_mcp.py         # Default server (has issues)
├── gen_engine/                # Generation commands
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

1. **CLI → MCP Engine**: Server management via `mcp_registry` functions
2. **CLI → Generation Engine**: Command building via `generator` functions  
3. **MCP Factory → Prompt Engine**: Server creation with prompt components
4. **Command Executor → All**: Subprocess handling with structured results
5. **Result Formatter → CLI**: Terminal output with styling

**Author**: Nazar Lenyshyn (nleny@softserveinc.com)  
**Python Version**: 3.12+ required