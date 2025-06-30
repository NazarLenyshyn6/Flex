# Prompt Engine

A modular prompt composition system for building dynamic, structured prompts with type-safe component architecture for code generation tasks.

## Overview

The Prompt Engine provides a toolkit for creating modular, composable prompt systems. It uses a strongly-typed architecture with component-based prompt assembly, allowing for flexible and reusable prompt configurations.

## Architecture

### Core Components

#### 1. **PromptComponent** (`prompt_component.py`)
Enumeration-based system for defining prompt component types:

- **Base Interface**: Common marker interface for all prompt components
- **Task Context**: High-level task or problem context specification
- **Modality**: Input data interpretation and parsing specifications
- **Tech Constraints**: Technical or architectural constraints for output
- **Output Control**: Final controlling layer with strict compliance rules


#### 2. **PromptStore** (`prompt_store.py`)
Abstract base class for managing frontend and backend prompt strings:

- **Type Safety**: Generic implementation with prompt component validation
- **Dual Storage**: Separate frontend and backend prompt registries
- **CRUD Operations**: Registration, retrieval, and removal of prompts
- **Subclass Enforcement**: Ensures proper store implementation via ABC mechanisms

**Key Methods:**
- `register_frontend_prompt()`: Registers frontend-specific prompts
- `register_backend_prompt()`: Registers backend-specific prompts
- `get_frontend_prompt()`: Retrieves frontend prompts with validation
- `get_backend_prompt()`: Retrieves backend prompts with validation

#### 3. **PromptComposer** (`prompt_composer.py`)
Dynamic prompt assembly engine with modular architecture:

- **Component Aggregation**: Combines individual prompt components into complete prompts
- **Store Registry**: Manages registration and retrieval of specialized prompt stores
- **Validation System**: Type checking for components and stores
- **Dual Composition**: Supports both frontend and backend prompt assembly

**Key Methods:**
- `register_prompt_store()`: Associates component types with their stores
- `compose_frontend_prompt()`: Assembles complete frontend prompts
- `compose_backend_prompt()`: Assembles complete backend prompts

#### 4. **Specialized Prompt Stores** (`prompt_stores/`)
Type-specific implementations for each component category:

- **TaskContextStore**: Manages task context prompts (UI generation focus)
- **ModalityStore**: Handles input modality specifications
- **TechConstraintStore**: Manages technical constraint prompts
- **OutputControlStore**: Controls output compliance and formatting rules

## Key Features

- **Modular Architecture**: Component-based prompt building with clear separation of concerns
- **Type Safety**: Full validation throughout the system using ABC patterns and type hints
- **Dual Target Support**: Separate frontend and backend prompt composition
- **Extensible Design**: Easy addition of new component types and stores
- **Strongly Typed**: Enum-based components for explicit configuration
- **Registry Pattern**: Centralized management of prompt stores and components
- **Validation Layer**: Comprehensive error handling and type checking

## Usage

### Basic Prompt Composition

```python
from prompt_engine.prompt_composer import PromptComposer
from prompt_engine.prompt_component import (
    TaskContextComponent,
    ModalityComponent,
    TechConstraintComponent,
    OutputControlComponent
)

# Frontend composition
frontend_components = [
    TaskContextComponent.UI_GENERATION,
    ModalityComponent.IMAGE_TEXT,
    TechConstraintComponent.NEXTJS,
    OutputControlComponent.STRICT_COMPLIANCE
]
frontend_prompt = PromptComposer.compose_frontend_prompt(frontend_components)

# Backend composition
backend_components = [
    TaskContextComponent.UI_GENERATION,
]
backend_prompt = PromptComposer.compose_backend_prompt(backend_components)
```

### Custom Prompt Store Registration

```python
from prompt_engine.prompt_composer import PromptComposer
from prompt_engine.prompt_store import PromptStore
from prompt_engine.prompt_component import PromptComponent
from enum import auto
from typing import Dict, Type

# Create custom component type
class CustomComponent(PromptComponent):
    CUSTOM_TASK = auto()

# Create custom store
class CustomStore(PromptStore[CustomComponent]):
    _frontend_prompt_store: Dict[CustomComponent, str] = {}
    _backend_prompt_store: Dict[CustomComponent, str] = {}
    
    @classmethod
    def prompt_component(cls) -> Type[CustomComponent]:
        return CustomComponent

# Register the store
PromptComposer.register_prompt_store(CustomComponent, CustomStore)

# Register prompts
CustomStore.register_frontend_prompt(
    CustomComponent.CUSTOM_TASK,
    "Custom frontend prompt content"
)
```

### Working with Individual Stores

```python
from prompt_engine.prompt_stores.task_context_store import TaskContextStore
from prompt_engine.prompt_component import TaskContextComponent

# TaskContextStore provides frontend and backend prompts
frontend_prompt = TaskContextStore.get_frontend_prompt(TaskContextComponent.UI_GENERATION)
backend_prompt = TaskContextStore.get_backend_prompt(TaskContextComponent.UI_GENERATION)

# Register additional prompts
TaskContextStore.register_frontend_prompt(
    TaskContextComponent.UI_GENERATION,
    "Custom frontend prompt content..."
)

# View all registered prompts
frontend_prompts = TaskContextStore.frontend_prompt_store()
backend_prompts = TaskContextStore.backend_prompt_store()

# Working with other stores
from prompt_engine.prompt_stores.modality_store import ModalityStore
from prompt_engine.prompt_component import ModalityComponent

# Access modality prompts
frontend_prompt = ModalityStore.get_frontend_prompt(ModalityComponent.IMAGE_TEXT)
```

### Component Validation

```python
from prompt_engine.prompt_component import TaskContextComponent, ModalityComponent

# Components must be proper enum values
try:
    components = [
        TaskContextComponent.UI_GENERATION,
        ModalityComponent.IMAGE_TEXT
    ]
    prompt = PromptComposer.compose_frontend_prompt(components)
except TypeError as e:
    print(f"Validation error: {e}")
```

### Dynamic Store Management

```python
from prompt_engine.prompt_composer import PromptComposer
from prompt_engine.prompt_component import TaskContextComponent

# View registered stores
stores = PromptComposer.prompt_stores()

# Remove a store (advanced usage)
PromptComposer.remove_prompt_store(TaskContextComponent)

# Re-register if needed
from prompt_engine.prompt_stores.task_context_store import TaskContextStore
PromptComposer.register_prompt_store(TaskContextComponent, TaskContextStore)
```

## Error Handling

The system provides comprehensive error handling:

### Component Validation
```python
# Component type validation
try:
    components = [
        TaskContextComponent.UI_GENERATION,
        ModalityComponent.IMAGE_TEXT
    ]
    prompt = PromptComposer.compose_frontend_prompt(components)
except TypeError as e:
    print(f"Validation error: {e}")
```

### Store Registration
```python
# Store registration validation
try:
    class CustomComponent(PromptComponent):
        NEW_TYPE = auto()
    PromptComposer.compose_frontend_prompt([CustomComponent.NEW_TYPE])
except KeyError as e:
    print(f"Store not registered: {e}")
```

### Type Validation in Stores
```python
# Component type matching
try:
    TaskContextStore.get_frontend_prompt(TaskContextComponent.UI_GENERATION)
except TypeError as e:
    print(f"Type validation: {e}")
```

## Best Practices

1. **Component Design**: Create focused, single-purpose component types
2. **Store Implementation**: Always implement both frontend and backend stores
3. **Validation**: Leverage the built-in validation for type safety
4. **Composition**: Use the composer for all prompt assembly operations
5. **Registration**: Register all stores at module initialization time

## Integration Patterns

### With MCP Engine

```python
# Direct integration with MCP Factory
from mcp_engine.mcp_factory import MCPFactory
from prompt_engine.prompt_composer import PromptComposer
from prompt_engine.prompt_component import (
    TaskContextComponent,
    ModalityComponent,
    TechConstraintComponent
)

components = [
    TaskContextComponent.UI_GENERATION,
    ModalityComponent.IMAGE_TEXT,
    TechConstraintComponent.NEXTJS
]

# Use prompt engine components in MCP factory
mcp_server = (MCPFactory()
    .add_frontend_generation_prompt(
        name="ui_generator",
        description="Generates UI from prompts",
        prompt_components=components
    )
    .get_mcp_server()
)
```

### Custom Prompt Assembly

```python
# Build complex prompts with multiple component categories
def build_comprehensive_prompt():
    task_components = [TaskContextComponent.UI_GENERATION]
    modality_components = [ModalityComponent.IMAGE_TEXT]
    tech_components = [TechConstraintComponent.NEXTJS]
    control_components = [OutputControlComponent.STRICT_COMPLIANCE]
    
    all_components = task_components + modality_components + tech_components + control_components
    
    return PromptComposer.compose_frontend_prompt(all_components)
```

## File Structure

```
prompt_engine/
├── __init__.py                 # Package initialization
├── prompt_component.py         # Component enumerations and base classes
├── prompt_store.py            # Abstract base class for prompt storage
├── prompt_composer.py         # Dynamic prompt assembly engine
├── prompt_stores/             # Specialized store implementations
│   ├── __init__.py           # Store package initialization
│   ├── task_context_store.py # Task context prompt management
│   ├── modality_store.py     # Input modality prompt management
│   ├── tech_constraint_store.py # Technical constraint prompts
│   └── output_control_store.py # Output control and compliance prompts
└── README.md                  # This documentation
```

## Dependencies

- **typing, typing_extensions**: Type annotations and validation
- **abc**: Abstract base class functionality
- **enum**: Enumeration support for component definitions  
- **inspect**: Runtime introspection for store validation

## Implementation Notes

### Component Lifecycle

1. **Component Definition**: Enums define available component types
2. **Store Implementation**: Specialized stores implement prompt storage  
3. **Store Registration**: Stores auto-register with composer
4. **Prompt Registration**: Individual prompts register with stores
5. **Composition**: Complete prompts assembled from registered components