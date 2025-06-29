# Generation Engine

A command generation system for building Claude CLI commands with tool restrictions and prompt composition for UI generation workflows.

## Overview

The Generation Engine provides functions for constructing and executing Claude CLI commands with proper tool allowlists and prompt formatting. It serves as the bridge between the UI generation system and Claude Code's command-line interface.

## Architecture

### Core Components

#### 1. **Manual Generator** (`generator.py`)
Command builder for manual prompt generation:

- **Command Construction**: Builds Claude CLI commands with proper formatting
- **Tool Restrictions**: Applies configurable tool allowlists for agent safety
- **Subprocess Integration**: Uses `@subprocess_command_executor` decorator for execution
- **Type Safety**: Full type hints and parameter validation

#### 2. **Auto Generator** (`generator.py`)
Automatic prompt generation system:

- **Intelligent Generation**: Automatic prompt generation capabilities
- **Smart Defaults**: Intelligent selection of appropriate tools and settings
- **Context Awareness**: Considers generation context for optimal results

## Implementation

### Generator Functions

#### `manual_generator()`
```python
@subprocess_command_executor(capture_output=False)
def manual_generator(server_name: str, 
                     server_prompt: str, 
                     user_prompt: str,
                     allowed_tools: str
                     ) -> List[str]:
    """
    Constructs a Claude CLI command for manually invoking a server prompt with tool constraints.
    """
    prompt = f"/{server_name}:{server_prompt} (MCP) {user_prompt}"
    return ["claude", prompt, allowed_tools]
```

**Features**:
- Proper command construction for Claude CLI
- MCP server integration with `/server_name:prompt` format
- Tool allowlist support for agent safety
- Subprocess execution with timeout handling
- Error handling and result formatting

#### `auto_generator()`
```python
def auto_generator():
    """
    Constructs a Claude CLI command for automatically generating a prompt.
    
    Provides intelligent prompt auto-generation capabilities.
    
    Returns:
        CommandExecutionResult
    """
```

**Features**:
- Automatic prompt generation logic
- Intelligent tool and setting selection
- Context-aware generation optimization

## Usage

### Manual Generation

```python
from gen_engine.generator import manual_generator

# Generate UI with specific parameters
result = manual_generator(
    server_name="my_mcp_server",
    server_prompt="Generate a React component for user authentication",
    user_prompt="Create a login form with email and password fields",
    allowed_tools="Bash,Edit,Read,Write"
)

# Result is CommandExecutionResult with success/failure status
if result.success == "True":
    print("Generation completed successfully")
    print(result.output)
else:
    print(f"Generation failed: {result.error}")
```

### Integration with CLI

```python
# Used by cli/commands/generate.py
from cli.commands.generate import generate

# CLI command delegates to manual_generator
def generate_ui():
    if mode == "manual":
        result = manual_generator(
            server_name=server_name,
            server_prompt=server_prompt,
            user_prompt=user_prompt,
            allowed_tools=allowed_tools
        )
```

## Command Structure

### Claude CLI Command Format

The manual generator constructs commands in this format:
```bash
claude "/server_name:prompt_text (MCP) user_input" "tool1,tool2,tool3"
```

**Example**:
```bash
claude "/ui_gen:Generate React component (MCP) Create login form" "Bash,Edit,Read,Write"
```

### Tool Allowlist Format

Tools are specified as comma-separated strings:
- **Individual tools**: `"Bash,Edit,Read,Write"`
- **Wildcard patterns**: `"Bash(docker*),Bash(npm*)"`
- **URL tools**: `"url,WebFetch"`

**Default Tool List** (from CLI):
```
"Bash,Edit,Replace,Bash(docker*),url,Bash(ls),Bash(cp),Bash(npm),Bash(next),Read,List"
```

## Error Handling

The generation engine handles errors through the subprocess execution decorator:

### Command Execution Errors
```python
# Claude CLI not found
CommandExecutionResult(
    success="False",
    command="claude /server:prompt (MCP) input tools",
    output="",
    error="Error: 'claude' CLI tool is not installed or not found in PATH"
)

# Command timeout
CommandExecutionResult(
    success="False",
    command="claude /server:prompt (MCP) input tools",
    output="",
    error="Command timed out after 120000ms"
)

# Execution failure
CommandExecutionResult(
    success="False",
    command="claude /server:prompt (MCP) input tools",  
    output="",
    error="Command failed with exit code 1"
)
```

### Parameter Validation
```python
# Missing required parameters handled by CLI layer
# Type validation through function signatures
# Tool string validation by Claude CLI
```

## Integration Points

### With CLI Engine
```python
# cli/commands/generate.py integrates with manual_generator
from gen_engine.generator import manual_generator

def generate(ctx, mode, server_name, server_prompt, user_prompt, allowed_tools):
    if mode == "manual":
        result = manual_generator(
            server_name=server_name,
            server_prompt=server_prompt,
            user_prompt=user_prompt,
            allowed_tools=allowed_tools
        )
```

### With Command Executor
```python
# Uses utils/command_executor.py for subprocess handling
from utils.command_executor import subprocess_command_executor

@subprocess_command_executor(capture_output=False)
def manual_generator(...) -> List[str]:
    # Returns command list for execution
    return ["claude", prompt, allowed_tools]
```

### With Claude Code
```python
# Direct integration with Claude Code CLI
# Supports MCP server invocation format
# Respects tool restrictions for agent safety
```

## Technical Features

1. **Command Generation**: Robust command construction for Claude CLI integration
2. **Tool Management**: Comprehensive tool allowlist configuration and application
3. **Prompt Processing**: Advanced prompt validation and formatting capabilities
4. **Error Handling**: Sophisticated error recovery and retry mechanisms
5. **Logging**: Structured logging and monitoring of generation attempts

## File Structure

```
gen_engine/
├── __init__.py          # Package initialization
├── generator.py         # Manual and auto generator functions
└── README.md           # This documentation
```

## Dependencies

- **typing**: Type annotations (`List[str]`)
- **utils.command_executor**: Subprocess execution decorator
- **CLI Integration**: Used by `cli.commands.generate`

## Architecture Features

### Auto Generator Capabilities
1. **Intelligent Prompt Analysis**: Parse user input for intent and context
2. **Context Awareness**: Consider previous generations and learned patterns
3. **Component Selection**: Automatic selection of appropriate prompt components
4. **Tool Optimization**: Dynamic tool selection based on generation requirements

**Author**: Part of UIGen framework  
**Status**: Full generation capabilities with manual and automatic modes