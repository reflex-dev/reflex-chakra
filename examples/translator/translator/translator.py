"""Welcome to Reflex! This file outlines the steps to create a basic app."""

# Import reflex.
from datetime import datetime
from googletrans import Translator

import reflex as rx
import reflex_chakra as rc
from reflex.base import Base

from .langs import langs

trans = Translator()

class Message(Base):
    original_text: str
    text: str
    created_at: str
    to_lang: str


class State(rx.State):
    """The app state."""

    text: str = ""
    messages: list[Message] = []
    lang: str = "Chinese (Simplified)"

    @rx.var
    def output(self) -> str:
        if not self.text.strip():
            return "Translations will appear here."
        translated = trans.translate(self.text,dest=self.lang)
        return translated.text

    def post(self):
        self.messages = [
            Message(
                original_text=self.text,
                text=self.output,
                created_at=datetime.now().strftime("%B %d, %Y %I:%M %p"),
                to_lang=self.lang,
            )
        ] + self.messages


# Define views.


def header():
    """Basic instructions to get started."""
    return rc.box(
        rc.text("Translator 🗺", font_size="2rem"),
        rc.text(
            "Translate things and post them as messages!",
            margin_top="0.5rem",
            color="#666",
        ),
    )


def down_arrow():
    return rc.vstack(
        rc.icon(
            tag="arrow_down",
            color="#666",
        )
    )


def text_box(text):
    return rc.text(
        text,
        background_color="#fff",
        padding="1rem",
        border_radius="8px",
    )


def message(message):
    return rc.box(
        rc.vstack(
            text_box(message.original_text),
            down_arrow(),
            text_box(message.text),
            rc.box(
                rc.text(message.to_lang),
                rc.text(" · ", margin_x="0.3rem"),
                rc.text(message.created_at),
                display="flex",
                font_size="0.8rem",
                color="#666",
            ),
            spacing="0.3rem",
            align_items="left",
        ),
        background_color="#f5f5f5",
        padding="1rem",
        border_radius="8px",
    )


def smallcaps(text, **kwargs):
    return rc.text(
        text,
        font_size="0.7rem",
        font_weight="bold",
        text_transform="uppercase",
        letter_spacing="0.05rem",
        **kwargs,
    )


def output():
    return rc.box(
        rc.box(
            smallcaps(
                "Output",
                color="#aeaeaf",
                background_color="white",
                padding_x="0.1rem",
            ),
            position="absolute",
            top="-0.5rem",
        ),
        rc.text(State.output),
        padding="1rem",
        border="1px solid #eaeaef",
        margin_top="1rem",
        border_radius="8px",
        position="relative",
    )


def index():
    """The main view."""
    return rc.container(
        header(),
        rc.input(
            placeholder="Text to translate",
            on_blur=State.set_text,
            margin_top="1rem",
            border_color="#eaeaef",
        ),
        rc.select(
            list(langs.keys()),
            value=State.lang,
            placeholder="Select a language",
            on_change=State.set_lang,
            margin_top="1rem",
        ),
        output(),
        rc.button("Post", on_click=State.post, margin_top="1rem"),
        rc.vstack(
            rx.foreach(State.messages, message),
            margin_top="2rem",
            spacing="1rem",
            align_items="left",
        ),
        padding="2rem",
        max_width="600px",
    )


app = rx.App()
app.add_page(index, title="Translator")
