"""An email input component."""

from reflex_chakra.components.forms.input import Input
from reflex.vars.base import Var


class Email(Input):
    """An email input component."""

    # The type of input.
    type_: Var[str] = "email"  # type: ignore
