"""A flexbox container."""

from reflex_chakra.components import ChakraComponent
from reflex.vars.base import Var


class Container(ChakraComponent):
    """A flexbox container that centers its children and sets a max width."""

    tag = "Container"

    # If true, container will center its children regardless of their width.
    center_content: Var[bool]
