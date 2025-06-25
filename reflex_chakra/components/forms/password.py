"""A password input component."""

from reflex.vars.base import Var

from reflex_chakra.components.forms.input import Input


class Password(Input):
    """A password input component."""

    # The type of input.
    type_: Var[str] = Var.create("password")
