"""A text component."""

from __future__ import annotations

from reflex.vars.base import Var

from reflex_chakra.components import ChakraComponent


class Text(ChakraComponent):
    """Render a paragraph of text."""

    tag = "Text"

    # Override the tag. The default tag is `<p>`.
    as_: Var[str]

    # Truncate text after a specific number of lines. It will render an ellipsis when the text exceeds the width of the viewport or max_width prop.
    no_of_lines: Var[int]
