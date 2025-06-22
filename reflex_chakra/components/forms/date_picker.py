"""A date input component."""

from reflex.vars.base import Var

from reflex_chakra.components.forms.input import Input


class DatePicker(Input):
    """A date input component."""

    # The type of input.
    type_: Var[str] = Var.create("date")
