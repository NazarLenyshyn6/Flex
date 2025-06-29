"""
This module defines `TechConstraintStore`, a concrete implementation of `PromptStore`
for managing prompt templates related to technology constraints (e.g., frameworks,
libraries, infrastructure) specified by the user.

This class allows structured registration and retrieval of frontend and backend
prompt components tied to specific `TechConstraintComponent` values.
"""


from typing import Dict, Type

from typing_extensions import override

from prompt_engine.prompt_store import PromptStore
from prompt_engine.prompt_component import TechConstraintComponent


class TechConstraintStore(PromptStore[TechConstraintComponent]):
    """
    Handles frontend and backend prompt templates related to technical constraints,
    such as required technologies (e.g., Next.js, FastAPI) specified for the task.

    This store provides a strongly-typed specialization of the generic `PromptStore`
    for managing prompts that enforce adherence to technical requirements.
    """
    _frontend_prompt_store: Dict[TechConstraintComponent, str] = {}
    _backend_prompt_store: Dict[TechConstraintComponent, str] = {}

    @override
    @classmethod
    def prompt_component(cls) -> Type[TechConstraintComponent]:
        """
        Returns the type of component this store handles.

        Returns:
            Type[TechConstraintComponent]: The `TechConstraintComponent` enum type.
        """
        return TechConstraintComponent


                                                                        # Register Tech Constraint Prompts
# -------------------------------------------------------------------------------------------------------------------------------------------------------------------------
TechConstraintStore.register_frontend_prompt(
    prompt_component=TechConstraintComponent.NEXTJS,
    frontend_prompt=
            """
            ###  Technical Stack (MANDATORY — NO EXCEPTIONS)

                    * **Framework**: `Next.js` using **App Router only**
                    * **Language**: `TypeScript` only
                    * **Components**: **React functional components** only
                    * **Styling**: Use **CSS Modules**, **TailwindCSS**, or **Styled Components** consistently
                    * **HTTP Client**: `axios` only — **`fetch` is strictly forbidden**
                    * **State Management**: Only **Zustand** or **Redux Toolkit**
                    * **Project Structure**: Must follow the `/app` folder convention of Next.js App Router

                    ---

                    Backend Integration Requirements
                    *Only use endpoints and payloads defined in UI/api_contract.md.
                    *No endpoint guessing, response inferring, or structure altering allowed.
                    *Use TypeScript interfaces to type-check all API inputs/outputs.
                    *Implement a centralized api service module (e.g. /services/api.ts) that wraps axios and enforces exact schema usage.
                    Every request must:
                    *Use the exact JSON schema as defined (no fields missing or added)
                    *Validate payloads before sending using type-safe helpers (e.g. Zod, Yup, or custom validators if needed)
                    Reject any response that does not conform to expected schema (log, throw, or handle)
                        * Required states: loading, error, success, empty, disabled
                        * Polling or real-time updates only if specified in the contract
                    ---

                    ###  Project Requirements

                    * Must run out-of-the-box with:

                    ```bash
                    npm install
                    npm run dev
                    ```

                    * Required files:

                    ```
                    package.json
                    tsconfig.json
                    next.config.js
                    .env.example
                    ```

                    * Use **strict TypeScript typing** — absolutely **no `any`**
                    * Organize code in a modular structure:

                    ```
                    /app
                    /components
                    /lib
                    /store
                    /services
                    /types
                    ```

                    ---

                    ###  Functionality & State Management

                    * Use **Zustand** or **Redux Toolkit** to centralize state
                    * Every feature must:

                    * Manage `loading`, `error`, `data`, and `UI toggles` in state
                    * Handle **optimistic updates** with rollback
                    * Wire all form inputs directly to backend logic
                    * Ensure state and API results are in full sync with the contract
            """
    )