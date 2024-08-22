import flexdown
import reflex as rx
import reflex_chakra as rc
import black
import textwrap
from typing import Any
from .blocks import headings, typography, code
from ..constants import fonts

demo_box_style = {
    "padding": "24px",
    "width": "100%",
    "overflow_x": "auto",
    "border-radius": "12px",
    "border": f"1px solid {rx.color('slate', 4)}",
    "background": f"{rx.color('slate', 2)}",
    "align_items": "center",
    "justify_content": "center",
}


@rx.memo
def code_block(code: str, language: str):
    return rx.box(
        rx.code_block(
            code,
            border_radius="12px",
            background="transparent",
            language=language,
            code_tag_props={
                "style": {
                    "fontFamily": "inherit",
                }
            },
            font_family="Source Code Pro",
            color=rx.color("slate", 12),
            padding="20px",
            style=fonts.code,
            margin="0",
            # TODO: use this when it's looking good
            # can_copy=True,
        ),
        rx.button(
            rx.icon(
                "clipboard",
                color=rx.color("slate", 9),
                transition="color 0.035s ease-out",
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
                "style": {
                    "fontFamily": "inherit",
                }
            },
            padding="20px",
            margin="0",
            # TODO: use this when it's looking good
            # can_copy=True,
        ),
        rx.button(
            rx.icon(
                "clipboard",
                color=rx.color("slate", 9),
                transition="color 0.035s ease-out",
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


def docdemobox(*children, **props) -> rx.Component:
    """Create a documentation demo box with the output of the code.

    Args:
        children: The children to display.

    Returns:
        The styled demo box.
    """
    return rx.vstack(
        *children,
        style=demo_box_style,
        **props,
    )


def doccode(
    code: str,
    language: str = "python",
    lines: tuple[int, int] | None = None,
    theme: str = "light",
) -> rx.Component:
    """Create a documentation code snippet.

    Args:
        code: The code to display.
        language: The language of the code.
        lines: The start/end lines to display.
        props: Props to apply to the code snippet.

    Returns:
        The styled code snippet.
    """
    # For Python snippets, lint the code with black.
    if language == "python":
        code = black.format_str(
            textwrap.dedent(code), mode=black.FileMode(line_length=60)
        ).strip()

    # If needed, only display a subset of the lines.
    if lines is not None:
        code = textwrap.dedent(
            "\n".join(code.strip().split("\n")[lines[0] : lines[1]])
        ).strip()

    # Create the code snippet.
    cb = code_block_dark if theme == "dark" else code_block
    return cb(
        code=code,
        language=language,
    )


def docdemo(
    code: str,
    state: str | None = None,
    comp: rx.Component | None = None,
    context: bool = False,
    demobox_props: dict[str, Any] | None = None,
    theme: str | None = None,
    **props,
) -> rx.Component:
    """Create a documentation demo with code and output.

    Args:
        code: The code to render the component.
        state: Code for any state needed for the component.
        comp: The pre-rendered component.
        context: Whether to wrap the render code in a function.
        props: Additional props to apply to the component.

    Returns:
        The styled demo.
    """
    demobox_props = demobox_props or {}
    # Render the component if necessary.
    if comp is None:
        comp = eval(code)

    # Wrap the render code in a function if needed.
    if context:
        code = f"""def index():
        return {code}
        """

    # Add the state code
    if state is not None:
        code = state + code

    if demobox_props.pop("toggle", False):
        return rx.tabs.root(
            rx.tabs.list(
                rx.tabs.trigger(
                    rx.hstack(
                        "UI",
                    ),
                    # style=tab_style,
                    value="tab1",
                ),
                rx.tabs.trigger(
                    rx.hstack(
                        "Code",
                    ),
                    # style=tab_style,
                    value="tab2",
                ),
                justify_content="end",
            ),
            rx.tabs.content(
                rx.box(
                    docdemobox(comp, **(demobox_props or {})),
                    margin_bottom="1em",
                    margin_top="1em",
                ),
                value="tab1",
            ),
            rx.tabs.content(
                doccode(code, theme=theme),
                value="tab2",
            ),
            default_value="tab1",
        )
    # Create the demo.
    return rx.vstack(
        docdemobox(comp, **(demobox_props or {})),
        doccode(code, theme=theme),
        width="100%",
        padding_y="1em",
        gap="1em",
        **props,
    )


class DemoBlock(flexdown.blocks.Block):
    """A block that displays a component along with its code."""

    starting_indicator = "```python demo"
    ending_indicator = "```"
    include_indicators = True
    theme: str = None

    def render(self, env) -> rx.Component:
        lines = self.get_lines(env)
        code = "\n".join(lines[1:-1])

        args = lines[0].removeprefix(self.starting_indicator).split()

        exec_mode = env.get("__exec", False)
        comp = ""

        for arg in args:
            if arg.startswith("id="):
                comp_id = arg.rsplit("id=")[-1]
                break
        else:
            comp_id = None

        if "exec" in args:
            env["__xd"].exec(code, env, self.filename)
            if not exec_mode:
                comp = env[list(env.keys())[-1]]()
        elif exec_mode:
            return comp
        elif "box" in args:
            comp = eval(code, env, env)
            return rx.box(docdemobox(comp), margin_bottom="1em", id=comp_id)
        else:
            comp = eval(code, env, env)

        # Sweep up additional CSS-like props to apply to the demobox itself
        demobox_props = {}
        for arg in args:
            prop, equals, value = arg.partition("=")
            if equals:
                demobox_props[prop] = value

        if "toggle" in args:
            demobox_props["toggle"] = True

        return docdemo(
            code, comp=comp, demobox_props=demobox_props, theme=self.theme, id=comp_id
        )


component_map = {
    "h1": lambda text: headings.h1_comp_xd(text=text),
    "h2": lambda text: headings.h2_comp_xd(text=text),
    "h3": lambda text: headings.h3_comp_xd(text=text),
    "h4": lambda text: headings.h4_comp_xd(text=text),
    "p": lambda text: typography.text_comp(text=text),
    "li": lambda text: typography.list_comp(text=text),
    "a": typography.doclink2,
    "code": lambda text: typography.code_comp(text=text),
    "codeblock": code.code_block_markdown,
}

xd = flexdown.Flexdown(
    block_types=[DemoBlock],
    component_map=component_map,
)
xd.clear_modules()


def markdown(text):
    return xd.get_default_block().render_fn(content=text)
