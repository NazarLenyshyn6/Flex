"""
This module defines `ModalityStore`, a concrete implementation of `PromptStore`
specialized for handling input modality components.

This class stores frontend and backend prompt templates associated with
each `ModalityComponent`, and ensures type-safe retrieval and registration
of these components.
"""


from typing import Dict, Type

from typing_extensions import override

from prompt_engine.prompt_store import PromptStore
from prompt_engine.prompt_component import ModalityComponent


class ModalityStore(PromptStore[ModalityComponent]):
    """
    Concrete implementation of `PromptStore` for storing and retrieving
    prompt templates related to input modality (e.g., image, text, or both).

    It maintains separate frontend and backend prompt stores keyed by
    `ModalityComponent` enums.
    """

    _frontend_prompt_store: Dict[ModalityComponent, str] = {}
    _backend_prompt_store: Dict[ModalityComponent, str] = {}

    @override
    @classmethod
    def prompt_component(cls) -> Type[ModalityComponent]:
        """
        Returns the type of prompt component this store manages.

        Returns:
            Type[ModalityComponent]: The component enum type.
        """
        return ModalityComponent


                                                                # Register Modality Prompts
# ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------
ModalityStore.register_frontend_prompt(
    prompt_component=ModalityComponent.IMAGE_TEXT,
    frontend_prompt=
    """
        ###  Input Assets

        * `UI/layout/`: Pixel-perfect reference images for all screens, modals, forms, and interaction states (hover, loading, error, empty, disabled, success). **You must match these exactly — no approximations allowed.**
        * `UI/api_contract.md`: The **sole source of truth** describing all endpoints, request/response JSON schemas, payload types, status codes, and behaviors. **No guessing, inferring, or altering any behavior**.
    """
    )