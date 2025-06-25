"""A time input component."""

from reflex.vars.base import Var

from reflex_chakra.components.forms.input import Input


class TimePicker(Input):
    """A time input component."""

    # The type of input.
    type_: Var[str] = Var.create("time")
