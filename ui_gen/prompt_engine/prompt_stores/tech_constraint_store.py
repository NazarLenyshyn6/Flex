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
    prompt_component=TechConstraintComponent.REACT,
    frontend_prompt=
            """
            Generate React components using modern React patterns including functional components, hooks, and JSX.
            Follow React best practices for component composition, state management, and lifecycle handling.
            Ensure components are compatible with React ecosystem and follow React naming conventions.
            """
    )

TechConstraintStore.register_frontend_prompt(
    prompt_component=TechConstraintComponent.NEXTJS,
    frontend_prompt=
            """
            Generate components optimized for Next.js framework including proper use of Next.js routing, SSR/SSG patterns, and built-in optimizations.
            Use Next.js specific features like Image component, Link component, and API routes where appropriate.
            Follow Next.js conventions for file structure, dynamic imports, and performance optimization.
            """
    )

TechConstraintStore.register_frontend_prompt(
    prompt_component=TechConstraintComponent.VUE,
    frontend_prompt=
            """
            Generate Vue.js components using Vue 3 Composition API, reactive data, and Vue's template syntax.
            Follow Vue.js conventions for component structure, props, events, and lifecycle hooks.
            Ensure components are compatible with Vue ecosystem and follow Vue naming conventions.
            """
    )

TechConstraintStore.register_frontend_prompt(
    prompt_component=TechConstraintComponent.SVELTE,
    frontend_prompt=
            """
            Generate Svelte components using Svelte's reactive syntax, stores, and component lifecycle.
            Follow Svelte conventions for component structure, reactive statements, and event handling.
            Utilize Svelte's compile-time optimizations and built-in state management patterns.
            """
    )

TechConstraintStore.register_frontend_prompt(
    prompt_component=TechConstraintComponent.TAILWIND,
    frontend_prompt=
            """
            Apply Tailwind CSS utility classes for styling, following Tailwind's utility-first approach.
            Use Tailwind's responsive design utilities, color system, and spacing scale consistently.
            Leverage Tailwind's component variants and state modifiers for interactive styling.
            """
    )

TechConstraintStore.register_frontend_prompt(
    prompt_component=TechConstraintComponent.CHAKRA_UI,
    frontend_prompt=
            """
            Use Chakra UI components and theming system for consistent design implementation.
            Follow Chakra UI patterns for component composition, spacing, and responsive design.
            Leverage Chakra UI's built-in accessibility features and design tokens.
            """
    )

TechConstraintStore.register_frontend_prompt(
    prompt_component=TechConstraintComponent.MATERIAL_UI,
    frontend_prompt=
            """
            Implement components using Material-UI (MUI) components following Material Design principles.
            Use MUI's theming system, styling solutions, and component variants appropriately.
            Follow Material Design guidelines for layout, typography, and interaction patterns.
            """
    )

TechConstraintStore.register_frontend_prompt(
    prompt_component=TechConstraintComponent.STORYBOOK,
    frontend_prompt=
            """
            Create components that are Storybook-compatible with proper story definitions and controls.
            Generate components with clear prop interfaces and variations suitable for Storybook documentation.
            Include Storybook stories that showcase different component states and use cases.
            """
    )

TechConstraintStore.register_frontend_prompt(
    prompt_component=TechConstraintComponent.TYPESCRIPT,
    frontend_prompt=
            """
            Generate TypeScript code with proper type definitions, interfaces, and type safety.
            Use TypeScript features like generics, union types, and strict type checking.
            Follow TypeScript best practices for component props, state, and function signatures.
            """
    )

TechConstraintStore.register_frontend_prompt(
    prompt_component=TechConstraintComponent.FLUTTER,
    frontend_prompt=
            """
            Generate Flutter widgets using Dart language and Flutter's widget composition patterns.
            Follow Flutter conventions for widget structure, state management, and Material/Cupertino design.
            Use Flutter's layout system and responsive design principles for cross-platform compatibility.
            """
    )

TechConstraintStore.register_frontend_prompt(
    prompt_component=TechConstraintComponent.REACT_NATIVE,
    frontend_prompt=
            """
            Create React Native components optimized for mobile platforms using React Native APIs and components.
            Follow React Native patterns for navigation, platform-specific code, and mobile UI conventions.
            Use React Native's built-in components and styling system for cross-platform mobile development.
            """
    )

TechConstraintStore.register_frontend_prompt(
    prompt_component=TechConstraintComponent.ANT_DESIGN,
    frontend_prompt=
            """
            Implement UI components using Ant Design component library and design language.
            Follow Ant Design patterns for form handling, data display, and enterprise application interfaces.
            Use Ant Design's theming capabilities and component configuration options.
            """
    )

TechConstraintStore.register_frontend_prompt(
    prompt_component=TechConstraintComponent.BOOTSTRAP,
    frontend_prompt=
            """
            Apply Bootstrap CSS framework classes and components for responsive web design.
            Use Bootstrap's grid system, utility classes, and component library consistently.
            Follow Bootstrap conventions for responsive layouts and component styling.
            """
    )

TechConstraintStore.register_frontend_prompt(
    prompt_component=TechConstraintComponent.WEB_COMPONENTS,
    frontend_prompt=
            """
            Create standard Web Components using Custom Elements, Shadow DOM, and HTML Templates.
            Follow Web Components specifications for component encapsulation and reusability.
            Ensure components are framework-agnostic and compatible with standard HTML usage.
            """
    )

TechConstraintStore.register_frontend_prompt(
    prompt_component=TechConstraintComponent.PYQT,
    frontend_prompt=
            """
            Generate PyQt application interfaces using Qt widgets and Python integration.
            Follow PyQt patterns for widget composition, signal-slot connections, and layout management.
            Create desktop application UIs that leverage Qt's native look and feel.
            """
    )

TechConstraintStore.register_frontend_prompt(
    prompt_component=TechConstraintComponent.ANDROID_JETPACK,
    frontend_prompt=
            """
            Develop Android UI components using Jetpack Compose and modern Android development patterns.
            Follow Android design guidelines and use Jetpack Compose's declarative UI approach.
            Integrate with Android lifecycle, navigation, and state management using Jetpack libraries.
            """
    )

TechConstraintStore.register_frontend_prompt(
    prompt_component=TechConstraintComponent.NO_FRAMEWORK,
    frontend_prompt=
            """
            Generate vanilla HTML, CSS, and JavaScript without external frameworks or libraries.
            Use modern web standards and browser APIs for component functionality.
            Focus on lightweight, performant solutions using only native web technologies.
            """
    )

