"""
This module defines the `RefinementStore`, a concrete subclass of `PromptStore`
that manages structured prompt templates focused on output refinement directives.

`RefinementComponent` values capture common post-generation improvements, such as
fixing layout bugs, enforcing best practices, or improving accessibility.

The store supports type-safe registration and retrieval of both frontend and backend
prompts, enabling consistent application of UI and code refinement strategies across
multiple generations.
"""


from typing import Dict, Type

from typing_extensions import override

from prompt_engine.prompt_store import PromptStore
from prompt_engine.prompt_component import RefinementComponent


class RefinementStore(PromptStore[RefinementComponent]):
    """
    Stores and retrieves frontend and backend prompts associated with
    `RefinementComponent` values, which represent post-generation refinement
    directives such as layout fixes, accessibility improvements, or code cleanup.

    Implements a type-safe specialization of `PromptStore` for structured refinement
    of generated output across domains like frontend UI or backend logic.
    """

    _frontend_prompt_store: Dict[RefinementComponent, str] = {}
    _backend_prompt_store: Dict[RefinementComponent, str] = {}

    @override
    @classmethod
    def prompt_component(cls) -> Type[RefinementComponent]:
        """
        Returns the type of prompt component managed by this store.

        Returns:
            Type[RefinementComponent]: The component enum type.
        """
        return RefinementComponent
    
    
                                                                        # Register Refinement Prompts
# -------------------------------------------------------------------------------------------------------------------------------------------------------------------------ModalityStore.register_frontend_prompt(
RefinementStore.register_frontend_prompt(
    prompt_component=RefinementComponent.FIX_VISUAL_LAYOUT,
    frontend_prompt=
    """
    Identify and fix visual layout issues including spacing problems, alignment issues, and element positioning.
    Correct CSS layout bugs, improper margins/padding, and visual inconsistencies in component arrangement.
    Ensure proper visual hierarchy and clean alignment throughout the interface.
    """
    )

RefinementStore.register_frontend_prompt(
    prompt_component=RefinementComponent.FIX_A11Y,
    frontend_prompt=
    """
    Add comprehensive accessibility features including ARIA labels, semantic HTML tags, and screen reader support.
    Implement keyboard navigation, focus management, and accessibility best practices for inclusive design.
    Ensure components meet WCAG guidelines and are usable by people with disabilities.
    """
    )

RefinementStore.register_frontend_prompt(
    prompt_component=RefinementComponent.ADD_RESPONSIVENESS,
    frontend_prompt=
    """
    Implement responsive design patterns to ensure proper rendering across mobile, tablet, and desktop devices.
    Add appropriate breakpoints, flexible layouts, and adaptive styling for different screen sizes.
    Optimize user experience for touch interfaces and varying viewport dimensions.
    """
    )

RefinementStore.register_frontend_prompt(
    prompt_component=RefinementComponent.FIX_INTERACTIVITY,
    frontend_prompt=
    """
    Fix interactive element functionality including button actions, form inputs, and user interaction handlers.
    Ensure proper event handling, state updates, and user feedback for all interactive components.
    Correct broken click handlers, form submissions, and interactive behavior issues.
    """
    )

RefinementStore.register_frontend_prompt(
    prompt_component=RefinementComponent.EXTRACT_CONSTANTS,
    frontend_prompt=
    """
    Identify hardcoded values and extract them into named constants or configuration objects.
    Replace magic numbers, string literals, and repeated values with meaningful constant definitions.
    Improve code maintainability by centralizing configurable values and eliminating duplication.
    """
    )

RefinementStore.register_frontend_prompt(
    prompt_component=RefinementComponent.ADD_COMMENTS,
    frontend_prompt=
    """
    Add helpful developer comments that explain complex logic, design decisions, and implementation details.
    Include documentation for component APIs, usage patterns, and important behavioral considerations.
    Make the code more maintainable through clear, concise explanatory comments.
    """
    )

RefinementStore.register_frontend_prompt(
    prompt_component=RefinementComponent.REMOVE_DUPLICATION,
    frontend_prompt=
    """
    Identify and eliminate code duplication by extracting common functionality into reusable components or utilities.
    Refactor repeated patterns into shared functions, hooks, or component abstractions.
    Improve code maintainability by following the DRY (Don't Repeat Yourself) principle.
    """
    )

RefinementStore.register_frontend_prompt(
    prompt_component=RefinementComponent.APPLY_BEST_PRACTICES,
    frontend_prompt=
    """
    Apply modern UI development best practices including proper component architecture and clean code principles.
    Implement industry-standard patterns for state management, component composition, and code organization.
    Ensure code follows established conventions and maintainability guidelines.
    """
    )

RefinementStore.register_frontend_prompt(
    prompt_component=RefinementComponent.SPLIT_COMPONENT,
    frontend_prompt=
    """
    Break down large, monolithic components into smaller, focused, and reusable component pieces.
    Separate concerns by extracting logical units into individual components with clear responsibilities.
    Improve component maintainability and reusability through proper decomposition.
    """
    )

RefinementStore.register_frontend_prompt(
    prompt_component=RefinementComponent.ADD_TYPES,
    frontend_prompt=
    """
    Add comprehensive type annotations using available type checking systems for the target platform.
    Define interfaces, type definitions, and type constraints for better code safety and developer experience.
    Ensure all component props, function parameters, and return values have explicit type information.
    """
    )

RefinementStore.register_frontend_prompt(
    prompt_component=RefinementComponent.UPGRADE_SEMANTICS,
    frontend_prompt=
    """
    Replace generic HTML elements with proper semantic HTML5 tags such as section, nav, article, and header.
    Improve document structure and accessibility by using meaningful semantic elements.
    Enhance SEO and screen reader compatibility through proper semantic markup.
    """
    )

RefinementStore.register_frontend_prompt(
    prompt_component=RefinementComponent.IMPROVE_CONTRAST,
    frontend_prompt=
    """
    Analyze and improve color contrast ratios to meet accessibility standards and enhance visual readability.
    Adjust color choices, text styling, and background combinations for better visual contrast.
    Ensure color schemes meet WCAG contrast requirements for all user interface elements.
    """
    )

RefinementStore.register_frontend_prompt(
    prompt_component=RefinementComponent.FIX_STATE_MANAGEMENT,
    frontend_prompt=
    """
    Correct issues with component state management including improper hook usage, state mutation, and prop handling.
    Fix state update patterns, event handling logic, and component lifecycle management problems.
    Ensure proper state flow and prevent common state-related bugs and anti-patterns.
    """
    )

RefinementStore.register_frontend_prompt(
    prompt_component=RefinementComponent.REDUCE_BUNDLE_SIZE,
    frontend_prompt=
    """
    Optimize code for smaller bundle sizes through tree shaking, lazy loading, and efficient import patterns.
    Eliminate unnecessary dependencies, unused code, and optimize component loading strategies.
    Implement code splitting and dynamic imports to reduce initial bundle size and improve performance.
    """
    )

RefinementStore.register_frontend_prompt(
    prompt_component=RefinementComponent.ADD_LOADING_STATES,
    frontend_prompt=
    """
    Implement loading indicators and states for asynchronous operations and data fetching workflows.
    Add proper loading spinners, skeleton screens, and progress indicators for better user experience.
    Handle loading, error, and success states appropriately in async component interactions.
    """
    )

RefinementStore.register_frontend_prompt(
    prompt_component=RefinementComponent.ENFORCE_NAMING_CONVENTIONS,
    frontend_prompt=
    """
    Standardize naming conventions for components, props, functions, and CSS classes throughout the codebase.
    Apply consistent naming patterns that follow industry standards and team conventions.
    Improve code readability and maintainability through clear, descriptive, and consistent naming.
    """
    )