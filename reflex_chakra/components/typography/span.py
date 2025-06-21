"""A span component."""

from __future__ import annotations

from reflex_chakra.components import ChakraComponent
from reflex.vars.base import Var


class Span(ChakraComponent):
    """Render an inline span of text."""

    tag = "Text"

    # Override the tag. The default tag is `<span>`.
    as_: Var[str] = "span"  # type: ignore
