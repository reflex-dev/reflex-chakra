from crm.components import navbar
from crm.components import crm
from crm.state import State
import reflex as rx
import reflex_chakra as rc


def index():
    return rc.vstack(
        navbar(),
        rx.cond(
            State.user,
            crm(),
            rc.vstack(
                rc.heading("Welcome to Pyneknown!"),
                rc.text(
                    "This Reflex example demonstrates how to build a fully-fledged customer relationship management (CRM) interface."
                ),
                rc.link(
                    rc.button(
                        "Log in to get started", color_scheme="blue", underline="none"
                    ),
                    href="/login",
                ),
                max_width="500px",
                text_align="center",
                spacing="1rem",
            ),
        ),
        spacing="1.5rem",
    )
