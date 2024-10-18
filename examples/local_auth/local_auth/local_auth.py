"""Main app module to demo local authentication."""
import reflex as rx
import reflex_chakra as rc

from .base_state import State
from .login import require_login
from .registration import registration_page as registration_page


def index() -> rx.Component:
    """Render the index page.

    Returns:
        A reflex component.
    """
    return rx.fragment(
        rc.color_mode_button(rc.color_mode_icon(), float="right"),
        rc.vstack(
            rc.heading("Welcome to my homepage!", font_size="2em"),
            rc.link("Protected Page", href="/protected"),
            spacing="1.5em",
            padding_top="10%",
        ),
    )


@require_login
def protected() -> rx.Component:
    """Render a protected page.

    The `require_login` decorator will redirect to the login page if the user is
    not authenticated.

    Returns:
        A reflex component.
    """
    return rc.vstack(
        rc.heading(
            "Protected Page for ", State.authenticated_user.username, font_size="2em"
        ),
        rc.link("Home", href="/"),
        rc.link("Logout", href="/", on_click=State.do_logout),
    )


app = rx.App()
app.add_page(index)
app.add_page(protected)
