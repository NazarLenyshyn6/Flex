# Prompt Engine

A **component-based composition system** implementing **dependency inversion principles** for type-safe, modular prompt assembly with extensible architecture and strong abstraction layers.

## Architecture Overview  

The Prompt Engine implements **interface-driven design** where the composition engine (`PromptComposer`) depends on component abstractions (`PromptComponent`) and storage interfaces (`PromptStore<T>`), enabling dynamic prompt assembly without tight coupling to specific implementations.

## Core Abstractions

### 1. **PromptComponent** (`prompt_component.py`) - **Type-Safe Component Taxonomy**

**Core Abstraction**: Enumeration-based interface hierarchy for prompt component classification
- **Interface Contract**: Base enum serving as marker interface for all prompt component types
- **Dependency Inversion**: All components depend on abstract `PromptComponent` base, not concrete implementations
- **Extension Points**: New component categories via enum inheritance without breaking existing code

**Component Hierarchy**:
- **`PromptComponent`**: Abstract base enum establishing the component contract
- **`TaskContextComponent`**: WHAT to generate (UI generation, bug fixes, themes, etc.)
- **`ModalityComponent`**: HOW input is provided (text, image, sketch, JSON schema, etc.)
- **`TechConstraintComponent`**: WHICH technologies to use (React, Vue, Tailwind, TypeScript, etc.)
- **`OutputControlComponent`**: HOW to format output (compliance, comments, testing, etc.)
- **`RefinementComponent`**: WHAT improvements to apply (accessibility, layout, performance, etc.)

**Abstraction Benefits**:
- **Type Safety**: Compile-time validation prevents invalid component combinations
- **Extensibility**: New component types added without modifying composition logic
- **Interface Segregation**: Each component category has focused, single-responsibility interface


### 2. **PromptStore<T>** (`prompt_store.py`) - **Generic Storage Abstraction**

**Core Abstraction**: Generic abstract base class for type-safe prompt storage
- **Interface Contract**: Abstract methods defining CRUD operations with type parameter constraints
- **Dependency Inversion**: Stores depend on `PromptComponent` abstraction, not specific component types
- **Extension Points**: Subclasses implement `prompt_component()` method to specify their managed component type

**Generic Interface Definition**:
```python
class PromptStore(ABC, Generic[T]):
    @classmethod
    @abstractmethod
    def prompt_component(cls) -> Type[PromptComponent]:
        """Contract: subclasses must declare their managed component type"""
    
    # CRUD interface with type safety
    @classmethod
    def get_frontend_prompt(cls, prompt_component: T) -> str
    @classmethod
    def register_frontend_prompt(cls, prompt_component: T, prompt: str) -> None
```

**Abstraction Benefits**:
- **Type Parameter Constraints**: Generic `T` ensures store implementations are type-safe
- **Interface Enforcement**: ABC pattern requires implementation of core methods
- **Dual Target Support**: Separate frontend/backend prompt storage with consistent interface
- **Validation Layer**: Component type validation at both registration and retrieval

### 3. **PromptComposer** (`prompt_composer.py`) - **Registry-Based Assembly Engine**

**Core Abstraction**: Central orchestrator implementing registry pattern for dynamic prompt composition
- **Interface Contract**: Stateless composition engine depending on registered `PromptStore<T>` implementations
- **Dependency Inversion**: Depends on `PromptComponent` and `PromptStore` abstractions, not concrete store implementations
- **Extension Points**: Store registry allows pluggable storage strategies without modifying composition logic

**Registry Interface**:
```python
class PromptComposer:
    @classmethod
    def register_prompt_store(cls, component_type: Type[PromptComponent], store_type: Type[PromptStore])
    
    @classmethod
    def compose_frontend_prompt(cls, components: List[PromptComponent]) -> str
    
    @classmethod  
    def compose_backend_prompt(cls, components: List[PromptComponent]) -> str
```

**Abstraction Benefits**:
- **Registry Pattern**: Loose coupling between composer and stores through registration mechanism
- **Type Safety**: Component type validation ensures only valid stores are registered
- **Composition Strategy**: Aggregates prompts from multiple stores based on component types
- **Stateless Design**: No internal state, enabling thread-safe operations

### 4. **Specialized Prompt Stores** (`prompt_stores/`) - **Concrete Implementations**

**Core Abstraction**: Type-specific implementations of `PromptStore<T>` interface demonstrating extension patterns
- **Interface Implementation**: Each store implements `PromptStore<T>` contract for a specific component type
- **Dependency Compliance**: All stores depend on `PromptComponent` abstraction and implement required abstract methods
- **Extension Examples**: Show how to create new stores following the established abstraction patterns

**Store Implementations**:
- **`TaskContextStore(PromptStore[TaskContextComponent])`**: Manages WHAT to generate prompts
- **`ModalityStore(PromptStore[ModalityComponent])`**: Handles HOW input is provided prompts  
- **`TechConstraintStore(PromptStore[TechConstraintComponent])`**: Manages WHICH technologies prompts
- **`OutputControlStore(PromptStore[OutputControlComponent])`**: Controls HOW to format output prompts
- **`RefinementStore(PromptStore[RefinementComponent])`**: Manages WHAT improvements prompts

**Implementation Pattern**:
```python
class TaskContextStore(PromptStore[TaskContextComponent]):
    @classmethod
    def prompt_component(cls) -> Type[TaskContextComponent]:
        return TaskContextComponent  # Type constraint enforcement
    
    # Inherited CRUD methods with type safety for TaskContextComponent
```

## Architectural Benefits

**Dependency Inversion Implementation**:
- **Interface Dependencies**: `PromptComposer` depends on `PromptComponent` and `PromptStore<T>` abstractions
- **Extension Without Modification**: New component types and stores added without changing composition logic
- **Pluggable Architecture**: Store registry enables runtime configuration of storage strategies

**Type Safety & Validation**:
- **Compile-time Safety**: Generic type parameters and enum constraints prevent invalid configurations
- **Runtime Validation**: ABC enforcement ensures proper interface implementation
- **Type Parameter Constraints**: `PromptStore<T>` generic ensures stores manage only their declared component types

**Separation of Concerns**:
- **Component Definition**: `PromptComponent` hierarchy focuses solely on taxonomy
- **Storage Responsibility**: `PromptStore<T>` implementations handle persistence concerns  
- **Composition Logic**: `PromptComposer` focuses purely on assembly strategy
- **Registry Management**: Clear separation between registration and composition operations

## Usage

### Basic Prompt Composition

```python
from prompt_engine.prompt_composer import PromptComposer
from prompt_engine.prompt_component import (
    TaskContextComponent,
    ModalityComponent,
    TechConstraintComponent,
    OutputControlComponent,
    RefinementComponent
)

# Frontend composition
frontend_components = [
    TaskContextComponent.UI_GENERATION,
    ModalityComponent.IMAGE,
    TechConstraintComponent.REACT,
    OutputControlComponent.STRICT_COMPLIANCE,
    RefinementComponent.FIX_A11Y
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
│   ├── output_control_store.py # Output control and compliance prompts
│   └── refinement_store.py   # Post-generation improvement prompts
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