"""A AspectRatio component."""

from reflex.vars.base import Var

from reflex_chakra.components import ChakraComponent


class AspectRatio(ChakraComponent):
    """AspectRatio component is used to embed responsive videos and maps, etc."""

    tag = "AspectRatio"

    # The aspect ratio of the Box
    ratio: Var[float]
