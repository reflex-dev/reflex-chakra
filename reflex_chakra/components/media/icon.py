"""An icon component."""

from reflex.utils import format

from reflex_chakra.components.base import ChakraComponent


class ChakraIconComponent(ChakraComponent):
    """A component that wraps a Chakra icon component."""

    library = "@chakra-ui/icons@2.0.19"


class Icon(ChakraIconComponent):
    """An image icon."""

    tag = "None"

    @classmethod
    def create(cls, *children, **props):
        """Initialize the Icon component.

        Run some additional checks on Icon component.

        Args:
            *children: The positional arguments
            **props: The keyword arguments

        Raises:
            AttributeError: The errors tied to bad usage of the Icon component.
            ValueError: If the icon tag is invalid.

        Returns:
            The created component.
        """
        if children:
            msg = f"Passing children to Icon component is not allowed: remove positional arguments {children} to fix"
            raise AttributeError(msg)
        if "tag" not in props:
            msg = "Missing 'tag' keyword-argument for Icon"
            raise AttributeError(msg)
        if not isinstance(props["tag"], str) or props["tag"].lower() not in ICON_LIST:
            msg = f"Invalid icon tag: {props['tag']}. Please use one of the following: {sorted(ICON_LIST)}"
            raise ValueError(msg)
        props["tag"] = format.to_title_case(props["tag"]) + "Icon"
        return super().create(*children, **props)


# List of all icons.
ICON_LIST: list[str] = [
    "add",
    "arrow_back",
    "arrow_down",
    "arrow_forward",
    "arrow_left",
    "arrow_right",
    "arrow_up",
    "arrow_up_down",
    "at_sign",
    "attachment",
    "bell",
    "calendar",
    "chat",
    "check_circle",
    "check",
    "chevron_down",
    "chevron_left",
    "chevron_right",
    "chevron_up",
    "close",
    "copy",
    "delete",
    "download",
    "drag_handle",
    "edit",
    "email",
    "external_link",
    "hamburger",
    "info",
    "info_outline",
    "link",
    "lock",
    "minus",
    "moon",
    "not_allowed",
    "phone",
    "plus_square",
    "question",
    "question_outline",
    "repeat",
    "repeat_clock",
    "search",
    "search2",
    "settings",
    "small_add",
    "small_close",
    "spinner",
    "star",
    "sun",
    "time",
    "triangle_down",
    "triangle_up",
    "unlock",
    "up_down",
    "view",
    "view_off",
    "warning",
    "warning_two",
]
