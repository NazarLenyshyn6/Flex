""" 
This module offers a ready-to-use server instance for users who prefer to run
a standard setup without creating custom configurations. It encapsulates
common settings and components that enable immediate use of the server
functionality out of the box.

Intended for users who want to quickly start with a working server and
avoid manual configuration steps.

Running this module starts the default server.
"""


from mcp.server.fastmcp import FastMCP

from mcp_engine.mcp_factory import MCPFactory
from prompt_engine.prompt_component import (
    TaskContextComponent, 
    ModalityComponent, 
    TechConstraintComponent, 
    OutputControlComponent, 
    )

# Construct and configure the FastMCP server
mcp: FastMCP = (MCPFactory()
                .add_frontend_generation_prompt(
                    name="frontend_generation",
                    description="Returns setup instructions for building a UI from images and api_contract",
                    prompt_components=[
                        TaskContextComponent.UI_GENERATION,
                        ModalityComponent.IMAGE_TEXT,
                        TechConstraintComponent.FASTAPI,
                        OutputControlComponent.STRICT_COMPLIANCE
                        ]
                    )
                .get_mcp_server()
                )

if __name__ == "__main__":
    mcp.run()
    
