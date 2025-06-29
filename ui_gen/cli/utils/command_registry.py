""" 
This module helps maintain a scalable CLI architecture by allowing
commands and subgroups to self-register to parent groups via
decorators, reducing boilerplate and centralizing command registration logic.
"""


from typing import Callable, TypeVar
import click

ClickCommandOrGroup = TypeVar("ClickCommandOrGroup", bound=click.Command)


def register_to_group(parent_group: click.Group) -> Callable[[ClickCommandOrGroup], ClickCommandOrGroup]:
    """
    Decorator to register a Click command or group with a specified parent Click group.

    This decorator should be applied above the Click command or group decorator
    (e.g., @click.command() or @click.group()) to automatically add the decorated
    command or group to the given parent group.

    Example usage:

        @register_to_group(parent_group)
        @click.command()
        def cmd():
            \"\"\"Command description.\"\"\"
            ...

    Args:
        parent_group: The parent Click group instance to which the
                      decorated command or group will be added.

    Returns:
        function: A decorator that registers the decorated command or group with the parent group
                  and returns the original command or group unchanged.
    """
    def decorator(obj:ClickCommandOrGroup) -> ClickCommandOrGroup:
        parent_group.add_command(obj)
        return obj
    return decorator