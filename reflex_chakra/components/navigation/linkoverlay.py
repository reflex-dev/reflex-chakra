"""Link overlay components."""

from reflex.vars.base import Var

from reflex_chakra.components import ChakraComponent


class LinkOverlay(ChakraComponent):
    """Wraps child component in a link."""

    tag = "LinkOverlay"

    # If true, the link will open in new tab
    is_external: Var[bool]

    # Href of the link overlay.
    href: Var[str]


class LinkBox(ChakraComponent):
    """The LinkBox lifts any nested links to the top using z-index to ensure proper keyboard navigation between links."""

    tag = "LinkBox"
