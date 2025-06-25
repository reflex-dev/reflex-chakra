"""A span component."""

from __future__ import annotations

from reflex.vars.base import Var

from reflex_chakra.components import ChakraComponent


class Span(ChakraComponent):
    """Render an inline span of text."""

    tag = "Text"

    # Override the tag. The default tag is `<span>`.
    as_: Var[str] = Var.create("span")
