from crm.state import LoginState
from crm.components import navbar
import reflex as rx
import reflex_chakra as rc


def login():
    return rc.vstack(
        navbar(),
        rc.box(
            rc.heading("Log in", margin_bottom="1rem"),
            rc.input(
                type_="email",
                placeholder="Email",
                margin_bottom="1rem",
                on_change=LoginState.set_email_field,
            ),
            rc.input(
                type_="password",
                placeholder="Password",
                margin_bottom="1rem",
                on_change=LoginState.set_password_field,
            ),
            rc.button("Log in", on_click=LoginState.log_in),
            rc.box(
                rc.link(
                    "Or sign up with this email and password",
                    href="#",
                    on_click=LoginState.sign_up,
                ),
                margin_top="0.5rem",
            ),
            max_width="350px",
            flex_direction="column",
        ),
    )
