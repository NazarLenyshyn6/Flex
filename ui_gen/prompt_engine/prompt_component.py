"""
This module defines enumerations for various modular components of a dynamic prompt system used in backend/frontend
code generation tasks. Each component represents a category of input or context that contributes
to the formation of structured and configurable prompts.

These enums allow for a strongly typed, explicit prompt configuration experience.
"""

from enum import Enum, auto


class PromptComponent(Enum):
    """
    Base enumeration for all prompt components. Acts as a marker interface for type safety and inheritance.
    """
    ...


class TaskContextComponent(PromptComponent):
    """
    Specifies the high-level task or problem context for the prompt.
    """

    UI_GENERATION = auto()


class ModalityComponent(PromptComponent):
    """
    Specifies modality and how the input data should be interpreted or parsed.
    """

    IMAGE_TEXT = auto()
    IMAGE = auto()
    TEXT = auto()


class TechConstraintComponent(PromptComponent):
    """
    Specifies technical or architectural constraints the output should adhere to.
    """

    NEXTJS = auto()
    FASTAPI = auto()


class OutputControlComponent(PromptComponent):
    """
    Final controlling layer of the prompt system. Specifies strict output-level constraints,
    format rules, and behavioral directives that the model must adhere to.
    Acts as a guardrail to enforce precision, compliance, and safe generation boundaries.
    """

    STRICT_COMPLIANCE = auto()