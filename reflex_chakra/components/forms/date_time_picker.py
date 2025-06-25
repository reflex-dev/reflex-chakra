"""A datetime-local input component."""

from reflex.vars.base import Var

from reflex_chakra.components.forms.input import Input


class DateTimePicker(Input):
    """A datetime-local input component."""

    # The type of input.
    type_: Var[str] = Var.create("datetime-local")
