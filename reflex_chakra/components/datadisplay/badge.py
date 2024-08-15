"""Badge component."""

from reflex_chakra.components import ChakraComponent, LiteralVariant
import reflex as rx


class Badge(ChakraComponent):
    """A badge component."""

    tag = "Badge"

    # Variant of the badge ("solid" | "subtle" | "outline")
    variant: rx.Var[LiteralVariant]

    # The color of the badge
    color_scheme: rx.Var[str]
