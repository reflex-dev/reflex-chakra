"""A reflexive container component."""

from reflex.vars.base import Var

from reflex_chakra.components import ChakraComponent


class Flex(ChakraComponent):
    """A reflexive container component."""

    tag = "Flex"

    # How to align items in the flex.
    align: Var[str]

    # Shorthand for flexBasis style prop
    basis: Var[str]

    # Shorthand for flexDirection style prop
    direction: Var[str | list[str]]

    # Shorthand for flexGrow style prop
    grow: Var[str]

    # The way to justify the items.
    justify: Var[str]

    # Shorthand for flexWrap style prop
    wrap: Var[str | list[str]]

    # Shorthand for flexShrink style prop
    shrink: Var[str]
