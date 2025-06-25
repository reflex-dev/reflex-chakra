"""Code block components for documentation pages."""

import reflex as rx

from rcweb.constants import css, fonts


@rx.memo
def code_block(code: str, language: str):
    return rx.box(
        rx.code_block(
            code,
            border_radius="12px",
            background="transparent",
            language=language,
            code_tag_props={
                "font_family": "inherit",
            },
            font_family="Source Code Pro",
            color=rx.color("slate", 12),
            padding="20px",
            style=fonts.code,
            margin="0",
        ),
        rx.button(
            rx.icon(
                "clipboard",
                color=rx.color("slate", 9),
                transition="color 0.035s ease-out",
                display="flex",
                justify_content="center",
                align_items="center",
                _hover={
                    "color": rx.color("slate", 11),
                },
            ),
            on_click=rx.set_clipboard(code),
            position="absolute",
            top="30px",
            right="30px",
            padding_x="0px",
            height="auto",
            background="transparent",
            cursor="pointer",
            _hover={
                "background": "transparent",
            },
            _active={
                "size": "0.8em",
                "transform": "scale(0.8)",
            },
        ),
        padding="8px",
        border_radius="12px",
        border=f"1px solid {rx.color('slate', 4)}",
        background_color=rx.color("slate", 2),
        position="relative",
        margin_bottom="1em",
        margin_top="1em",
        width="100%",
    )


@rx.memo
def code_block_dark(code: str, language: str):
    return rx.box(
        rx.code_block(
            code,
            border_radius="6px",
            theme="dark",
            background="transparent",
            language=language,
            code_tag_props={
                "font_family": "inherit",
            },
            padding="20px",
            margin="0",
        ),
        rx.button(
            rx.icon(
                "clipboard",
                color=rx.color("slate", 9),
                transition="color 0.035s ease-out",
                display="flex",
                justify_content="center",
                align_items="center",
                _hover={
                    "color": rx.color("slate", 11),
                },
            ),
            on_click=rx.set_clipboard(code),
            position="absolute",
            top="30px",
            right="30px",
            padding_x="0px",
            height="auto",
            background="transparent",
            _hover={
                "opacity": 0.5,
                "cursor": "pointer",
                "background": "transparent",
            },
            _active={
                "size": "0.8em",
                "transform": "scale(0.8)",
            },
        ),
        border_radius="6px",
        border=f"1px solid {rx.color('slate', 4)}",
        background_color=rx.color("slate", 2),
        position="relative",
        margin_bottom="1em",
        margin_top="1em",
        width="100%",
    )


def code_block_markdown(*children, **props):
    language = props.get("language", "none")
    return code_block(code=children[0], language=language)


def code_block_markdown_dark(*children, **props):
    language = props.get("language", "none")
    return code_block_dark(code=children[0], language=language)


def doccmdoutput(
    command: str,
    output: str,
) -> rx.Component:
    """Create a documentation code snippet.

    Args:
        command: The command to display.
        output: The output of the command.
        theme: The theme of the component.

    Returns:
        The styled command and its example output.
    """
    return rx.flex(
        rx.flex(
            rx.lucide.icon(tag="chevrons-right", color="white", width=18, height=18),
            rx.code_block(
                command,
                border_radius=css.DOC_BORDER_RADIUS,
                background="transparent",
                theme="a11y-dark",
                language="bash",
                code_tag_props={
                    "font_family": "inherit",
                },
                style=fonts.code,
                font_family="Source Code Pro",
            ),
            rx.button(
                rx.icon(
                    "clipboard",
                    color=rx.color("slate", 2),
                    transition="color 0.035s ease-out",
                    display="flex",
                    justify_content="center",
                    align_items="center",
                    _hover={
                        "color": rx.color("slate", 5),
                    },
                ),
                height="auto",
                background="transparent",
                cursor="pointer",
                _hover={
                    "background": "transparent",
                },
                _active={
                    "size": "0.8em",
                    "transform": "scale(0.8)",
                },
                on_click=rx.set_clipboard(command),
                position="absolute",
                top="1.75em",
                right="0.5em",
            ),
            direction="row",
            align="center",
            spacing="1",
            margin_left="1em",
        ),
        rx.divider(size="4", color_scheme="green"),
        rx.flex(
            rx.code_block(
                output,
                border_radius="12px",
                background="transparent",
                theme="nord",
                language="log",
                code_tag_props={
                    "font_family": "inherit",
                },
                style=fonts.code,
                font_family="Source Code Pro",
            ),
        ),
        direction="column",
        spacing="2",
        border_radius="12px",
        border=f"1px solid {rx.color('slate', 5)}",
        position="relative",
        margin_y="1em",
        width="100%",
        background_color="black",
    )
