"""A line to divide parts of the layout."""

from typing import Literal

from reflex.vars.base import Var

from reflex_chakra.components import ChakraComponent, LiteralDividerVariant

LiteralLayout = Literal["horizontal", "vertical"]


class Divider(ChakraComponent):
    """Dividers are used to visually separate content in a list or group."""

    tag = "Divider"

    # Pass the orientation prop and set it to either horizontal or vertical. If the vertical orientation is used, make sure that the parent element is assigned a height.
    orientation: Var[LiteralLayout]

    # Variant of the divider ("solid" | "dashed")
    variant: Var[LiteralDividerVariant]
