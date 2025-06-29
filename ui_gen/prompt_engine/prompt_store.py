"""
This module defines abstract base class for managing frontend and backend prompt strings associated with
strongly-typed prompt components in a structured and reusable way.

`PromptStore` -  generic and extensible class that enables prompt
registration, retrieval, and validation for both frontend and backend contexts. Subclasses
must define their own storage dictionaries and the specific type of `PromptComponent` they support.

Features:
- Separation of frontend and backend prompt registries
- Type-safe prompt component validation
- Enforced subclass structure via ABC mechanisms
- Common CRUD operations for prompt management

Usage:
    Subclass `PromptStore` and implement the `prompt_component()` class method
    to specify the expected type of prompt components.
"""


from abc import ABC, abstractmethod
from typing import TypeVar, Generic, Dict, Type, Any

from prompt_engine.prompt_component import PromptComponent

T = TypeVar("T", bound=PromptComponent)


class PromptStore(ABC, Generic[T]):
    """
    Abstract base class for managing prompt components and their corresponding frontend and backend prompts.

    Subclasses must define their own `_frontend_prompt_store` and `_backend_prompt_store` dictionaries,
    and implement the `prompt_component()` class method to specify the expected PromptComponent type.
    """

    _frontend_prompt_store: Dict[T, str] = {}
    _backend_prompt_store: Dict[T, str] = {}

    def __init_subclass__(cls) -> None:
        """
        Ensures that each subclass provides its own `_frontend_prompt_store` and `_backend_prompt_store`.
        Raises:
            KeyError: If the subclass does not define both required stores.
        """
        super().__init_subclass__()
        if (cls.__dict__.get('_frontend_prompt_store') is None or
            cls.__dict__.get('_backend_prompt_store') is None
            ):
            raise KeyError(
                f"Subclass '{cls.__name__}' must define its own '_frontend_prompt_store' and '_backend_prompt_store' dictionaries."
            )

    @classmethod
    def _validate_prompt_component(cls, prompt_component: Any) -> None:
        """
        Validates whether the provided prompt_component is of the expected type.

        Args:
            prompt_component: The prompt component to validate.

        Raises:
            TypeError: If the component is not of the expected type.
        """
        expected_prompt_component = cls.prompt_component()
        if not isinstance(prompt_component, expected_prompt_component):
            raise TypeError(
                f"Invalid prompt component: extexped: {expected_prompt_component.__name__}"
                f"got '{type(prompt_component).__name__}'."
            )

    @classmethod
    def get_frontend_prompt(cls, prompt_component: T) -> str:
        """
        Retrieves the frontend prompt associated with a given prompt component.

        Args:
            prompt_component: The prompt component to retrieve the prompt for.

        Returns:
            str: The corresponding frontend prompt string.

        Raises:
            KeyError: If the component is not registered.
        """
        cls._validate_prompt_component(prompt_component)
        if prompt_component not in cls._frontend_prompt_store:
            raise KeyError(
                f"Prompt component '{prompt_component}' not found in {cls.__name__} frontend prompt store."
            )
        return cls._frontend_prompt_store[prompt_component]

    @classmethod
    def get_backend_prompt(cls, prompt_component: T) -> str:
        """
        Retrieves the backend prompt associated with a given prompt component.

        Args:
            prompt_component: The prompt component to retrieve the prompt for.

        Returns:
            str: The corresponding backend prompt string.

        Raises:
            KeyError: If the component is not registered.
        """
        cls._validate_prompt_component(prompt_component)
        if prompt_component not in cls._backend_prompt_store:
            raise KeyError(
                f"Prompt component '{prompt_component}' not found in {cls.__name__} backend prompt store."
            )
        return cls._backend_prompt_store[prompt_component]

    @classmethod
    def register_frontend_prompt(cls,
                              prompt_component: T,
                              frontend_prompt: str
                              ) -> None:
        """
        Registers or updates the frontend prompt for a given component.

        Args:
            prompt_component: The prompt component to associate with the prompt.
            frontend_prompt: The frontend prompt string.
        """
        cls._validate_prompt_component(prompt_component)
        cls._frontend_prompt_store[prompt_component] = frontend_prompt

    @classmethod
    def register_backend_prompt(cls,
                             prompt_component: T,
                             backend_prompt: str
                             ) -> None:
        """
        Registers or updates the backend prompt for a given component.

        Args:
            prompt_component: The prompt component to associate with the prompt.
            backend_prompt: The backend prompt string.
        """
        cls._validate_prompt_component(prompt_component)
        cls._backend_prompt_store[prompt_component] = backend_prompt

    @classmethod
    def remove_frontend_prompt(cls, prompt_component: T) -> None:
        """
        Removes the frontend prompt associated with a given component, if present.

        Args:
            prompt_component: The prompt component to remove.
        """
        if prompt_component in cls._frontend_prompt_store:
            cls._frontend_prompt_store.pop(prompt_component)

    @classmethod
    def remove_backend_prompt(cls, prompt_component: T) -> None:
        """
        Removes the backend prompt associated with a given component, if present.

        Args:
            prompt_component: The prompt component to remove.
        """
        if prompt_component in cls._backend_prompt_store:
            cls._backend_prompt_store.pop(prompt_component)

    @classmethod
    def frontend_prompt_store(cls) -> Dict[T, str]:
        """
        Returns the entire frontend prompt store.

        Returns:
            Dict[T, str]: A dictionary mapping prompt components to their frontend prompts.
        """
        return cls._frontend_prompt_store

    @classmethod
    def backend_prompt_store(cls) -> Dict[T, str]:
        """
        Returns the entire backend prompt store.

        Returns:
            Dict[T, str]: A dictionary mapping prompt components to their backend prompts.
        """
        return cls._backend_prompt_store

    @classmethod
    @abstractmethod
    def prompt_component(cls) -> Type[PromptComponent]:
        """
        Must be implemented by subclasses to return the specific PromptComponent type used for validation.

        Returns:
            Type[PromptComponent]: The class type of the expected prompt component.
        """
        ...