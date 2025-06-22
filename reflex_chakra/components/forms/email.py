"""An email input component."""

from reflex.vars.base import Var

from reflex_chakra.components.forms.input import Input


class Email(Input):
    """An email input component."""

    # The type of input.
    type_: Var[str] = Var.create("email")
