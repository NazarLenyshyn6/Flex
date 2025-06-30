"""
This module defines enumerations for various modular components of a dynamic prompt system used in backend/frontend
code generation tasks. Each component represents a category of input or context that contributes
to the formation of structured and configurable prompts.

These enums allow for a strongly typed, explicit prompt configuration experience.
"""


from enum import Enum, auto


class PromptComponent(Enum):
    """Base enumeration for all prompt components. Acts as a marker interface for type safety and inheritance."""
    ...


class TaskContextComponent(PromptComponent):
    """Defines the primary intent or goal of the prompt generation process."""

    UI_GENERATION = auto()          # Generate standard UI components (forms, buttons, navbars, etc.)
    UI_FIX_BUGS = auto()            # Detect and repair UI layout/styling/behavior bugs
    UI_THEME_GEN = auto()           # Create or extend design tokens and themes
    UI_A11Y_REVIEW = auto()         # Audit and improve accessibility (ARIA, WCAG)
    UI_COMPONENT_LIB_GEN = auto()   # Generate reusable component libraries / design systems
    UI_SPEC_TO_CODE = auto()        # Convert specs (Markdown, Figma) to code
    UI_TEST_GEN = auto()            # Generate tests (unit/E2E) for UI components
    UI_REFACTOR = auto()            # Refactor for performance, readability, or structure
    UI_MIGRATION = auto()           # Migrate UI from one framework to another
    UI_DOC_GEN = auto()             # Generate Storybook or inline documentation
    UI_AUTOMATION_WIDGET = auto()   # Build tools like admin panels or dashboards
    UI_ERROR_BOUNDARY_GEN = auto()  # Scaffold robust error boundaries
    UI_I18N_GEN = auto()            # Scaffold localization/internationalization support
    UI_FORM_BUILDER = auto()        # Auto-generate forms from JSON/schema/spec


class ModalityComponent(PromptComponent):
    """Specifies the modality of the input used to generate UI prompts."""

    TEXT = auto()             # Free-form prompt or command text
    IMAGE = auto()            # UI screenshot or rendered component
    SKETCH = auto()           # Hand-drawn sketch or whiteboard wireframe
    MARKDOWN_SPEC = auto()    # Markdown-formatted spec or requirement
    JSON_SCHEMA = auto()      # Backend data model or schema
    HTML = auto()             # Existing HTML (for audit/migration)
    YAML_UI_CONFIG = auto()   # DSL-style YAML config describing UI
    DSL_UI_LANG = auto()      # Domain-specific language (e.g., Retool DSL)


class TechConstraintComponent(PromptComponent):
    """Describes which technologies, libraries, or design systems the output must conform to."""

    REACT = auto()
    NEXTJS = auto()
    VUE = auto()
    SVELTE = auto()
    TAILWIND = auto()
    CHAKRA_UI = auto()
    MATERIAL_UI = auto()
    STORYBOOK = auto()
    TYPESCRIPT = auto()
    FLUTTER = auto()
    REACT_NATIVE = auto()
    ANT_DESIGN = auto()
    BOOTSTRAP = auto()
    WEB_COMPONENTS = auto()
    PYQT = auto()
    ANDROID_JETPACK = auto()
    NO_FRAMEWORK = auto()


class OutputControlComponent(PromptComponent):
    """Controls the style, format, and functional requirements of the generated code."""

    STRICT_COMPLIANCE = auto()      # Must follow spec or pattern exactly
    COPY_PASTE_READY = auto()       # Can be dropped directly into codebase
    NO_IMPORTS = auto()             # Must not include external imports
    FULL_MODULE = auto()            # Includes imports, styles, setup
    SNIPPET_ONLY = auto()           # Output only code snippet body
    EXPLAINABLE = auto()            # Include inline/block comments
    NO_COMMENTS = auto()            # Bare code only
    WITH_TESTS = auto()             # Include tests in output
    A11Y_ENFORCED = auto()          # Must pass accessibility audit
    TYPE_ANNOTATED = auto()         # Must include types (JSDoc, TS)
    PERFORMANCE_SAFE = auto()       # Avoid anti-patterns (rerenders, bloat)
    EXTRACT_VARIABLES = auto()      # Extract hardcoded values as tokens
    MOBILE_RESPONSIVE = auto()      # Must be responsive
    DARK_MODE_SUPPORTED = auto()    # Includes dark mode compatibility
    INTEGRATION_READY = auto()      # Should hook into app layout/store
    
    
class RefinementComponent(PromptComponent):
    """Specifies post-generation improvement or bug-fix directives."""

    FIX_VISUAL_LAYOUT = auto()             # Fix spacing, alignment, layout issues
    FIX_A11Y = auto()                      # Add accessibility features (labels, ARIA)
    ADD_RESPONSIVENESS = auto()           # Ensure proper rendering on mobile/tablet
    FIX_INTERACTIVITY = auto()            # Make buttons/inputs functional or correct behavior
    EXTRACT_CONSTANTS = auto()            # Extract magic values to variables
    ADD_COMMENTS = auto()                 # Add helpful developer comments
    REMOVE_DUPLICATION = auto()           # Refactor repeated code into reusable parts
    APPLY_BEST_PRACTICES = auto()         # Clean code to follow modern UI best practices
    SPLIT_COMPONENT = auto()              # Break large monolith into multiple small components
    ADD_TYPES = auto()                    # Add TypeScript or PropTypes
    UPGRADE_SEMANTICS = auto()            # Use proper HTML5 tags (e.g., `<section>`, `<nav>`)
    IMPROVE_CONTRAST = auto()             # Adjust colors for better visual contrast
    FIX_STATE_MANAGEMENT = auto()         # Correct issues with hooks, state, props
    REDUCE_BUNDLE_SIZE = auto()           # Simplify logic, lazy-load where needed
    ADD_LOADING_STATES = auto()           # Insert loading indicators for async flows
    ENFORCE_NAMING_CONVENTIONS = auto()   # Rename components, props, CSS classes
