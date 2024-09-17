"""Sign up page. Uses auth_layout to render UI shared with the login page."""
import reflex_chakra as rc
from twitter.layouts import auth_layout
from twitter.state.auth import AuthState


def signup():
    """The sign up page."""
    return auth_layout(
        rc.box(
            rc.input(placeholder="Username", on_blur=AuthState.set_username, mb=4),
            rc.input(
                type_="password",
                placeholder="Password",
                on_blur=AuthState.set_password,
                mb=4,
            ),
            rc.input(
                type_="password",
                placeholder="Confirm password",
                on_blur=AuthState.set_confirm_password,
                mb=4,
            ),
            rc.button(
                "Sign up",
                on_click=AuthState.signup,
                bg="blue.500",
                color="white",
                _hover={"bg": "blue.600"},
            ),
            align_items="left",
            bg="white",
            border="1px solid #eaeaea",
            p=4,
            max_width="400px",
            border_radius="lg",
        ),
        rc.text(
            "Already have an account? ",
            rc.link("Sign in here.", href="/", color="blue.500"),
            color="gray.600",
        ),
    )
