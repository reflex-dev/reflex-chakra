"""A heading component."""

from reflex.vars.base import Var

from reflex_chakra.components import ChakraComponent, LiteralHeadingSize


class Heading(ChakraComponent):
    """A page heading."""

    tag = "Heading"

    # Override the tag. The default tag is `<h2>`.
    as_: Var[str]

    # "4xl" | "3xl" | "2xl" | "xl" | "lg" | "md" | "sm" | "xs"
    size: Var[LiteralHeadingSize]
