"""
This module defines `TaskContextStore`, a specialized subclass of `PromptStore`
for handling prompt templates related to the context of the task being performed,
such as UI generation, data analysis, or chatbot interaction.

This class enables type-safe registration and retrieval of frontend and backend
prompts tied to specific `TaskContextComponent` values.
"""


from typing import Dict, Type

from typing_extensions import override

from prompt_engine.prompt_store import PromptStore
from prompt_engine.prompt_component import TaskContextComponent


class TaskContextStore(PromptStore[TaskContextComponent]):
    """
    Manages storage and retrieval of frontend and backend prompt templates
    associated with `TaskContextComponent` values, which define the high-level
    purpose or scope of the user's task (e.g., UI generation).

    Provides a strongly-typed implementation of the generic `PromptStore`.
    """
    _frontend_prompt_store: Dict[TaskContextComponent, str] = {}
    _backend_prompt_store: Dict[TaskContextComponent, str] = {}

    @override
    @classmethod
    def prompt_component(cls) -> Type[TaskContextComponent]:
        """
        Specifies the type of prompt component managed by this store.

        Returns:
            Type[TaskContextComponent]: The `TaskContextComponent` enum type.
        """
        return TaskContextComponent



                                                                        # Register Task Context Prompts
# -------------------------------------------------------------------------------------------------------------------------------------------------------------------------

TaskContextStore.register_frontend_prompt(
    prompt_component=TaskContextComponent.UI_GENERATION,
    frontend_prompt=
            """
            You are a **senior frontend engineer** tasked with building a **fully functional, production-grade web application**.
            The application must be **visually and behaviorally identical** and must **connect directly to the real backend**.
            """
    )

TaskContextStore.register_backend_prompt(
    prompt_component=TaskContextComponent.UI_GENERATION,
    backend_prompt=
            """
            You are a **senior frontend engineer** tasked with building a **fully functional, production-grade web application**.
            The application must be **visually and behaviorally identical** and must **connect directly to the real backend**.
            """
    )