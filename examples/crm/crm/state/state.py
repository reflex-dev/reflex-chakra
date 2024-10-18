from typing import Optional
import reflex as rx
import reflex_chakra as rc
from .models import User


class State(rx.State):
    """The app state."""

    user: Optional[User] = None
