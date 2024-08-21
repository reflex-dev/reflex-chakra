import reflex as rx
import reflex_chakra as rc
from typing import Callable, Type, Any, Literal, Union, get_origin, get_args
import inspect
import flexdown
from reflex.components.el.elements.base import BaseHTML
import os
from ..utils.flexdown import xd, markdown, docdemobox
from ..utils.sidebar import sidebar as sb
from ..constants import css, fonts
import textwrap
import mistletoe

flat_items = []

TYPE_COLORS = {
    "int": "red",
    "float": "orange",
    "str": "yellow",
    "bool": "teal",
    "Component": "purple",
    "List": "blue",
    "Dict": "blue",
    "Tuple": "blue",
    "None": "gray",
    "Figure": "green",
    "Literal": "gray",
    "Union": "gray",
}

EVENTS = {
    "on_focus": {
        "description": "Function or event handler called when the element (or some element inside of it) receives focus. For example, it is called when the user clicks on a text input."
    },
    "on_blur": {
        "description": "Function or event handler called when focus has left the element (or left some element inside of it). For example, it is called when the user clicks outside of a focused text input."
    },
    "on_change": {
        "description": "Function or event handler called when the value of an element has changed. For example, it is called when the user types into a text input each keystoke triggers the on change."
    },
    "on_click": {
        "description": "Function or event handler called when the user clicks on an element. For example, it’s called when the user clicks on a button."
    },
    "on_context_menu": {
        "description": "Function or event handler called when the user right-clicks on an element. For example, it is called when the user right-clicks on a button."
    },
    "on_double_click": {
        "description": "Function or event handler called when the user double-clicks on an element. For example, it is called when the user double-clicks on a button."
    },
    "on_mouse_up": {
        "description": "Function or event handler called when the user releases a mouse button on an element. For example, it is called when the user releases the left mouse button on a button."
    },
    "on_mouse_down": {
        "description": "Function or event handler called when the user presses a mouse button on an element. For example, it is called when the user presses the left mouse button on a button."
    },
    "on_mouse_enter": {
        "description": "Function or event handler called when the user’s mouse enters an element. For example, it is called when the user’s mouse enters a button."
    },
    "on_mouse_leave": {
        "description": "Function or event handler called when the user’s mouse leaves an element. For example, it is called when the user’s mouse leaves a button."
    },
    "on_mouse_move": {
        "description": "Function or event handler called when the user moves the mouse over an element. For example, it’s called when the user moves the mouse over a button."
    },
    "on_mouse_out": {
        "description": "Function or event handler called when the user’s mouse leaves an element. For example, it is called when the user’s mouse leaves a button."
    },
    "on_mouse_over": {
        "description": "Function or event handler called when the user’s mouse enters an element. For example, it is called when the user’s mouse enters a button."
    },
    "on_scroll": {
        "description": "Function or event handler called when the user scrolls the page. For example, it is called when the user scrolls the page down."
    },
    "on_submit": {
        "description": "Function or event handler called when the user submits a form. For example, it is called when the user clicks on a submit button."
    },
    "on_cancel": {
        "description": "Function or event handler called when the user cancels a form. For example, it is called when the user clicks on a cancel button."
    },
    "on_edit": {
        "description": "Function or event handler called when the user edits a form. For example, it is called when the user clicks on a edit button."
    },
    "on_change_start": {
        "description": "Function or event handler called when the user starts selecting a new value(By dragging or clicking)."
    },
    "on_change_end": {
        "description": "Function or event handler called when the user is done selecting a new value(By dragging or clicking)."
    },
    "on_complete": {
        "description": "Called when the user completes a form. For example, it’s called when the user clicks on a complete button."
    },
    "on_error": {
        "description": "The on_error event handler is called when the user encounters an error in a form. For example, it’s called when the user clicks on a error button."
    },
    "on_load": {
        "description": "The on_load event handler is called when the user loads a form. For example, it is called when the user clicks on a load button."
    },
    "on_esc": {
        "description": "The on_esc event handler is called when the user presses the escape key. For example, it is called when the user presses the escape key."
    },
    "on_open": {
        "description": "The on_open event handler is called when the user opens a form. For example, it is called when the user clicks on a open button."
    },
    "on_close": {
        "description": "The on_close event handler is called when the user closes a form. For example, it is called when the user clicks on a close button."
    },
    "on_close_complete": {
        "description": "The on_close_complete event handler is called when the user closes a form. For example, it is called when the user clicks on a close complete button."
    },
    "on_overlay_click": {
        "description": "The on_overlay_click event handler is called when the user clicks on an overlay. For example, it is called when the user clicks on a overlay button."
    },
    "on_key_down": {
        "description": "The on_key_down event handler is called when the user presses a key."
    },
    "on_key_up": {
        "description": "The on_key_up event handler is called when the user releases a key."
    },
    "on_ready": {
        "description": "The on_ready event handler is called when the script is ready to be executed."
    },
    "on_mount": {
        "description": "The on_mount event handler is called when the component is loaded on the page."
    },
    "on_unmount": {
        "description": "The on_unmount event handler is called when the component is removed from the page. This handler is only called during navigation, not when the page is refreshed."
    },
    "on_input": {
        "description": "The on_input event handler is called when the editor receives input from the user. It receives the raw browser event as an argument.",
    },
    "on_resize_editor": {
        "description": "The on_resize_editor event handler is called when the editor is resized. It receives the height and previous height as arguments.",
    },
    "on_copy": {
        "description": "The on_copy event handler is called when the user copies text from the editor. It receives the clipboard data as an argument.",
    },
    "on_cut": {
        "description": "The on_cut event handler is called when the user cuts text from the editor. It receives the clipboard data as an argument.",
    },
    "on_paste": {
        "description": "The on_paste event handler is called when the user pastes text into the editor. It receives the clipboard data and max character count as arguments.",
    },
    "toggle_code_view": {
        "description": "The toggle_code_view event handler is called when the user toggles code view. It receives a boolean whether code view is active.",
    },
    "toggle_full_screen": {
        "description": "The toggle_full_screen event handler is called when the user toggles full screen. It receives a boolean whether full screen is active.",
    },
    "on_cell_activated": {
        "description": "The on_cell_activated event handler is called when the user activate a cell from the data editor. It receive the coordinates of the cell.",
    },
    "on_cell_clicked": {
        "description": "The on_cell_clicked event handler is called when the user click on a cell of the data editor. It receive the coordinates of the cell.",
    },
    "on_cell_context_menu": {
        "description": "The on_cell_context_menu event handler is called when the user right-click on a cell of the data editor. It receives the coordinates of the cell.",
    },
    "on_cell_edited": {
        "description": "The on_cell_edited event handler is called when the user modify the content of a cell. It receives the coordinates of the cell and the modified content.",
    },
    "on_group_header_clicked": {
        "description": "The on_group_header_clicked event handler is called when the user left-click on a group header of the data editor. It receive the index and the data of the group header.",
    },
    "on_group_header_context_menu": {
        "description": "The on_group_header_context_menu event handler is called when the user right-click on a group header of the data editor. It receive the index and the data of the group header.",
    },
    "on_group_header_renamed": {
        "description": "The on_group_header_context_menu event handler is called when the user rename a group header of the data editor. It receive the index and the modified content of the group header.",
    },
    "on_header_clicked": {
        "description": "The on_header_clicked event handler is called when the user left-click a header of the data editor. It receive the index and the content of the header.",
    },
    "on_header_context_menu": {
        "description": "The on_header_context_menu event handler is called when the user right-click a header of the data editor. It receives the index and the content of the header. ",
    },
    "on_header_menu_click": {
        "description": "The on_header_menu_click event handler is called when the user click on the menu button of the header. (menu header not implemented yet)",
    },
    "on_item_hovered": {
        "description": "The on_item_hovered event handler is called when the user hover on an item of the data editor.",
    },
    "on_delete": {
        "description": "The on_delete event handler is called when the user delete a cell of the data editor.",
    },
    "on_finished_editing": {
        "description": "The on_finished_editing event handler is called when the user finish an editing, regardless of if the value changed or not.",
    },
    "on_row_appended": {
        "description": "The on_row_appended event handler is called when the user add a row to the data editor.",
    },
    "on_selection_cleared": {
        "description": "The on_selection_cleared event handler is called when the user unselect a region of the data editor.",
    },
    "on_column_resize": {
        "description": "The on_column_resize event handler is called when the user try to resize a column from the data editor."
    },
    "on_open_change": {
        "description": "The on_open_change event handler is called when the open state of the component changes."
    },
    "on_focus_outside": {
        "description": "The on_focus_outside event handler is called when the user focuses outside the component."
    },
    "on_interact_outside": {
        "description": "The on_interact_outside event handler is called when the user interacts outside the component."
    },
    "on_open_auto_focus": {
        "description": "The on_open_auto_focus event handler is called when the component opens and the focus is returned to the first item."
    },
    "on_change": {
        "description": "The on_change event handler is called when the value or checked state of the component changes."
    },
    "on_value_change": {
        "description": "The on_change event handler is called when the value state of the component changes."
    },
    "on_close_auto_focus": {
        "description": "The on_close_auto_focus event handler is called when focus moves to the trigger after closing. It can be prevented by calling event.preventDefault."
    },
    "on_escape_key_down": {
        "description": "The on_escape_key_down event handler is called when the escape key is down. It can be prevented by calling event.preventDefault."
    },
    "on_pointer_down_outside": {
        "description": "The on_pointer_down_outside event handler is called when a pointer event occurs outside the bounds of the component. It can be prevented by calling event.preventDefault."
    },
    "on_value_commit": {
        "description": "The on_value_commit event handler is called when the value changes at the end of an interaction. Useful when you only need to capture a final value e.g. to update a backend service."
    },
    "on_clear_server_errors": {
        "description": "The on_clear_server_errors event handler is called when the form is submitted or reset and the server errors need to be cleared."
    },
    "on_select": {
        "description": "The on_select event handler is called when the user selects an item."
    },
    "on_drop": {
        "description": "The on_drop event handler is called when the user drops an item."
    },
}


def get_prev_next(url):
    """Get the previous and next links in the sidebar."""
    url = url.strip("/")
    for i, item in enumerate(flat_items):
        if item.link.strip("/") == url:
            if i == 0:
                return None, flat_items[i + 1]
            elif i == len(flat_items) - 1:
                return flat_items[i - 1], None
            else:
                return flat_items[i - 1], flat_items[i + 1]
    return None, None


def get_default_value(lines: list[str], start_index: int) -> str:
    """Process lines of code to get the value of a prop, handling multi-line values.

    Args:
        lines: The lines of code to process.
        start_index: The index of the line where the prop is defined.

    Returns:
        The default value of the prop.
    """
    # Check for the default value in the prop comment (Default: )
    # Need to update the components comments in order to get the default value
    if start_index > 0:
        comment_line = lines[start_index - 1].strip()
        if comment_line.startswith("#"):
            default_match = re.search(r'Default:\s*(["\']?\w+["\']?|\w+)', comment_line)
            if default_match:
                default_value = default_match.group(1)
                return default_value


class Prop(rx.Base):
    """Hold information about a prop."""

    # The name of the prop.
    name: str

    # The type of the prop.
    type_: Any

    # The description of the prop.
    description: str

    # The default value of the prop.
    default_value: str


class Route(rx.Base):
    """A page route."""

    # The path of the route.
    path: str

    # The page title.
    title: str | None = None

    # Background color for the page.
    background_color: str | None = None

    # The component to render for the route.
    component: Callable[[], rx.Component]

    # whether to add the route to the app's pages. This is typically used
    # to delay adding the 404 page(which is explicitly added in pcweb.py).
    # https://github.com/reflex-dev/reflex-web/pull/659#pullrequestreview-2021171902
    add_as_page: bool = True


def get_path(component_fn: Callable):
    """Get the path for a page based on the file location.

    Args:
        component_fn: The component function for the page.
    """
    module = inspect.getmodule(component_fn)

    # Create a path based on the module name.
    return (
        module.__name__.replace(".", "/").replace("_", "-").split("pcweb/pages")[1]
        + "/"
    )


def docpage(
    set_path: str | None = None,
    t: str | None = None,
    right_sidebar: bool = True,
    chakra_components={},
) -> rx.Component:
    """A template that most pages on the reflex.dev site should use.

    This template wraps the webpage with the navbar and footer.

    Args:
        set_path: The path to set for the sidebar.
        prop: Props to apply to the template.

    Returns:
        A wrapper function that returns the full webpage.
    """

    def docpage(contents: Callable[[], Route]) -> Route:
        """Wrap a component in a docpage template.

        Args:
            contents: A function that returns a page route.

        Returns:
            The final route with the template applied.
        """
        # Get the path to set for the sidebar.
        path = get_path(contents) if set_path is None else set_path
        # Set the page title.
        title = contents.__name__.replace("_", " ").title() if t is None else t

        def wrapper(*args, **kwargs) -> rx.Component:
            """The actual function wrapper.

            Args:
                *args: Args to pass to the contents function.
                **kwargs: Kwargs to pass to the contents function.

            Returns:
                The page with the template applied.
            """
            # Create the docpage sidebar.
            sidebar = sb(url=path, width="280px", chakra_components=chakra_components)
            # # Get the previous and next sidebar links.
            prev, next = get_prev_next(path)
            links = []

            # Create the previous component link.
            if prev:
                next_prev_name = (
                    prev.alt_name_for_next_prev
                    if prev.alt_name_for_next_prev
                    else prev.names
                )
                links.append(
                    rx.link(
                        rx.hstack(
                            # get_icon(icon="arrow_right", transform="rotate(180deg)"),
                            rx.icon("arrow_right"),
                            next_prev_name,
                            align_items="center",
                            gap="8px",
                            width="100%",
                            justify_content=[
                                "center",
                                "center",
                                "flex-start",
                                "flex-start",
                                "flex-start",
                            ],
                            border_radius="8px",
                        ),
                        underline="none",
                        href=prev.link,
                        _hover={"color": rx.color("slate", 11)},
                        transition="color 0.035s ease-out",
                        background_color=[
                            rx.color("slate", 3),
                            rx.color("slate", 3),
                            "transparent",
                            "transparent",
                            "transparent",
                        ],
                        border_radius="8px",
                        padding=["2px 6px", "2px 6px", "0px", "0px", "0px"],
                        style={
                            "color": rx.color("slate", 9),
                            **fonts.small,
                            ":hover": {"color": rx.color("slate", 11)},
                        },
                        width=["100%", "100%", "auto", "auto", "auto"],
                    )
                )
            else:
                links.append(rx.box())
            # links.append(rx.box())
            # Create the next component link.
            if next:
                next_prev_name = (
                    next.alt_name_for_next_prev
                    if next.alt_name_for_next_prev
                    else next.names
                )
                links.append(
                    rx.link(
                        rx.hstack(
                            next_prev_name,
                            # get_icon(icon="arrow_right"),
                            rx.icon("arrow_right"),
                            align_items="center",
                            gap="8px",
                            width="100%",
                            justify_content=[
                                "center",
                                "center",
                                "flex-end",
                                "flex-end",
                                "flex-end",
                            ],
                            background_color=[
                                rx.color("slate", 3),
                                rx.color("slate", 3),
                                "transparent",
                                "transparent",
                                "transparent",
                            ],
                            padding=["2px 6px", "2px 6px", "0px", "0px", "0px"],
                            border_radius="8px",
                        ),
                        underline="none",
                        href=next.link,
                        _hover={"color": rx.color("slate", 11)},
                        transition="color 0.035s ease-out",
                        style={
                            "color": rx.color("slate", 9),
                            **fonts.small,
                            ":hover": {"color": rx.color("slate", 11)},
                        },
                        width=["100%", "100%", "auto", "auto", "auto"],
                    ),
                )
            else:
                links.append(rx.box())
            # links.append(rx.box())
            toc = []
            if not isinstance(contents, rx.Component):
                comp = contents(*args, **kwargs)
            else:
                comp = contents

            if isinstance(comp, tuple):
                toc, comp = comp

            # Return the templated page.
            return rx.flex(
                # navbar(),
                rx.el.main(
                    rx.box(
                        sidebar,
                        margin_top="105px",
                        height="100%",
                        width="24%",
                        display=["none", "none", "none", "none", "flex", "flex"],
                        flex_shrink=0,
                    ),
                    rx.box(
                        rx.box(
                            # breadcrumb(path, nav_sidebar),
                            padding_x=[
                                "0px",
                                "0px",
                                "0px",
                                "48px",
                                "96px",
                            ],
                        ),
                        rx.box(
                            rx.el.article(comp),
                            rx.el.nav(
                                *links,
                                justify="between",
                                margin_top=["32px", "32px", "40px", "40px", "40px"],
                                margin_bottom=[
                                    "24px",
                                    "24px",
                                    "24pxpx",
                                    "48px",
                                    "48px",
                                ],
                                gap="8px",
                                display="flex",
                                flex_direction="row",
                                justify_content="space-between",
                            ),
                            # docpage_footer(path=path),
                            padding_x=["16px", "24px", "24px", "48px", "96px"],
                            margin_top=["105px", "145px", "0px", "0px", "0px"],
                            padding_top="5em",
                        ),
                        width=(
                            ["100%", "100%", "100%", "90%", "70%", "60%"]
                            if right_sidebar
                            else "100%"
                        ),
                        height="100%",
                    ),
                    rx.el.nav(
                        rx.flex(
                            rx.heading(
                                "On this page",
                                as_="h5",
                                style={
                                    "color": rx.color("slate", 12),
                                    "font-family": "Instrument Sans",
                                    "font-size": "14px",
                                    "font-style": "normal",
                                    "font-weight": "600",
                                    "line-height": "20px",
                                    "letter-spacing": "-0.21px",
                                },
                            ),
                            rx.unordered_list(
                                *[
                                    (
                                        rx.list_item(
                                            rx.link(
                                                text,
                                                style={
                                                    "transition": "color 0.035s ease-out",
                                                    "color": rx.color("slate", 9),
                                                    "overflow": "hidden",
                                                    "text-overflow": "ellipsis",
                                                    "white-space": "nowrap",
                                                    **fonts.small,
                                                    ":hover": {
                                                        "color": rx.color("slate", 11),
                                                    },
                                                },
                                                _hover={
                                                    "color": rx.color("slate", 11),
                                                },
                                                underline="none",
                                                href=path
                                                + "#"
                                                + text.lower().replace(" ", "-"),
                                            )
                                        )
                                        if level == 1
                                        else (
                                            rx.list_item(
                                                rx.link(
                                                    text,
                                                    style={
                                                        "transition": "color 0.035s ease-out",
                                                        "overflow": "hidden",
                                                        "text-overflow": "ellipsis",
                                                        "white-space": "nowrap",
                                                        "color": rx.color("slate", 9),
                                                        **fonts.small,
                                                        ":hover": {
                                                            "color": rx.color(
                                                                "slate", 11
                                                            ),
                                                        },
                                                    },
                                                    _hover={
                                                        "color": rx.color("slate", 11),
                                                    },
                                                    underline="none",
                                                    href=path
                                                    + "#"
                                                    + text.lower().replace(" ", "-"),
                                                )
                                            )
                                            if level == 2
                                            else rx.list_item(
                                                rx.link(
                                                    text,
                                                    style={
                                                        "transition": "color 0.035s ease-out",
                                                        "overflow": "hidden",
                                                        "text-overflow": "ellipsis",
                                                        "white-space": "nowrap",
                                                        "color": rx.color("slate", 9),
                                                        **fonts.small,
                                                        ":hover": {
                                                            "color": rx.color(
                                                                "slate", 11
                                                            ),
                                                        },
                                                    },
                                                    _hover={
                                                        "color": rx.color("slate", 11),
                                                    },
                                                    underline="none",
                                                    padding_left="24px",
                                                    href=path
                                                    + "#"
                                                    + text.lower().replace(" ", "-"),
                                                )
                                            )
                                        )
                                    )
                                    for level, text in toc
                                ],
                                list_style_type="none",
                                display="flex",
                                gap="16px",
                                flex_direction="column",
                                margin_left="0px !important",
                            ),
                            direction="column",
                            width="100%",
                            position="fixed",
                            gap="16px",
                            padding="14px 8px 0px 8px",
                            max_width="280px",
                            justify="start",
                            overflow="hidden",
                            max_height="80vh",
                            overflow_y="scroll",
                        ),
                        margin_top="105px",
                        width="18%",
                        height="100%",
                        display=(
                            ["none", "none", "none", "none", "none", "flex"]
                            if right_sidebar
                            else "none"
                        ),
                        flex_shrink=0,
                    ),
                    max_width="110em",
                    margin_left="auto",
                    margin_right="auto",
                    margin_top="0px",
                    height="100%",
                    min_height="100vh",
                    width="100%",
                    display="flex",
                    flex_direction="row",
                ),
                background=rx.color("slate", 1),
                width="100%",
                justify="center",
                flex_direction="column",
            )

        # Return the route.
        components = path.split("/")
        category = (
            " ".join(
                word.capitalize() for word in components[2].replace("-", " ").split()
            )
            if len(components) > 2
            else None
        )
        return Route(
            path=path,
            title=f"{title} · Reflex Docs" if category is None else title,
            component=wrapper,
        )

    return docpage


import re


class Source(rx.Base):
    """Parse the source code of a component."""

    # The component to parse.
    component: Type[rx.Component]

    # The source code.
    code: list[str] = []

    def __init__(self, *args, **kwargs):
        """Initialize the source code parser."""
        super().__init__(*args, **kwargs)

        # Get the source code.
        self.code = [
            line
            for line in inspect.getsource(self.component).splitlines()
            if len(line) > 0
        ]

    def get_docs(self) -> str:
        """Get the docstring of the component.

        Returns:
            The docstring of the component.
        """
        return self.component.__doc__

    def get_props(self):
        """Get a dictionary of the props and their descriptions.

        Returns:
            A dictionary of the props and their descriptions.
        """
        props = self._get_props()

        parent_cls = self.component.__bases__[0]
        if parent_cls != rx.Component and parent_cls != BaseHTML:
            props += Source(component=parent_cls).get_props()

        return props

    def _get_props(self):
        """Get a dictionary of the props and their descriptions.

        Returns:
            A dictionary of the props and their descriptions.
        """
        out = []
        props = self.component.get_props()
        comments = []

        for i, line in enumerate(self.code):
            line = self.code[i]

            if re.search("def ", line):
                break

            if line.strip().startswith("#"):
                comments.append(line)
                continue

            match = re.search(r"\w+:", line)
            if match is None:
                continue

            prop = match.group(0).strip(":")
            if prop not in props:
                continue

            default_value = get_default_value(self.code, i)

            if i > 0:
                comment_above = self.code[i - 1].strip()
                assert comment_above.startswith(
                    "#"
                ), f"Expected comment, got {comment_above}"

            comment = Source.get_comment(comments)
            comments.clear()

            type_ = self.component.get_fields()[prop].outer_type_
            out.append(
                Prop(
                    name=prop,
                    type_=type_,
                    default_value=default_value if default_value else "",
                    description=comment,
                )
            )

        return out

    @staticmethod
    def get_comment(comments: list[str]):
        return "".join([comment.strip().strip("#") for comment in comments])


def get_code_style(color: str):
    return {
        "color": rx.color(color, 11),
        "border_radius": "4px",
        "border": f"1px solid {rx.color(color, 5)}",
        "background": rx.color(color, 3),
    }


def hovercard(trigger: rx.Component, content: rx.Component) -> rx.Component:
    return rx.hover_card.root(
        rx.hover_card.trigger(
            trigger,
        ),
        rx.hover_card.content(
            content,
            side="top",
            align="center",
            color=rx.color("slate", 9),
            style=fonts.small,
        ),
    )


def color_scheme_hovercard(literal_values: list[str]) -> rx.Component:
    return hovercard(
        rx.icon(tag="palette", size=15, color=rx.color("slate", 9), flex_shrink=0),
        rx.grid(
            *[
                rx.tooltip(
                    rx.box(
                        width="30px",
                        height="30px",
                        border_radius="max(var(--radius-2), var(--radius-full))",
                        flex_shrink=0,
                        bg=f"var(--{color}-9)",
                    ),
                    content=color,
                    delay_duration=0,
                )
                for color in literal_values
            ],
            columns="6",
            spacing="3",
        ),
    )


def prop_docs(
    prop: Prop, prop_dict, component, is_interactive: bool
) -> list[rx.Component]:
    """Generate the docs for a prop."""
    # Get the type of the prop.
    type_ = prop.type_
    if rx.utils.types._issubclass(prop.type_, rx.Var):
        # For vars, get the type of the var.
        type_ = rx.utils.types.get_args(type_)[0]

    origin = get_origin(type_)
    args = get_args(type_)

    literal_values = []  # Literal values of the prop
    all_types = []  # List for all the prop types
    MAX_PROP_VALUES = 3

    COMMON_TYPES = {}  # Used to exclude common types from the MAX_PROP_VALUES
    if origin is Union:
        non_literal_types = []  # List for all the non-literal types

        for arg in args:
            all_types.append(arg.__name__)
            if get_origin(arg) is Literal:
                literal_values.extend(str(lit_arg) for lit_arg in arg.__args__)
            elif arg.__name__ != "Breakpoints":  # Don't include Breakpoints
                non_literal_types.append(arg.__name__)

        if len(literal_values) < 10:
            literal_str = " | ".join(f'"{value}"' for value in literal_values)
            type_components = ([literal_str] if literal_str else []) + non_literal_types
            type_name = (
                " | ".join(type_components)
                if len(type_components) == 1
                else f"Union[{', '.join(type_components)}]"
            )
        else:
            type_name = (
                "Literal"
                if not non_literal_types
                else f"Union[Literal, {', '.join(non_literal_types)}]"
            )

    elif origin is dict:
        key_type = args[0].__name__ if args else "Any"
        value_type = args[1].__name__ if len(args) > 1 else "Any"
        type_name = f"Dict[{key_type}, {value_type}]"

    elif origin is Literal:
        literal_values = list(map(str, args))
        if len(literal_values) > MAX_PROP_VALUES and prop.name not in COMMON_TYPES:
            type_name = "Literal"
        else:
            type_name = " | ".join([f'"{value}"' for value in literal_values])

    else:
        type_name = type_.__name__

    # Get the default value.
    default_value = prop.default_value if prop.default_value is not None else "-"
    # Get the color of the prop.
    color = TYPE_COLORS.get(type_.__name__, "gray")
    # Return the docs for the prop.
    return [
        rx.table.cell(
            rx.hstack(
                rx.code(prop.name, text_wrap="nowrap", style=get_code_style("violet")),
                hovercard(
                    rx.icon(
                        tag="info", size=15, color=rx.color("slate", 9), flex_shrink=0
                    ),
                    rx.text(prop.description, size="2"),
                ),
                spacing="2",
                align="center",
            ),
            padding_left="1em",
            justify="start",
        ),
        rx.table.cell(
            rx.hstack(
                rx.cond(
                    (len(literal_values) > 0) & (prop.name not in COMMON_TYPES),
                    rx.code(
                        (
                            " | ".join(
                                [f'"{v}"' for v in literal_values[:MAX_PROP_VALUES]]
                                + ["..."]
                            )
                            if len(literal_values) > MAX_PROP_VALUES
                            else type_name
                        ),
                        # color_scheme=color,
                        style=get_code_style(color),
                        text_wrap="nowrap",
                    ),
                    rx.code(
                        type_name,
                        # color_scheme=color,
                        style=get_code_style(color),
                        text_wrap="nowrap",
                    ),
                ),
                rx.cond(
                    len(literal_values) > MAX_PROP_VALUES
                    and prop.name not in COMMON_TYPES,
                    hovercard(
                        rx.icon(
                            tag="circle-ellipsis",
                            size=15,
                            color=rx.color("slate", 9),
                            flex_shrink=0,
                        ),
                        rx.text(
                            " | ".join([f'"{v}"' for v in literal_values]), size="2"
                        ),
                    ),
                ),
                rx.cond(
                    (origin == Union)
                    & (
                        "Breakpoints" in all_types
                    ),  # Display that the type is Union with Breakpoints
                    hovercard(
                        rx.icon(
                            tag="info",
                            size=15,
                            color=rx.color("slate", 9),
                            flex_shrink=0,
                        ),
                        rx.text(f"Union[{', '.join(all_types)}]", size="2"),
                    ),
                ),
                rx.cond(
                    (prop.name == "color_scheme") | (prop.name == "accent_color"),
                    color_scheme_hovercard(literal_values),
                ),
                spacing="2",
                align="center",
            ),
            padding_left="1em",
            justify="start",
        ),
        rx.table.cell(
            rx.flex(
                rx.code(
                    default_value,
                    style=get_code_style(
                        "red"
                        if default_value == "False"
                        else "green"
                        if default_value == "True"
                        else "gray"
                    ),
                    text_wrap="nowrap",
                )
            ),
            padding_left="1em",
            justify="start",
        ),
    ]


def generate_props(src: Source, component, comp):
    if len(src.get_props()) == 0:
        return rx.vstack(
            rx.heading("Props", as_="h3"),
            rx.text("No component specific props"),
            width="100%",
            overflow_x="auto",
            align_items="start",
            padding_y=".5em",
        )

    padding_left = "1em"

    prop_dict = {}

    is_interactive = False

    body = rx.table.body(
        *[
            rx.table.row(
                *prop_docs(prop, prop_dict, component, is_interactive), align="center"
            )
            for prop in src.get_props()
            if not prop.name.startswith("on_")  # ignore event trigger props
        ],
        background=rx.color("slate", 2),
    )

    try:
        if f"{component.__name__}" in comp.metadata:
            comp = eval(comp.metadata[component.__name__])(**prop_dict)

        elif not is_interactive:
            comp = rx.fragment()

        else:
            try:
                comp = rx.vstack(component.create("Test", **prop_dict))
            except:
                comp = rx.fragment()
            if "data" in component.__name__.lower():
                raise Exception("Data components cannot be created")
    except Exception as e:
        print(f"Failed to create component {component.__name__}, error: {e}")
        comp = rx.fragment()

    return rx.vstack(
        docdemobox(comp) if not isinstance(comp, rx.Fragment) else "",
        rx.scroll_area(
            rx.table.root(
                rx.el.style(
                    """
                    .rt-TableRoot:where(.rt-variant-surface) :where(.rt-TableRootTable) :where(.rt-TableHeader) {
                    --table-row-background-color: "transparent"
                    }
                    """
                ),
                rx.table.header(
                    rx.table.row(
                        rx.table.column_header_cell(
                            "Prop",
                            padding_left=padding_left,
                            justify="start",
                            text_wrap="nowrap",
                            width="auto",
                        ),
                        rx.table.column_header_cell(
                            "Type | Values",
                            padding_left=padding_left,
                            justify="start",
                            text_wrap="nowrap",
                            width="auto",
                        ),
                        rx.table.column_header_cell(
                            "Default",
                            padding_left=padding_left,
                            justify="start",
                            text_wrap="nowrap",
                            width="auto",
                        ),
                        rx.cond(
                            is_interactive,
                            rx.table.column_header_cell(
                                "Interactive",
                                padding_left=padding_left,
                                justify="start",
                                text_wrap="nowrap",
                                width="auto",
                            ),
                            rx.fragment(),
                        ),
                    ),
                    background=rx.color("slate", 3),
                ),
                body,
                width="100%",
                padding_x="0",
                variant="surface",
                size="1",
                border=f"1px solid {rx.color('slate', 4)}",
            ),
            max_height="25em",
            margin_bottom="16px",
        ),
    )


def generate_valid_children(comp):
    if not comp._valid_children:
        return rx.text("")

    valid_children = [
        rc.wrap_item(rx.code(child, style=get_code_style("violet")))
        for child in comp._valid_children
    ]
    return rx.vstack(
        rx.heading("Valid Children", as_="h3", style=fonts.large),
        rc.wrap(*valid_children),
        width="100%",
        align_items="start",
        padding_bottom="24px",
    )


default_triggers = rx.Component.create().get_event_triggers()


def same_trigger(t1, t2):
    if t1 is None or t2 is None:
        return False
    args1 = inspect.getfullargspec(t1).args
    args2 = inspect.getfullargspec(t2).args
    return args1 == args2


def generate_event_triggers(comp, src):
    prop_name_to_description = {
        prop.name: prop.description
        for prop in src.get_props()
        if prop.name.startswith("on_")
    }
    triggers = comp().get_event_triggers()
    custom_events = [
        event
        for event in triggers
        if not same_trigger(triggers.get(event), default_triggers.get(event))
    ]

    if not custom_events:
        return rx.vstack(
            rx.heading("Event Triggers", as_="h3", style=fonts.large),
            rx.link(
                "See the full list of default event triggers",
                href="https://reflex.dev/docs/api-reference/event-triggers/",
                color=rx.color("violet", 11),
                style=fonts.base,
                is_external=True,
            ),
            width="100%",
            overflow_x="auto",
            align_items="start",
            padding_y=".5em",
        )
    padding_left = "1em"

    return rx.vstack(
        rx.heading("Event Triggers", as_="h3", style=fonts.large),
        rx.link(
            "See the full list of default event triggers",
            href="https://reflex.dev/docs/api-reference/event-triggers/",
            color=rx.color("violet", 11),
            style=fonts.base,
            is_external=True,
        ),
        rx.scroll_area(
            rx.table.root(
                rx.el.style(
                    """
                    .rt-TableRoot:where(.rt-variant-surface) :where(.rt-TableRootTable) :where(.rt-TableHeader) {
                        --table-row-background-color: "transparent"
                    }
                """
                ),
                rx.table.header(
                    rx.table.row(
                        rx.table.column_header_cell(
                            "Trigger", padding_left=padding_left, justify="start"
                        ),
                        rx.table.column_header_cell(
                            "Description", padding_left=padding_left, justify="start"
                        ),
                    ),
                    background_color=rx.color("slate", 3),
                ),
                rx.table.body(
                    *[
                        rx.table.row(
                            rx.table.cell(
                                rx.code(event, style=get_code_style("violet")),
                                padding_left=padding_left,
                                justify="start",
                            ),
                            rx.table.cell(
                                prop_name_to_description.get(event)
                                or EVENTS[event]["description"],
                                color=rx.color("slate", 11),
                                style=fonts.small,
                                padding_left=padding_left,
                                justify="start",
                            ),
                        )
                        for event in custom_events
                    ],
                    background_color=rx.color("slate", 2),
                ),
                width="100%",
                variant="surface",
                size="1",
                border=f"1px solid {rx.color('slate', 4)}",
            ),
            width="100%",
            overflow="hidden",
            align_items="start",
        ),
        gap="24px",
        max_height="40em",
        align_items="start",
    )


def component_docs(component_tuple, comp):
    """Generates documentation for a given component."""

    component = component_tuple[0]

    src = Source(component=component)
    props = generate_props(src, component, comp)
    triggers = generate_event_triggers(component, src)
    children = generate_valid_children(component)

    return rx.box(
        rx.heading(component_tuple[1]),
        rx.box(markdown(textwrap.dedent(src.get_docs())), padding_bottom=".5em"),
        props,
        children,
        triggers,
        text_align="left",
        width="100%",
        padding_bottom="2em",
    )


def get_headings(comp):
    """Get the strings from markdown component."""
    if isinstance(comp, mistletoe.block_token.Heading):
        heading_text = "".join(
            token.content for token in comp.children if hasattr(token, "content")
        )
        return [(comp.level, heading_text)]

    # Recursively get the strings from the children.
    if not hasattr(comp, "children") or comp.children is None:
        return []

    headings = []
    for child in comp.children:
        headings.extend(get_headings(child))
    return headings


def get_toc(source, href, component_list=None):
    component_list = component_list or []
    component_list = component_list[1:]

    # Generate the TOC
    # The environment used for execing and evaling code.
    env = source.metadata
    env["__xd"] = xd

    # Get the content of the document.
    source = source.content

    # Get the blocks in the source code.
    # Note: we must use reflex-web's special flexdown instance xd here - it knows about all custom block types (like DemoBlock)
    blocks = xd.get_blocks(source, href)

    content_pieces = []
    for block in blocks:
        if (
            not isinstance(block, flexdown.blocks.MarkdownBlock)
            or len(block.lines) == 0
            or not block.lines[0].startswith("#")
        ):
            continue
        # Now we should have all the env entries we need
        content = block.get_content(env)
        content_pieces.append(content)

    content = "\n".join(content_pieces)
    doc = mistletoe.Document(content)

    # Parse the markdown headers.
    headings = get_headings(doc)

    if len(component_list):
        headings.append((1, "API Reference"))
    for component_tuple in component_list:
        headings.append((2, component_tuple[1]))
    return headings


def multi_docs(path, comp, component_list, title, chakra_components):
    components = [
        component_docs(component_tuple, comp) for component_tuple in component_list[1:]
    ]
    fname = path.strip("/") + ".md"
    ll_doc_exists = os.path.exists(fname.replace(".md", "-ll.md"))

    non_active_style = {
        "padding": "8px",
        "color": rx.color("slate", 9),
        "width": "7em",
        "transition": "color 0.035s ease-out",
        "_hover": {
            "color": rx.color("slate", 11),
        },
        **fonts.small,
    }

    active_style = {
        "padding": "8px",
        "background": rx.color("slate", 2),
        "color": rx.color("slate", 11),
        "box_shadow": css.shadows["large"],
        "border_radius": "8px",
        "width": "7em",
        "cursor": "default",
        "border": f"1px solid {rx.color('slate', 4)}",
        **fonts.small,
    }

    def links(current_page, ll_doc_exists, path):
        if ll_doc_exists:
            if current_page == "hl":
                return rx.flex(
                    rx.box(flex_grow="1"),
                    rx.flex(
                        rx.link(
                            rx.center(rx.text("High Level"), style=active_style),
                            underline="none",
                        ),
                        rx.link(
                            rx.center(rx.text("Low Level"), style=non_active_style),
                            href=path + "/low",
                            underline="none",
                        ),
                        spacing="2",
                        padding="8px",
                        background=rx.color("slate", 3),
                        border_radius="16px",
                        align_items="center",
                        justify_items="center",
                    ),
                    margin_bottom=".5em",
                )
            else:
                return rx.flex(
                    rx.box(flex_grow="1"),
                    rx.flex(
                        rx.link(
                            rx.center(rx.text("High Level"), style=non_active_style),
                            href=path,
                            underline="none",
                        ),
                        rx.link(
                            rx.center(rx.text("Low Level"), style=active_style),
                            href=path + "/low",
                            underline="none",
                        ),
                        spacing="2",
                        padding="8px",
                        background=rx.color("slate", 3),
                        border_radius="16px",
                        align_items="center",
                        justify_items="center",
                    ),
                    margin_bottom=".5em",
                )
        return rx.fragment()

    @docpage(set_path=path, t=title, chakra_components=chakra_components)
    def out():
        toc = get_toc(comp, fname, component_list)
        return toc, rx.flex(
            links("hl", ll_doc_exists, path),
            xd.render(comp, filename=fname),
            rx.heading(text="API Reference"),
            rx.vstack(*components),
            direction="column",
            width="100%",
        )

    return out
