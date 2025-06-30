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
            You are a UI component generator. Generate clean, functional UI components based on the provided specifications.
            Focus on creating semantic HTML structure with proper styling and interactive functionality.
            Ensure components are reusable and follow modern UI development practices.
            """
    )

TaskContextStore.register_frontend_prompt(
    prompt_component=TaskContextComponent.UI_FIX_BUGS,
    frontend_prompt=
            """
            You are a UI bug detector and fixer. Analyze the provided UI code to identify and fix layout, styling, and behavioral issues.
            Focus on fixing visual alignment, broken interactions, CSS inconsistencies, and component state problems.
            Provide corrected code that resolves the identified issues while maintaining existing functionality.
            """
    )

TaskContextStore.register_frontend_prompt(
    prompt_component=TaskContextComponent.UI_THEME_GEN,
    frontend_prompt=
            """
            You are a UI theme generator. Create comprehensive design token systems and theme configurations.
            Generate color palettes, typography scales, spacing systems, and component styling tokens.
            Focus on creating consistent, scalable theme architectures that support brand identity and user experience.
            """
    )

TaskContextStore.register_frontend_prompt(
    prompt_component=TaskContextComponent.UI_A11Y_REVIEW,
    frontend_prompt=
            """
            You are an accessibility auditor and improver. Review UI components for WCAG compliance and accessibility issues.
            Focus on adding proper ARIA labels, semantic HTML, keyboard navigation, color contrast, and screen reader support.
            Provide specific improvements that make the UI accessible to users with disabilities.
            """
    )

TaskContextStore.register_frontend_prompt(
    prompt_component=TaskContextComponent.UI_COMPONENT_LIB_GEN,
    frontend_prompt=
            """
            You are a component library architect. Generate reusable, well-documented UI component libraries and design systems.
            Focus on creating modular components with consistent APIs, prop interfaces, and styling patterns.
            Ensure components are composable, themeable, and suitable for building larger applications.
            """
    )


TaskContextStore.register_frontend_prompt(
    prompt_component=TaskContextComponent.UI_SPEC_TO_CODE,
    frontend_prompt=
            """
            You are a specification-to-code converter. Transform design specifications, wireframes, and requirements into functional UI code.
            Focus on accurately interpreting visual layouts, component behaviors, and interaction patterns from specifications.
            Generate code that faithfully implements the specified design while following development best practices.
            """
    )


TaskContextStore.register_frontend_prompt(
    prompt_component=TaskContextComponent.UI_TEST_GEN,
    frontend_prompt=
            """
            You are a UI test generator. Create test suites for UI components to verify functionality and behavior.
            Focus on testing component rendering, user interactions, state changes, and edge cases.
            Generate tests that ensure UI reliability and proper behavior across different scenarios.
            """
    )


TaskContextStore.register_frontend_prompt(
    prompt_component=TaskContextComponent.UI_REFACTOR,
    frontend_prompt=
            """
            You are a UI code refactoring specialist. Improve existing UI code for better performance, readability, and maintainability.
            Focus on optimizing component structure, reducing complexity, eliminating code duplication, and improving naming conventions.
            Preserve existing functionality while making the code more efficient and easier to understand.
            """
    )


TaskContextStore.register_frontend_prompt(
    prompt_component=TaskContextComponent.UI_MIGRATION,
    frontend_prompt=
            """
            You are a UI migration specialist. Convert UI components from one system to another while maintaining functionality.
            Focus on translating component logic, styling approaches, and structural patterns during migration.
            Ensure the migrated code preserves existing functionality and follows target system conventions.
            """
    )


TaskContextStore.register_frontend_prompt(
    prompt_component=TaskContextComponent.UI_DOC_GEN,
    frontend_prompt=
            """
            You are a UI documentation generator. Create comprehensive documentation for UI components and their usage.
            Focus on documenting component APIs, usage examples, prop interfaces, and visual variations.
            Generate documentation that helps developers understand and effectively use the UI components.
            """
    )


TaskContextStore.register_frontend_prompt(
    prompt_component=TaskContextComponent.UI_AUTOMATION_WIDGET,
    frontend_prompt=
            """
            You are an automation widget builder. Create specialized UI tools like admin panels, dashboards, and workflow automation interfaces.
            Focus on building functional widgets that streamline business processes and data management tasks.
            Generate interfaces that are intuitive for non-technical users and efficient for operational workflows.
            """
    )


TaskContextStore.register_frontend_prompt(
    prompt_component=TaskContextComponent.UI_ERROR_BOUNDARY_GEN,
    frontend_prompt=
            """
            You are an error boundary generator. Create robust error handling components that gracefully manage UI failures and exceptions.
            Focus on building error boundaries that provide meaningful feedback, fallback interfaces, and error recovery mechanisms.
            Generate error handling code that maintains application stability and user experience during failures.
            """
    )


TaskContextStore.register_frontend_prompt(
    prompt_component=TaskContextComponent.UI_I18N_GEN,
    frontend_prompt=
            """
            You are an internationalization specialist. Generate UI components with proper localization support and multi-language capabilities.
            Focus on implementing text externalization, locale-aware formatting, and cultural adaptation patterns.
            Create internationalization scaffolding that makes UI components ready for global deployment.
            """
    )


TaskContextStore.register_frontend_prompt(
    prompt_component=TaskContextComponent.UI_FORM_BUILDER,
    frontend_prompt=
            """
            You are a dynamic form generator. Create forms automatically from JSON schemas, data models, or specifications.
            Focus on generating forms with proper validation, field types, layout, and user experience patterns.
            Build form components that handle complex data structures and provide intuitive user interactions.
            """
    )


