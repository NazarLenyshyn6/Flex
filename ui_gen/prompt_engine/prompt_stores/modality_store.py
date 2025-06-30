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
    prompt_component=ModalityComponent.TEXT,
    frontend_prompt=
    """
    Process free-form text input as UI generation instructions. Parse natural language commands and descriptions to extract UI requirements.
    Identify component types, layout specifications, styling preferences, and functional requirements from textual descriptions.
    Convert text-based UI requests into structured component generation parameters.
    """
    )

ModalityStore.register_frontend_prompt(
    prompt_component=ModalityComponent.IMAGE,
    frontend_prompt=
    """
    Analyze UI screenshots or rendered component images to understand visual structure and design patterns.
    Extract layout information, component hierarchy, styling details, and visual relationships from images.
    Generate code that recreates the visual appearance and structure shown in the provided UI images.
    """
    )

ModalityStore.register_frontend_prompt(
    prompt_component=ModalityComponent.SKETCH,
    frontend_prompt=
    """
    Interpret hand-drawn sketches and whiteboard wireframes to understand intended UI layout and functionality.
    Extract component placement, rough sizing, navigation flow, and interaction patterns from sketched designs.
    Transform sketched concepts into functional UI components while preserving the intended design intent.
    """
    )

ModalityStore.register_frontend_prompt(
    prompt_component=ModalityComponent.MARKDOWN_SPEC,
    frontend_prompt=
    """
    Parse structured markdown specifications to extract UI requirements and component definitions.
    Process markdown-formatted documents containing feature specifications, component requirements, and design guidelines.
    Convert markdown specifications into implementable UI components following the documented requirements.
    """
    )

ModalityStore.register_frontend_prompt(
    prompt_component=ModalityComponent.JSON_SCHEMA,
    frontend_prompt=
    """
    Interpret JSON schemas and backend data models to generate appropriate UI components for data representation.
    Analyze data structure, field types, validation rules, and relationships to create suitable form inputs and display components.
    Generate UI components that properly handle the data types and constraints defined in the JSON schema.
    """
    )

ModalityStore.register_frontend_prompt(
    prompt_component=ModalityComponent.HTML,
    frontend_prompt=
    """
    Process existing HTML markup for audit, analysis, or migration purposes.
    Extract semantic structure, styling patterns, and component organization from HTML code.
    Use HTML analysis to inform UI improvements, framework migrations, or component modernization.
    """
    )

ModalityStore.register_frontend_prompt(
    prompt_component=ModalityComponent.YAML_UI_CONFIG,
    frontend_prompt=
    """
    Parse YAML configuration files that describe UI structure and component hierarchies.
    Extract component definitions, layout specifications, and configuration parameters from YAML format.
    Generate UI components based on the structured configuration data provided in YAML format.
    """
    )

ModalityStore.register_frontend_prompt(
    prompt_component=ModalityComponent.DSL_UI_LANG,
    frontend_prompt=
    """
    Process domain-specific language expressions for UI generation from custom UI description languages.
    Parse DSL syntax to understand component specifications, data bindings, and interaction patterns.
    Convert DSL expressions into native UI components while preserving the specified behavior and structure.
    """
    )