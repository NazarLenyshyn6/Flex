"""
This module defines the `MCPFactory`, a structured interface for building FastMCP-based
prompt generation servers using modular `PromptComponent`s.

Features:
- Initializes FastMCP instance with specified name and dependencies
- Adds frontend and backend generation prompts from typed component lists
- Uses `PromptComposer` for dynamic prompt assembly
"""


from typing import Any, List, Self, Literal

from pydantic import (
    BaseModel,
    Field,
    validate_call
    )
from mcp.server.fastmcp import FastMCP

from prompt_engine.prompt_composer import PromptComposer
from prompt_engine.prompt_component import PromptComponent

class MCPFactory(BaseModel):
    """
    Factory for building and configuring a FastMCP server with dynamic generation prompts.
    """

    dependencies: List[str] = Field(default_factory=list)

    def model_post_init(self, context: Any) -> None:
        """
        Pydantic post-initialization hook to construct the internal FastMCP.
        """
        self._mcp: FastMCP = FastMCP(
            dependencies=self.dependencies
            )

    def _add_generation_prompt(
        self,
        layer: Literal["frontend", "backend"],
        name: str,
        description: str,
        prompt_components: List[PromptComponent]
        ) -> Self:
        """
        Internal method to register a prompt with the FastMCP server.

        Args:
            layer: Either "frontend" or "backend".
            name: The identifier name of the prompt.
            description: Human-readable description of the prompt.
            prompt_components: List of prompt components to be composed.

        Returns:
            Self: for fluent chaining.
        """
        if layer == "frontend":
            generation_prompt = PromptComposer.compose_frontend_prompt(prompt_components)
        else:
            generation_prompt = PromptComposer.compose_backend_prompt(prompt_components)
        self._mcp.prompt(name=name, description=description)(lambda: generation_prompt)
        return self

    @validate_call()
    def add_frontend_generation_prompt(
        self,
        name: str,
        description: str,
        prompt_components: List[PromptComponent]
        ) -> Self:
        """
        Adds a frontend generation prompt to the MCP server.

        Returns:
            Self: for fluent chaining.
        """
        return self._add_generation_prompt(
            layer="frontend",
            name=name,
            description=description,
            prompt_components=prompt_components
            )

    @validate_call()
    def add_backend_generation_prompt(
        self,
        name: str,
        description: str,
        prompt_components: List[PromptComponent]
        ) -> Self:
        """
        Adds a backend generation prompt to the MCP server.

        Returns:
            Self: for fluent chaining.
        """
        return self._add_generation_prompt(
            layer="backend",
            name=name,
            description=description,
            prompt_components=prompt_components
            )

    def get_mcp_server(self) -> FastMCP:
        """
        Returns the configured FastMCP instance.

        Returns:
            FastMCP
        """
        return self._mcp