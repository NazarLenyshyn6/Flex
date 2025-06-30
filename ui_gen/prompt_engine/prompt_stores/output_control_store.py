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
            Generate code that strictly follows the provided specifications, patterns, and requirements without deviation.
            Ensure exact compliance with all stated constraints, style guides, and functional requirements.
            Do not make assumptions or add features beyond what is explicitly specified.
            """
    )

OutputControlStore.register_frontend_prompt(
    prompt_component=OutputControlComponent.COPY_PASTE_READY,
    frontend_prompt=
            """
            Generate complete, self-contained code that can be directly copied and pasted into a project without modification.
            Include all necessary imports, dependencies, and setup code required for immediate functionality.
            Ensure the code runs without additional configuration or missing dependencies.
            """
    )

OutputControlStore.register_frontend_prompt(
    prompt_component=OutputControlComponent.NO_IMPORTS,
    frontend_prompt=
            """
            Generate code without any external import statements or library dependencies.
            Use only built-in language features, native APIs, and standard library functionality.
            Avoid references to external packages, frameworks, or third-party libraries.
            """
    )

OutputControlStore.register_frontend_prompt(
    prompt_component=OutputControlComponent.FULL_MODULE,
    frontend_prompt=
            """
            Generate a complete module with all necessary imports, styles, configuration, and setup code.
            Include comprehensive implementation with proper module structure and all supporting code.
            Provide a fully functional module that integrates seamlessly with the target application.
            """
    )

OutputControlStore.register_frontend_prompt(
    prompt_component=OutputControlComponent.SNIPPET_ONLY,
    frontend_prompt=
            """
            Generate only the essential code snippet or component body without imports, setup, or boilerplate.
            Focus on the core functionality and implementation logic without surrounding infrastructure.
            Provide minimal, focused code that addresses the specific requirement.
            """
    )

OutputControlStore.register_frontend_prompt(
    prompt_component=OutputControlComponent.EXPLAINABLE,
    frontend_prompt=
            """
            Include comprehensive inline comments and documentation that explain the code's purpose and functionality.
            Add explanatory comments for complex logic, design decisions, and implementation details.
            Make the code self-documenting for educational and maintenance purposes.
            """
    )

OutputControlStore.register_frontend_prompt(
    prompt_component=OutputControlComponent.NO_COMMENTS,
    frontend_prompt=
            """
            Generate clean code without any comments, documentation, or explanatory text.
            Focus on production-ready code that is self-explanatory through clear naming and structure.
            Avoid inline comments, block comments, or documentation strings.
            """
    )

OutputControlStore.register_frontend_prompt(
    prompt_component=OutputControlComponent.WITH_TESTS,
    frontend_prompt=
            """
            Include comprehensive test coverage alongside the generated code implementation.
            Generate unit tests, integration tests, and edge case scenarios as appropriate.
            Ensure tests validate functionality, error handling, and component behavior.
            """
    )

OutputControlStore.register_frontend_prompt(
    prompt_component=OutputControlComponent.A11Y_ENFORCED,
    frontend_prompt=
            """
            Generate code that meets accessibility standards and passes WCAG compliance requirements.
            Include proper ARIA attributes, semantic HTML, keyboard navigation, and screen reader support.
            Ensure the code is fully accessible to users with disabilities.
            """
    )

OutputControlStore.register_frontend_prompt(
    prompt_component=OutputControlComponent.TYPE_ANNOTATED,
    frontend_prompt=
            """
            Include comprehensive type annotations, interfaces, and type definitions throughout the code.
            Use TypeScript types, JSDoc comments, or language-appropriate type systems for full type safety.
            Ensure all functions, variables, and components have explicit type information.
            """
    )

OutputControlStore.register_frontend_prompt(
    prompt_component=OutputControlComponent.PERFORMANCE_SAFE,
    frontend_prompt=
            """
            Generate code that avoids performance anti-patterns and follows optimization best practices.
            Prevent unnecessary re-renders, memory leaks, expensive calculations, and inefficient patterns.
            Focus on performance-conscious implementations that scale well.
            """
    )

OutputControlStore.register_frontend_prompt(
    prompt_component=OutputControlComponent.EXTRACT_VARIABLES,
    frontend_prompt=
            """
            Extract hardcoded values into named constants, configuration objects, or design tokens.
            Replace magic numbers, strings, and values with meaningful variable names and centralized definitions.
            Make the code more maintainable by eliminating hardcoded values.
            """
    )

OutputControlStore.register_frontend_prompt(
    prompt_component=OutputControlComponent.MOBILE_RESPONSIVE,
    frontend_prompt=
            """
            Ensure the generated UI components are fully responsive and work properly on mobile devices.
            Include appropriate breakpoints, flexible layouts, and mobile-optimized interactions.
            Test and optimize for various screen sizes and touch interfaces.
            """
    )

OutputControlStore.register_frontend_prompt(
    prompt_component=OutputControlComponent.DARK_MODE_SUPPORTED,
    frontend_prompt=
            """
            Include dark mode styling and theme support in the generated components.
            Implement proper color schemes, contrast ratios, and visual adaptations for dark themes.
            Ensure components work seamlessly in both light and dark mode environments.
            """
    )

OutputControlStore.register_frontend_prompt(
    prompt_component=OutputControlComponent.INTEGRATION_READY,
    frontend_prompt=
            """
            Generate components that integrate smoothly with existing application architecture and state management.
            Include proper hooks for application layout, routing, global state, and other integration points.
            Ensure components fit naturally within the broader application context.
            """
    )