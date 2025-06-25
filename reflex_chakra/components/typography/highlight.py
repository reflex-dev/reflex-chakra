"""A highlight component."""

from reflex.components.tags.tag import Tag
from reflex.vars.base import Var

from reflex_chakra.components import ChakraComponent


class Highlight(ChakraComponent):
    """Highlights a specific part of a string."""

    tag = "Highlight"

    # A query for the text to highlight. Can be a string or a list of strings.
    query: Var[list[str]]

    # The style of the content.
    # Note: styles and style are different prop.
    styles: Var[dict] = Var.create(
        {"px": "2", "py": "1", "rounded": "full", "bg": "teal.100"}
    )

    def _render(self) -> Tag:
        return super()._render().add_props(styles=self.style)
