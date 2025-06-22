"""Avatar components."""

from __future__ import annotations

from reflex.event import EventHandler, no_args_event_spec
from reflex.vars.base import Var

from reflex_chakra.components.base import ChakraComponent, LiteralAvatarSize


class Avatar(ChakraComponent):
    """The image that represents the user."""

    tag = "Avatar"

    # The default avatar used as fallback when name, and src is not specified.
    icon: Var[str]

    # The label of the icon.
    icon_label: Var[str]

    # If true, opt out of the avatar's fallback logic and renders the img at all times.
    ignore_fallback: Var[bool]

    # The name of the person in the avatar.
    name: Var[str]

    # If true, the Avatar will show a border around it. Best for a group of avatars.
    show_border: Var[bool]

    # The image url of the Avatar.
    src: Var[str]

    # List of sources to use for different screen resolutions.
    src_set: Var[str]

    # "2xs" | "xs" | "sm" | "md" | "lg" | "xl" | "2xl" | "full"
    size: Var[LiteralAvatarSize]

    # Fired when the image fails to load.
    on_error: EventHandler[no_args_event_spec]


class AvatarBadge(ChakraComponent):
    """A wrapper that displays its content on the right corner of the avatar."""

    tag = "AvatarBadge"


class AvatarGroup(ChakraComponent):
    """A wrapper to stack multiple Avatars together."""

    tag = "AvatarGroup"

    # The maximum number of visible avatars.
    max_: Var[int]

    # The space between the avatars in the group.
    spacing: Var[int]
