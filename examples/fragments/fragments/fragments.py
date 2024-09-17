"""Welcome to Reflex! This file outlines the steps to create a basic app."""
from rxconfig import config

import reflex as rx
import reflex_chakra as rc

docs_url = "https://reflex.dev/docs/getting-started/introduction"
filename = f"{config.app_name}/{config.app_name}.py"


class State(rx.State):
    """The app state."""

    pass


def raw_fragment_intro():
    """Raw fragment: Return a raw list of Reflex components, and use * to use the fragment."""
    return [
        rc.heading("This is a raw fragment", font_size="2em"),
        rc.box("Just regular Python! Use these with the * operator."),
    ]


def react_fragment_intro():
    """React fragment: Wrap the result into a `rx.fragment` to take advantage of React fragments. Use normally."""
    return rx.fragment(
        rc.heading("This is a React fragment", font_size="2em"),
        rc.box(
            "Read the fragment docs at ",
            rc.link("https://reactjs.org/docs/fragments.html"),
        ),
    )


def index():
    return rc.center(
        rc.vstack(
            *raw_fragment_intro(),
            react_fragment_intro(),
            rc.link(
                "Check out our docs!",
                href=docs_url,
                border="0.1em solid",
                padding="0.5em",
                border_radius="0.5em",
                _hover={
                    "color": "rgb(107,99,246)",
                },
            ),
            spacing="1.5em",
            font_size="2em",
        ),
        padding_top="10%",
    )


app = rx.App()
app.add_page(index)
