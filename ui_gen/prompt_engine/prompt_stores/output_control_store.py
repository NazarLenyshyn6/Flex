"""
This module defines `OutputControlStore`, a concrete implementation of `PromptStore`
responsible for managing prompts related to output expectations, such as the
strictness or formatting of generated responses.

This store supports registering and retrieving both frontend and backend prompts
based on `OutputControlComponent` values.
"""


from typing import Dict, Type

from typing_extensions import override

from prompt_engine.prompt_store import PromptStore
from prompt_engine.prompt_component import OutputControlComponent


class OutputControlStore(PromptStore[OutputControlComponent]):
    """
    Stores and retrieves frontend and backend prompts associated with
    `OutputControlComponent` values, which define the required level of
    compliance or formatting in the model's output.
    """

    _frontend_prompt_store: Dict[OutputControlComponent, str] = {}
    _backend_prompt_store: Dict[OutputControlComponent, str] = {}

    @override
    @classmethod
    def prompt_component(cls) -> Type[OutputControlComponent]:
        """
        Returns the type of prompt component managed by this store.

        Returns:
            Type[OutputControlComponent]: The component enum type.
        """
        return OutputControlComponent


                                                                        # Register Output Control Prompts
# -------------------------------------------------------------------------------------------------------------------------------------------------------------------------

OutputControlStore.register_frontend_prompt(
    prompt_component=OutputControlComponent.STRICT_COMPLIANCE,
    frontend_prompt=
            """
            ###  Final Deliverables

            * Must be **live-demo ready** with full real-world functionality
            * Must showcase **working UI and backend-connected logic**
            * Must use **axios** and **centralized state**
            * Must support:

            * Navigation
            * User flows
            * Error states
            * Edge case handling
            * Must enforce **strict JSON API communication** as per contract

            Required: Schema-Driven Validation & Safety (NEW SECTION)
                * All request payloads and responses must be bound to strict TypeScript types derived
                * Optionally use runtime validators (e.g. Zod, Yup) to enforce shape before sending
                * Add a validation layer to all axios calls that:
                * Asserts required keys and types are present
                * Rejects calls that deviate from schema
                * Ensure request body structure and field types are 100% compliant with backend contract — even a missing or extra field must cause dev-time failure

            ---

            ###  Absolutely Forbidden

            * Using Pages Router
            * Using `fetch`, GraphQL, or any HTTP library besides `axios`
            * Using mocks, dummy data, or faked responses
            * Inferring, guessing, or modifying backend behavior
            * Using any state manager other than Zustand or Redux Toolkit
            * Writing any `GET` or `POST` call with incorrect or partial JSON payloads
            * Using `any` in TypeScript

            ---

            **Failure to follow any point above — especially any deviation from expected API JSON schema — will result in project rejection.** This must be a **production-ready**, **error-free**, **pixel-perfect**, and **strictly compliant** frontend system.
            Any mismatch between frontend and backend schemas (resulting in 422 or 500 errors) will lead to immediate rejection.
            The final result must be error-free, pixel-perfect, and contract-compliant in every interaction.
            """
    )