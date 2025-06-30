"""
This module defines the `PromptComposer` class, a dynamic prompt assembly engine that combines individual
prompt components using a modular, strongly-typed architecture.

Each component of a prompt (e.g., task context, input modality, tech constraints, etc.)
is registered and stored via specialized `PromptStore` subclasses. The `PromptComposer`
uses these stores to compose complete prompts tailored to specific frontend or backend
scenarios.

Supports:
- Registering and retrieving prompt stores for each component category
- Validating component types and prompt store subclasses
- Dynamically composing prompts using registered stores
"""


from typing import ClassVar, Dict, Type, Any, Callable, List
import inspect

from prompt_engine.prompt_store import PromptStore
from prompt_engine.prompt_stores.task_context_store import TaskContextStore
from prompt_engine.prompt_stores.modality_store import ModalityStore
from prompt_engine.prompt_stores.tech_constraint_store import TechConstraintStore
from prompt_engine.prompt_stores.output_control_store import OutputControlStore
from prompt_engine.prompt_component import (
    PromptComponent, 
    TaskContextComponent, 
    ModalityComponent, 
    TechConstraintComponent, 
    OutputControlComponent
    )


class PromptComposer:
    """
    Composes structured prompts by aggregating modular prompt components
    from registered `PromptComponent` subclasses.

    Prompts can be composed for frontend or backend use cases independently.
    """

    _prompt_stores: ClassVar[Dict[Type[PromptComponent], Type[PromptStore]]] = {}

    @staticmethod
    def _validate_prompt_component(prompt_component: Any) -> None:
        """
        Validates that the given object is a valid subclass of PromptComponent.

        Args:
            prompt_component: The object to validate.

        Raises:
            TypeError: If the object is not a subclass of PromptComponent.
        """
        if not issubclass(prompt_component, PromptComponent):
            raise TypeError(
                "Expected prompt store component to be  a subclass of PromptComponent"
            )

    @staticmethod
    def _validate_prompt_store(prompt_store: Any) -> None:
        """
        Validates that the given object is a subclass of PromptStore.

        Args:
            prompt_store: The class to validate.

        Raises:
            TypeError: If the class does not inherit from PromptStore.
        """
        if not inspect.isclass(prompt_store) or not issubclass(prompt_store, PromptStore):
            raise TypeError(
                "Prompt store must be sublass of PromptStore"
            )

    @classmethod
    def _get_prompt_store(cls, prompt_component: Type[PromptComponent]) -> Type[PromptStore]:
        """
        Retrieves the prompt store class registered for the given component.

        Args:
            prompt_component: The component class to look up.

        Raises:
            KeyError: If the component is not registered.

        Returns:
            Type[PromptStore]: The associated prompt store class.
        """
        cls._validate_prompt_component(prompt_component)
        if  prompt_component not in cls._prompt_stores:
            raise KeyError(
                f"Prompt store '{prompt_component.__name__} not in the instructors registry."
            )
        return cls._prompt_stores[prompt_component]

    @classmethod
    def _get_frontend_prompt(cls, prompt_component: PromptComponent) -> str:
        """
        Fetches the frontend prompt for a given prompt component.

        Args:
            prompt_component: The specific prompt component instance.

        Returns:
            str: The associated frontend prompt string.
        """
        prompt_store = cls._get_prompt_store(prompt_component.__class__)
        prompt = prompt_store.get_frontend_prompt(prompt_component)
        return prompt

    @classmethod
    def _get_backend_prompt(cls,prompt_component: PromptComponent) -> str:
        """
        Fetches the backend prompt for a given prompt component.

        Args:
            prompt_component: The specific prompt component instance.

        Returns:
            str: The associated backend prompt string.
        """
        prompt_store = cls._get_prompt_store(prompt_component.__class__)
        prompt = prompt_store.get_backend_prompt(prompt_component)
        return prompt

    @classmethod
    def _compose_prompt(cls, get_prompt_func: Callable, prompt_components: List[PromptComponent]) -> str:
        """
        Composes a complete prompt by aggregating individual components using the provided prompt retrieval function.

        Args:
            get_prompt_func: Function to fetch either frontend or backend prompts.
            prompt_components: List of `PromptComponent` instances.

        Returns:
            str: The fully composed prompt string.
        """
        return ''.join(get_prompt_func(prompt_component) for prompt_component in prompt_components)

    @classmethod
    def register_prompt_store(cls,
                             prompt_component: Type[PromptComponent],
                             prompt_store: Type[PromptStore]
                             ) -> None:
        """
        Registers a prompt store class to handle a specific prompt component type.

        Args:
            prompt_component: The prompt component class.
            prompt_store: The associated prompt store class.
        """
        cls._validate_prompt_component(prompt_component)
        cls._validate_prompt_store(prompt_store)
        cls._prompt_stores[prompt_component] = prompt_store

    @classmethod
    def remove_prompt_store(cls, prompt_component: Type[PromptComponent]) -> None:
        """
        Unregisters a prompt store for the given component type.

        Args:
            prompt_component: The prompt component class to unregister.
        """
        if prompt_component in cls._prompt_stores:
            cls._prompt_stores.pop(prompt_component)

    @classmethod
    def prompt_stores(cls) -> Dict[Type[PromptComponent], Type[PromptStore]]:
        """
        Returns all currently registered prompt stores.

        Returns:
            Dict[Type[PromptComponent], Type[PromptStore]]: Mapping of component types to their prompt stores.
        """
        return cls._prompt_stores

    @classmethod
    def compose_frontend_prompt(cls, prompt_components: List[PromptComponent]) -> str:
        """
        Composes a frontend prompt using the provided prompt components.

        Args:
            prompt_components: List of component instances.

        Returns:
            str: Composed frontend prompt.
        """
        return cls._compose_prompt(get_prompt_func=cls._get_frontend_prompt, prompt_components=prompt_components)

    @classmethod
    def compose_backend_prompt(cls, prompt_components: List[PromptComponent]) -> str:
        """
        Composes a backend prompt using the provided prompt components.

        Args:
            prompt_components: List of component instances.

        Returns:
            str: Composed backend prompt.
        """
        return cls._compose_prompt(get_prompt_func=cls._get_backend_prompt, prompt_components=prompt_components)
    
    
                                                              # Register Prompt Stores
# ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------
PromptComposer.register_prompt_store(
    prompt_component=TaskContextComponent,
    prompt_store=TaskContextStore
    )

PromptComposer.register_prompt_store(
    prompt_component=ModalityComponent,
    prompt_store=ModalityStore
    )

PromptComposer.register_prompt_store(
    prompt_component=TechConstraintComponent,
    prompt_store=TechConstraintStore
    )

PromptComposer.register_prompt_store(
    prompt_component=OutputControlComponent,
    prompt_store=OutputControlStore
    )
