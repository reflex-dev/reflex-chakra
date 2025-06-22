"""Badge component."""

from reflex.vars.base import Var

from reflex_chakra.components import ChakraComponent, LiteralVariant


class Badge(ChakraComponent):
    """A badge component."""

    tag = "Badge"

    # Variant of the badge ("solid" | "subtle" | "outline")
    variant: Var[LiteralVariant]

    # The color of the badge
    color_scheme: Var[str]
