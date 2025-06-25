"""Tooltip components."""

from __future__ import annotations

from reflex.event import EventHandler, no_args_event_spec
from reflex.vars.base import Var

from reflex_chakra.components import ChakraComponent, LiteralChakraDirection


class Tooltip(ChakraComponent):
    """A tooltip message to appear."""

    tag = "Tooltip"

    # The padding required to prevent the arrow from reaching the very edge of the popper.
    arrow_padding: Var[int]

    # The color of the arrow shadow.
    arrow_shadow_color: Var[str]

    # Size of the arrow.
    arrow_size: Var[int]

    # Delay (in ms) before hiding the tooltip
    delay: Var[int]

    # If true, the tooltip will hide on click
    close_on_click: Var[bool]

    # If true, the tooltip will hide on pressing Esc key
    close_on_esc: Var[bool]

    # If true, the tooltip will hide while the mouse is down
    close_on_mouse_down: Var[bool]

    # If true, the tooltip will be initially shown
    default_is_open: Var[bool]

    # Theme direction ltr or rtl. Popper's placement will be set accordingly
    direction: Var[LiteralChakraDirection]

    # The distance or margin between the reference and popper. It is used internally to create an offset modifier. NB: If you define offset prop, it'll override the gutter.
    gutter: Var[int]

    # If true, the tooltip will show an arrow tip
    has_arrow: Var[bool]

    # If true, the tooltip with be disabled.
    is_disabled: Var[bool]

    # If true, the tooltip will be open.
    is_open: Var[bool]

    # The label of the tooltip
    label: Var[str]

    # Delay (in ms) before showing the tooltip
    open_delay: Var[int]

    # The placement of the popper relative to its reference.
    placement: Var[str]

    # If true, the tooltip will wrap its children in a `<span/>` with `tabIndex=0`
    should_wrap_children: Var[bool]

    # Fired when the tooltip is closing.
    on_close: EventHandler[no_args_event_spec]

    # Fired when the tooltip is opened.
    on_open: EventHandler[no_args_event_spec]
