"""A radio component."""

from typing import Any

from reflex_chakra.components import ChakraComponent
from reflex_chakra.components.typography.text import Text
from reflex.components.component import Component
from reflex.components.core.foreach import Foreach
from reflex.event import EventHandler
from reflex.utils.types import _issubclass
from reflex.vars.base import Var


class RadioGroup(ChakraComponent):
    """A grouping of individual radio options."""

    tag = "RadioGroup"

    # State var to bind the input.
    value: Var[Any]

    # The default value.
    default_value: Var[Any]

    # The name of the form field
    name: Var[str]

    # Fired when the radio group value changes.
    on_change: EventHandler[lambda e0: [e0]]

    @classmethod
    def create(cls, *children, **props) -> Component:
        """Create a radio group component.

        Args:
            *children: The children of the component.
            **props: The props of the component.

        Returns:
            The component.
        """
        if len(children) == 1 and isinstance(children[0], list):
            children = [Radio.create(child) for child in children[0]]
        if (
            len(children) == 1
            and isinstance(children[0], Var)
            and _issubclass(children[0]._var_type, list)
        ):
            children = [Foreach.create(children[0], lambda item: Radio.create(item))]
        return super().create(*children, **props)


class Radio(Text):
    """Radios are used when only one choice may be selected in a series of options."""

    tag = "Radio"

    # Value of radio.
    value: Var[Any]

    # The default value.
    default_value: Var[Any]

    # The color scheme.
    color_scheme: Var[str]

    # If true, the radio will be initially checked.
    default_checked: Var[bool]

    # If true, the radio will be checked. You'll need to pass onChange to update its value (since it is now controlled)
    is_checked: Var[bool]

    # If true, the radio will be disabled.
    is_disabled: Var[bool]

    # If true, the radio button will be invalid. This also sets `aria-invalid` to true.
    is_invalid: Var[bool]

    # If true, the radio will be read-only
    is_read_only: Var[bool]

    # If true, the radio button will be required. This also sets `aria-required` to true.
    is_required: Var[bool]

    @classmethod
    def create(cls, *children, **props) -> Component:
        """Create a radio component.

        By default, the value is bound to the first child.

        Args:
            *children: The children of the component.
            **props: The props of the component.

        Returns:
            The radio component.
        """
        if "value" not in props:
            assert len(children) == 1
            props["value"] = children[0]
        return super().create(*children, **props)
