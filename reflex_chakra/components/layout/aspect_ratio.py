"""A AspectRatio component."""

from reflex_chakra.components import ChakraComponent
from reflex.vars.base import Var


class AspectRatio(ChakraComponent):
    """AspectRatio component is used to embed responsive videos and maps, etc."""

    tag = "AspectRatio"

    # The aspect ratio of the Box
    ratio: Var[float]
