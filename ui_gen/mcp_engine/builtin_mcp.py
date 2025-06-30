""" 
This module offers a comprehensive, production-ready MCP server instance with
multiple specialized UI generation capabilities optimized for Next.js development.
It encapsulates powerful settings and components that enable advanced UI generation
functionality out of the box.

Intended for users who want a feature-rich server with extensive UI generation
capabilities without manual configuration steps.

Running this module starts the powerful server with 15 specialized prompts.
"""


from mcp.server.fastmcp import FastMCP

from mcp_engine.mcp_factory import MCPFactory
from prompt_engine.prompt_component import (
    TaskContextComponent, 
    ModalityComponent, 
    TechConstraintComponent, 
    OutputControlComponent,
    RefinementComponent
    )



# Construct and configure the comprehensive FastMCP server
mcp: FastMCP = (MCPFactory()
                
                # Screenshot + Text to Strictly Compiled Frontend
                .add_frontend_generation_prompt(
                    name="screenshot_text_to_compiled_ui",
                    description="Generate strictly compiled Next.js components taking layout from screenshots and functionality from text descriptions",
                    prompt_components=[
                        TaskContextComponent.UI_GENERATION,
                        ModalityComponent.IMAGE,
                        ModalityComponent.TEXT,
                        TechConstraintComponent.NEXTJS,
                        TechConstraintComponent.REACT,
                        TechConstraintComponent.TAILWIND,
                        TechConstraintComponent.TYPESCRIPT,
                        OutputControlComponent.STRICT_COMPLIANCE,
                        OutputControlComponent.COPY_PASTE_READY,
                        OutputControlComponent.TYPE_ANNOTATED,
                        OutputControlComponent.FULL_MODULE
                        ]
                    )
                
                # Core UI Generation - Image to Next.js Component
                .add_frontend_generation_prompt(
                    name="nextjs_image_to_component",
                    description="Generate Next.js React components from UI images/screenshots with Tailwind CSS styling",
                    prompt_components=[
                        TaskContextComponent.UI_GENERATION,
                        ModalityComponent.IMAGE,
                        TechConstraintComponent.NEXTJS,
                        TechConstraintComponent.REACT,
                        TechConstraintComponent.TAILWIND,
                        TechConstraintComponent.TYPESCRIPT,
                        OutputControlComponent.COPY_PASTE_READY,
                        OutputControlComponent.TYPE_ANNOTATED,
                        OutputControlComponent.MOBILE_RESPONSIVE
                        ]
                    )
                
                # Sketch to Component - Wireframe to Implementation
                .add_frontend_generation_prompt(
                    name="nextjs_sketch_to_component",
                    description="Convert hand-drawn sketches and wireframes to Next.js components",
                    prompt_components=[
                        TaskContextComponent.UI_GENERATION,
                        ModalityComponent.SKETCH,
                        TechConstraintComponent.NEXTJS,
                        TechConstraintComponent.REACT,
                        TechConstraintComponent.TAILWIND,
                        TechConstraintComponent.TYPESCRIPT,
                        OutputControlComponent.COPY_PASTE_READY,
                        OutputControlComponent.MOBILE_RESPONSIVE
                        ]
                    )
                
                # Spec to Component - Requirements to Implementation
                .add_frontend_generation_prompt(
                    name="nextjs_spec_to_component",
                    description="Build Next.js components from markdown specifications and requirements",
                    prompt_components=[
                        TaskContextComponent.UI_SPEC_TO_CODE,
                        ModalityComponent.MARKDOWN_SPEC,
                        TechConstraintComponent.NEXTJS,
                        TechConstraintComponent.REACT,
                        TechConstraintComponent.TAILWIND,
                        TechConstraintComponent.TYPESCRIPT,
                        OutputControlComponent.FULL_MODULE,
                        OutputControlComponent.WITH_TESTS,
                        OutputControlComponent.TYPE_ANNOTATED
                        ]
                    )
                
                # Component Library Generator
                .add_frontend_generation_prompt(
                    name="nextjs_component_library",
                    description="Generate reusable Next.js component libraries with Storybook integration",
                    prompt_components=[
                        TaskContextComponent.UI_COMPONENT_LIB_GEN,
                        ModalityComponent.TEXT,
                        TechConstraintComponent.NEXTJS,
                        TechConstraintComponent.REACT,
                        TechConstraintComponent.TAILWIND,
                        TechConstraintComponent.TYPESCRIPT,
                        TechConstraintComponent.STORYBOOK,
                        OutputControlComponent.FULL_MODULE,
                        OutputControlComponent.WITH_TESTS,
                        OutputControlComponent.TYPE_ANNOTATED,
                        OutputControlComponent.A11Y_ENFORCED
                        ]
                    )
                
                # Form Builder - Dynamic Form Generation
                .add_frontend_generation_prompt(
                    name="nextjs_form_builder",
                    description="Generate dynamic forms from JSON schemas with validation and Next.js integration",
                    prompt_components=[
                        TaskContextComponent.UI_FORM_BUILDER,
                        ModalityComponent.JSON_SCHEMA,
                        TechConstraintComponent.NEXTJS,
                        TechConstraintComponent.REACT,
                        TechConstraintComponent.TAILWIND,
                        TechConstraintComponent.TYPESCRIPT,
                        OutputControlComponent.COPY_PASTE_READY,
                        OutputControlComponent.TYPE_ANNOTATED,
                        OutputControlComponent.A11Y_ENFORCED
                        ]
                    )
                
                # Accessibility Audit & Fix
                .add_frontend_generation_prompt(
                    name="nextjs_accessibility_audit",
                    description="Audit and improve accessibility of Next.js components for WCAG compliance",
                    prompt_components=[
                        TaskContextComponent.UI_A11Y_REVIEW,
                        ModalityComponent.HTML,
                        TechConstraintComponent.NEXTJS,
                        TechConstraintComponent.REACT,
                        TechConstraintComponent.TAILWIND,
                        OutputControlComponent.A11Y_ENFORCED,
                        OutputControlComponent.EXPLAINABLE,
                        RefinementComponent.FIX_A11Y
                        ]
                    )
                
                # Performance Optimization
                .add_frontend_generation_prompt(
                    name="nextjs_performance_optimizer",
                    description="Optimize Next.js components for performance and bundle size",
                    prompt_components=[
                        TaskContextComponent.UI_REFACTOR,
                        ModalityComponent.TEXT,
                        TechConstraintComponent.NEXTJS,
                        TechConstraintComponent.REACT,
                        TechConstraintComponent.TYPESCRIPT,
                        OutputControlComponent.PERFORMANCE_SAFE,
                        OutputControlComponent.TYPE_ANNOTATED,
                        RefinementComponent.REDUCE_BUNDLE_SIZE,
                        RefinementComponent.APPLY_BEST_PRACTICES
                        ]
                    )
                
                # Responsive Design Enhancer
                .add_frontend_generation_prompt(
                    name="nextjs_responsive_enhancer",
                    description="Add responsive design capabilities to existing Next.js components",
                    prompt_components=[
                        TaskContextComponent.UI_GENERATION,
                        ModalityComponent.HTML,
                        TechConstraintComponent.NEXTJS,
                        TechConstraintComponent.TAILWIND,
                        OutputControlComponent.MOBILE_RESPONSIVE,
                        OutputControlComponent.COPY_PASTE_READY,
                        RefinementComponent.ADD_RESPONSIVENESS,
                        RefinementComponent.FIX_VISUAL_LAYOUT
                        ]
                    )
                
                # Theme Generator
                .add_frontend_generation_prompt(
                    name="nextjs_theme_generator",
                    description="Generate comprehensive design systems and themes for Next.js applications",
                    prompt_components=[
                        TaskContextComponent.UI_THEME_GEN,
                        ModalityComponent.TEXT,
                        TechConstraintComponent.NEXTJS,
                        TechConstraintComponent.TAILWIND,
                        TechConstraintComponent.TYPESCRIPT,
                        OutputControlComponent.FULL_MODULE,
                        OutputControlComponent.DARK_MODE_SUPPORTED,
                        OutputControlComponent.EXTRACT_VARIABLES
                        ]
                    )
                
                # Testing Suite Generator
                .add_frontend_generation_prompt(
                    name="nextjs_test_generator",
                    description="Generate comprehensive test suites for Next.js components",
                    prompt_components=[
                        TaskContextComponent.UI_TEST_GEN,
                        ModalityComponent.TEXT,
                        TechConstraintComponent.NEXTJS,
                        TechConstraintComponent.REACT,
                        TechConstraintComponent.TYPESCRIPT,
                        OutputControlComponent.WITH_TESTS,
                        OutputControlComponent.TYPE_ANNOTATED,
                        OutputControlComponent.A11Y_ENFORCED
                        ]
                    )
                
                # Error Boundary Generator
                .add_frontend_generation_prompt(
                    name="nextjs_error_boundary",
                    description="Generate robust error boundaries for Next.js applications",
                    prompt_components=[
                        TaskContextComponent.UI_ERROR_BOUNDARY_GEN,
                        ModalityComponent.TEXT,
                        TechConstraintComponent.NEXTJS,
                        TechConstraintComponent.REACT,
                        TechConstraintComponent.TYPESCRIPT,
                        OutputControlComponent.FULL_MODULE,
                        OutputControlComponent.TYPE_ANNOTATED,
                        OutputControlComponent.EXPLAINABLE
                        ]
                    )
                
                # Internationalization Setup
                .add_frontend_generation_prompt(
                    name="nextjs_i18n_setup",
                    description="Set up internationalization for Next.js applications",
                    prompt_components=[
                        TaskContextComponent.UI_I18N_GEN,
                        ModalityComponent.TEXT,
                        TechConstraintComponent.NEXTJS,
                        TechConstraintComponent.REACT,
                        TechConstraintComponent.TYPESCRIPT,
                        OutputControlComponent.FULL_MODULE,
                        OutputControlComponent.INTEGRATION_READY,
                        OutputControlComponent.TYPE_ANNOTATED
                        ]
                    )
                
                # Migration Assistant
                .add_frontend_generation_prompt(
                    name="nextjs_migration_assistant",
                    description="Migrate UI components to Next.js from other frameworks",
                    prompt_components=[
                        TaskContextComponent.UI_MIGRATION,
                        ModalityComponent.HTML,
                        TechConstraintComponent.NEXTJS,
                        TechConstraintComponent.REACT,
                        TechConstraintComponent.TAILWIND,
                        TechConstraintComponent.TYPESCRIPT,
                        OutputControlComponent.COPY_PASTE_READY,
                        OutputControlComponent.TYPE_ANNOTATED
                        ]
                    )
                
                # Documentation Generator
                .add_frontend_generation_prompt(
                    name="nextjs_doc_generator",
                    description="Generate comprehensive documentation and Storybook stories for Next.js components",
                    prompt_components=[
                        TaskContextComponent.UI_DOC_GEN,
                        ModalityComponent.TEXT,
                        TechConstraintComponent.NEXTJS,
                        TechConstraintComponent.STORYBOOK,
                        TechConstraintComponent.TYPESCRIPT,
                        OutputControlComponent.FULL_MODULE,
                        OutputControlComponent.EXPLAINABLE,
                        OutputControlComponent.TYPE_ANNOTATED
                        ]
                    )
                
                # Automation Dashboard
                .add_frontend_generation_prompt(
                    name="nextjs_automation_dashboard",
                    description="Generate admin panels and automation dashboards with Next.js",
                    prompt_components=[
                        TaskContextComponent.UI_AUTOMATION_WIDGET,
                        ModalityComponent.JSON_SCHEMA,
                        TechConstraintComponent.NEXTJS,
                        TechConstraintComponent.REACT,
                        TechConstraintComponent.TAILWIND,
                        TechConstraintComponent.TYPESCRIPT,
                        OutputControlComponent.FULL_MODULE,
                        OutputControlComponent.INTEGRATION_READY,
                        OutputControlComponent.TYPE_ANNOTATED
                        ]
                    )
                
                .get_mcp_server()
                )


if __name__ == "__main__":
    mcp.run()
    