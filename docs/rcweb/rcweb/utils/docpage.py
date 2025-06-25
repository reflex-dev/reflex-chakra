"""Utility functions for the component docs page."""

import dataclasses
import functools
import hashlib
import inspect
import re
import textwrap
from collections.abc import Callable, Sequence
from types import UnionType
from typing import (
    Any,
    Literal,
    Union,
    get_args,
    get_origin,
)

import flexdown
import flexdown.blocks
import mistletoe
import mistletoe.block_token
import mistletoe.token
import reflex as rx
from reflex.components.base.fragment import Fragment
from reflex.components.component import Component
from reflex.components.el.elements.base import BaseHTML
from reflex.constants.colors import ColorType

import reflex_chakra as rc
from rcweb.utils.blocks.headings import h1_comp, h2_comp
from rcweb.utils.flexdown import docdemobox, markdown, xd
from rcweb.utils.sidebar import MobileAndTabletSidebarState
from rcweb.utils.sidebar import sidebar as sb

flat_items = []

# Mapping from types to colors.
TYPE_COLORS: dict[str, ColorType] = {
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
        "description": "Function or event handler called when the value of an element has changed. For example, it is called when the user types into a text input each keystroke triggers the on change."
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
    "on_animation_start": {
        "description": "The on_animation_start event handler is called when the animation starts. It receives the animation name as an argument.",
    },
    "on_animation_end": {
        "description": "The on_animation_end event handler is called when the animation ends. It receives the animation name as an argument.",
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
    "get_server_side_group_key": {"description": "Get the server side group key."},
    "is_server_side_group_open_by_default": {
        "description": "Event handler to check if the server-side group is open by default."
    },
    "get_child_count": {"description": "Event handler to get the child count."},
    "on_selection_changed": {
        "description": "The on_selection_changed event handler is called when the selection changes."
    },
    "on_first_data_rendered": {
        "description": "The on_first_data_rendered event handler is called when the first data is rendered."
    },
    "get_row_id": {
        "description": "The get_row_id event handler is called to get the row id."
    },
    "get_data_path": {
        "description": "The get_data_path event handler is called to get the data path."
    },
    "is_server_side_group": {
        "description": "The is_server_side_group event handler is called to check if the group is server-side."
    },
}


def get_prev_next(url):
    """Get the previous and next links in the sidebar."""
    url = url.strip("/")
    for i, item in enumerate(flat_items):
        if item.link.strip("/") == url:
            prev_link = flat_items[i - 1] if i > 0 else None
            next_link = flat_items[i + 1] if i < len(flat_items) - 1 else None
            return prev_link, next_link
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
            default_match = re.search(r"Default:\s*(.+)$", comment_line)
            if default_match:
                return default_match.group(1).strip()

    # Get the initial line
    line = lines[start_index]
    parts = line.split("=", 1)
    if len(parts) != 2:
        return ""
    value = parts[1].strip()

    # Check if the value is complete
    open_brackets = value.count("{") - value.count("}")
    open_parentheses = value.count("(") - value.count(")")

    # If brackets or parentheses are not balanced, collect more lines
    current_index = start_index + 1
    while (open_brackets > 0 or open_parentheses > 0) and current_index < len(lines):
        next_line = lines[current_index].strip()
        value += " " + next_line
        open_brackets += next_line.count("{") - next_line.count("}")
        open_parentheses += next_line.count("(") - next_line.count(")")
        current_index += 1

    # Remove any trailing comments
    value = re.split(r"\s+#", value)[0].strip()

    # Process Var.create_safe within dictionary
    def process_var_create_safe(match):
        content = match.group(1)
        # Extract only the first argument
        return re.split(r",", content)[0].strip()

    value = re.sub(r"Var\.create_safe\((.*?)\)", process_var_create_safe, value)
    value = re.sub(r"\bColor\s*\(", "rx.color(", value)

    return value.strip()


@dataclasses.dataclass
class Prop:
    """Hold information about a prop."""

    # The name of the prop.
    name: str

    # The type of the prop.
    type_: Any

    # The description of the prop.
    description: str

    # The default value of the prop.
    default_value: str


@dataclasses.dataclass(kw_only=True)
class Route:
    """A page route."""

    # The path of the route.
    path: str

    # The page title.
    title: str | None = None

    # The page description.
    description: str | None = None

    # The page image.
    image: str | None = None

    # The page extra meta data.
    meta: list[dict[str, str]] | None = None

    # Background color for the page.
    background_color: str | None = None

    # The component to render for the route.
    component: Callable[[], rx.Component]

    # whether to add the route to the app's pages. This is typically used
    # to delay adding the 404 page(which is explicitly added in pcweb.py).
    # https://github.com/reflex-dev/reflex-web/pull/659#pullrequestreview-2021171902
    add_as_page: bool = True

    def __hash__(self):
        return hash(f"{self.path}-{self.title}")


def get_path(component_fn: Callable):
    """Get the path for a page based on the file location.

    Args:
        component_fn: The component function for the page.
    """
    module = inspect.getmodule(component_fn)

    if module is None:
        msg = f"Could not find module for {component_fn}"
        raise ValueError(msg)

    # Create a path based on the module name.
    return (
        module.__name__.replace(".", "/").replace("_", "-").split("pcweb/pages")[1]
        + "/"
    )


def docpage(
    chakra_components: dict[str, list[tuple[str, list[tuple[type, str]]]]],
    set_path: str | None = None,
    t: str | None = None,
    right_sidebar: bool = True,
    page_title: str | None = None,
    pseudo_right_bar: bool = False,
):
    """A template that most pages on the reflex.dev site should use.

    This template wraps the webpage with the navbar and footer.

    Args:
        set_path: The path to set for the sidebar.
        prop: Props to apply to the template.

    Returns:
        A wrapper function that returns the full webpage.
    """

    def docpage(
        contents: Callable[[], Component]
        | Callable[[], tuple[list[tuple[int, str]], Component]],
    ) -> Route:
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

        @functools.wraps(contents)
        def wrapper(*args, **kwargs) -> rx.Component:
            """The actual function wrapper.

            Args:
                *args: Args to pass to the contents function.
                **kwargs: Kwargs to pass to the contents function.

            Returns:
                The page with the template applied.
            """
            # Create the docpage sidebar.
            sidebar = sb(url=path, width="300px", chakra_components=chakra_components)
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
                    rx.box(
                        rx.link(
                            rx.box(
                                "Back",
                                class_name="flex flex-row justify-center lg:justify-start items-center gap-2 rounded-lg w-full",
                            ),
                            underline="none",
                            href=prev.link,
                            class_name="py-0.5 lg:py-0 rounded-lg lg:w-auto font-small text-slate-9 hover:!text-slate-11 transition-color",
                        ),
                        rx.text(next_prev_name, class_name="font-smbold text-slate-12"),
                        class_name="flex flex-col justify-start gap-1",
                    )
                )
            else:
                links.append(rx.fragment())
            links.append(rx.spacer())

            if next:
                next_prev_name = (
                    next.alt_name_for_next_prev
                    if next.alt_name_for_next_prev
                    else next.names
                )
                links.append(
                    rx.box(
                        rx.link(
                            rx.box(
                                "Next",
                                class_name="flex flex-row lg:justify-start items-center gap-2 rounded-lg w-full self-end",
                            ),
                            underline="none",
                            href=next.link,
                            class_name="py-0.5 lg:py-0 rounded-lg lg:w-auto font-small text-slate-9 hover:!text-slate-11 transition-color",
                        ),
                        rx.text(next_prev_name, class_name="font-smbold text-slate-12"),
                        class_name="flex flex-col justify-start gap-1 items-end",
                    )
                )
            else:
                links.append(rx.fragment())

            table_of_contents = []
            if not isinstance(contents, rx.Component):
                comp = contents(*args, **kwargs)
            else:
                comp = contents

            if isinstance(comp, tuple):
                table_of_contents, comp = comp

            show_right_sidebar = right_sidebar and len(table_of_contents) >= 2

            main_content_width = " lg:w-[60%]" if show_right_sidebar else " lg:w-full"

            return rx.box(
                # navbar
                rc.flex(
                    rc.box(
                        rx.box(
                            rx.el.button(
                                rx.color_mode.icon(
                                    light_component=rx.icon(
                                        "sun", size=16, class_name="!text-slate-9"
                                    ),
                                    dark_component=rx.icon(
                                        "moon", size=16, class_name="!text-slate-9"
                                    ),
                                ),
                                on_click=rx.toggle_color_mode,
                                class_name="flex flex-row justify-center items-center px-3 py-0.5 w-full h-[47px]",
                            ),
                            float="right",
                        ),
                        rx.mobile_and_tablet(
                            rc.icon_button(
                                rx.icon("menu"),
                                on_click=MobileAndTabletSidebarState.toggle_drawer,
                                float="right",
                            ),
                        ),
                        justify="space-between",
                        align_items="center",
                        padding="1em",
                        width="100%",
                    ),
                    width="100%",
                    justify="center",
                ),
                rx.el.main(
                    rx.box(
                        sidebar,
                        class_name="h-full shrink-0 desktop-only lg:w-[24%]",
                    ),
                    rx.box(
                        rx.box(
                            class_name="px-0 lg:px-20 pt-11 sm:pt-0",
                        ),
                        rx.box(
                            rx.el.article(comp),
                            rx.el.nav(
                                *links,
                                class_name="flex flex-row gap-2 mt-8 lg:mt-10 mb-6 lg:mb-12",
                            ),
                            class_name="lg:mt-0 mt-6 px-4 lg:px-20",
                        ),
                        class_name="h-full w-full" + main_content_width,
                    ),
                    (
                        rx.el.nav(
                            rx.box(
                                rx.el.h5(
                                    "On this page",
                                    class_name="font-smbold text-[0.875rem] text-slate-12 hover:text-violet-9 leading-5 tracking-[-0.01313rem] transition-color",
                                ),
                                rx.el.ul(
                                    *[
                                        (
                                            rx.el.li(
                                                rx.link(
                                                    text,
                                                    class_name="font-small text-slate-9 hover:!text-slate-11 whitespace-normal transition-color",
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
                                                        class_name="font-small text-slate-9 hover:!text-slate-11 whitespace-normal transition-color",
                                                        underline="none",
                                                        href=path
                                                        + "#"
                                                        + text.lower().replace(
                                                            " ", "-"
                                                        ),
                                                    )
                                                )
                                                if level == 2
                                                else rx.el.li(
                                                    rx.link(
                                                        text,
                                                        underline="none",
                                                        class_name="pl-6 font-small text-slate-9 hover:!text-slate-11  transition-color",
                                                        href=path
                                                        + "#"
                                                        + text.lower().replace(
                                                            " ", "-"
                                                        ),
                                                    )
                                                )
                                            )
                                        )
                                        for level, text in table_of_contents
                                    ],
                                    class_name="flex flex-col gap-4 list-none",
                                ),
                                class_name="fixed flex flex-col justify-start gap-4 p-[0.875rem_0.5rem_0px_0.5rem] max-h-[80vh] overflow-y-scroll",
                                style={"width": "inherit"},
                            ),
                            class_name="shrink-0 w-[16%]"
                            + (
                                " hidden xl:flex xl:flex-col"
                                if show_right_sidebar and not pseudo_right_bar
                                else " hidden"
                            ),
                            id="toc-navigation",
                        )
                        if not pseudo_right_bar or show_right_sidebar
                        else rx.spacer()
                    ),
                    class_name="justify-center flex flex-row mx-auto mt-0 max-w-[94.5em] h-full min-h-screen w-full",
                ),
                class_name="flex flex-col justify-center bg-slate-1 w-full",
            )

        components = path.split("/")
        category = (
            " ".join(
                word.capitalize() for word in components[2].replace("-", " ").split()
            )
            if len(components) > 2
            else None
        )
        if page_title:
            return Route(
                path=path,
                title=page_title,
                component=wrapper,
            )
        return Route(
            path=path,
            title=f"{title} · Reflex Docs" if category is None else title,
            component=wrapper,
        )

    return docpage


@dataclasses.dataclass(init=False)
class Source:
    """Parse the source code of a component."""

    # The component to parse.
    component: type[Component]

    # The source code.
    code: list[str] = dataclasses.field(default_factory=list)

    def __init__(self, component: type[Component]):
        """Initialize the source code parser."""
        self.component = component

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
        return self.component.__doc__ or ""

    def get_props(self) -> list[Prop]:
        """Get a dictionary of the props and their descriptions.

        Returns:
            A dictionary of the props and their descriptions.
        """
        props = self._get_props()

        parent_cls = self.component.__bases__[0]
        if parent_cls != rx.Component and parent_cls != BaseHTML:
            parent_props = Source(component=parent_cls).get_props()
            # filter out the props that have been overridden in the parent class.
            props += [
                prop
                for prop in parent_props
                if prop.name not in {p.name for p in props}
            ]

        return props

    def _get_props(self) -> list[Prop]:
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
                if not comment_above.startswith("#"):
                    msg = f"Expected comment above prop {prop}, got {comment_above}"
                    raise ValueError(msg)

            comment = Source.get_comment(comments)
            comments.clear()

            type_ = self.component.get_fields()[prop].outer_type_

            out.append(
                Prop(
                    name=prop,
                    type_=type_,
                    default_value=default_value,
                    description=comment,
                )
            )

        return out

    @staticmethod
    def get_comment(comments: list[str]):
        return "".join([comment.strip().strip("#") for comment in comments])


def get_code_style(color: ColorType):
    return {
        "color": rx.color(color, 11),
        "border_radius": "0.25rem",
        "border": f"1px solid {rx.color(color, 5)}",
        "background": rx.color(color, 3),
    }


count = 0


def get_id(s):
    global count
    count += 1
    s = str(count)
    hash_object = hashlib.sha256(s.encode())
    hex_dig = hash_object.hexdigest()
    return "a_" + hex_dig[:8]


class PropDocsState(rx.State):
    """Container for dynamic vars used by the prop docs."""


def hovercard(trigger: rx.Component, content: rx.Component) -> rx.Component:
    return rx.hover_card.root(
        rx.hover_card.trigger(
            trigger,
        ),
        rx.hover_card.content(
            content,
            side="top",
            align="center",
            class_name="font-small text-slate-11",
        ),
    )


def color_scheme_hovercard(literal_values: list[str]) -> rx.Component:
    return hovercard(
        rx.icon(tag="palette", size=15, class_name="!text-slate-9 shrink-0"),
        rx.grid(
            *[
                rx.tooltip(
                    rx.box(
                        bg=f"var(--{color}-9)", class_name="rounded-md size-8 shrink-0"
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


def prop_docs(prop: Prop) -> list[rx.Component]:
    """Generate the docs for a prop."""
    # Get the type of the prop.
    type_ = prop.type_
    if get_origin(type_) is rx.Var:
        # For vars, get the type of the var.
        type_ = get_args(type_)[0]

    origin = get_origin(type_)
    args = get_args(type_)

    literal_values = []  # Literal values of the prop
    all_types = []  # List for all the prop types
    max_prop_values = 2

    short_type_name = None

    common_types = {}  # Used to exclude common types from the MAX_PROP_VALUES
    if origin in (Union, UnionType):
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

        short_type_name = "Union"

    elif origin is dict:
        key_type = args[0].__name__ if args else "Any"
        value_type = (
            getattr(args[1], "__name__", str(args[1])) if len(args) > 1 else "Any"
        )
        type_name = f"Dict[{key_type}, {value_type}]"
        short_type_name = "Dict"

    elif origin is Literal:
        literal_values = list(map(str, args))
        if len(literal_values) > max_prop_values and prop.name not in common_types:
            type_name = "Literal"
        else:
            type_name = " | ".join([f'"{value}"' for value in literal_values])
        short_type_name = "Literal"

    else:
        type_name = type_.__name__
        short_type_name = type_name

    # Get the default value.
    default_value = prop.default_value if prop.default_value is not None else "-"
    # Get the color of the prop.
    color = TYPE_COLORS.get(short_type_name, "gray")
    # Return the docs for the prop.
    return [
        rx.table.cell(
            rx.box(
                rx.code(prop.name, class_name="code-style text-nowrap leading-normal"),
                hovercard(
                    rx.icon(
                        tag="info",
                        size=15,
                        class_name="!text-slate-9 shrink-0",
                    ),
                    rx.text(prop.description, class_name="font-small text-slate-11"),
                ),
                class_name="flex flex-row items-center gap-2",
            ),
            class_name="justify-start pl-4",
        ),
        rx.table.cell(
            rx.box(
                rx.cond(
                    (len(literal_values) > 0) & (prop.name not in common_types),
                    rx.code(
                        (
                            " | ".join(
                                [f'"{v}"' for v in literal_values[:max_prop_values]]
                                + ["..."]
                            )
                            if len(literal_values) > max_prop_values
                            else type_name
                        ),
                        style=get_code_style(color),
                        class_name="code-style text-nowrap leading-normal",
                    ),
                    rx.code(
                        type_name,
                        style=get_code_style(color),
                        class_name="code-style text-nowrap leading-normal",
                    ),
                ),
                rx.cond(
                    len(literal_values) > max_prop_values
                    and prop.name not in common_types,
                    hovercard(
                        rx.icon(
                            tag="circle-ellipsis",
                            size=15,
                            class_name="!text-slate-9 shrink-0",
                        ),
                        rx.text(
                            " | ".join([f'"{v}"' for v in literal_values]),
                            class_name="font-small text-slate-11",
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
                            class_name="!text-slate-9 shrink-0",
                        ),
                        rx.text(
                            f"Union[{', '.join(all_types)}]",
                            class_name="font-small text-slate-11",
                        ),
                    ),
                ),
                rx.cond(
                    (prop.name == "color_scheme") | (prop.name == "accent_color"),
                    color_scheme_hovercard(literal_values),
                ),
                class_name="flex flex-row items-center gap-2",
            ),
            class_name="justify-start pl-4",
        ),
        rx.table.cell(
            rx.box(
                rx.code(
                    default_value,
                    style=get_code_style(
                        "red"
                        if default_value == "False"
                        else "green"
                        if default_value == "True"
                        else "gray"
                    ),
                    class_name="code-style leading-normal text-nowrap",
                ),
                class_name="flex",
            ),
            class_name="justify-start pl-4",
        ),
    ]


def generate_props(src, component, comp):
    if len(src.get_props()) == 0:
        return rx.box(
            rx.heading("Props", as_="h3", class_name="font-large text-slate-12"),
            rx.text("No component specific props", class_name="text-slate-9 font-base"),
            class_name="flex flex-col overflow-x-auto justify-start py-2 w-full",
        )

    table_header_class_name = (
        "font-small text-slate-12 text-normal w-auto justify-start pl-4 font-bold"
    )

    prop_dict = {}

    body = rx.table.body(
        *[
            rx.table.row(*prop_docs(prop), align="center")
            for prop in src.get_props()
            if not prop.name.startswith("on_")  # ignore event trigger props
        ],
        class_name="bg-slate-2",
    )

    try:
        if f"{component.__name__}" in comp.metadata:
            comp = eval(comp.metadata[component.__name__])(**prop_dict)

        else:
            comp = rx.fragment()
    except Exception as e:
        print(f"Failed to create component {component.__name__}, error: {e}")  # noqa: T201
        comp = rx.fragment()

    interactive_component = (
        docdemobox(comp) if not isinstance(comp, Fragment) else "",
    )
    return rx.vstack(
        interactive_component,
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
                            class_name=table_header_class_name,
                        ),
                        rx.table.column_header_cell(
                            "Type | Values",
                            class_name=table_header_class_name,
                        ),
                        rx.table.column_header_cell(
                            "Default",
                            class_name=table_header_class_name,
                        ),
                        rx.table.column_header_cell(
                            "Interactive",
                            class_name=table_header_class_name,
                        ),
                    ),
                    class_name="bg-slate-3",
                ),
                body,
                variant="surface",
                size="1",
                class_name="px-0 w-full border border-slate-4",
            ),
            class_name="max-h-96 mb-4",
        ),
    )


def generate_valid_children(comp):
    if not comp._valid_children:
        return rx.text("")

    valid_children = [
        rx.code(child, class_name="code-style leading-normal")
        for child in comp._valid_children
    ]
    return rx.box(
        rx.heading("Valid Children", as_="h3", class_name="font-large text-slate-12"),
        rx.box(*valid_children, class_name="flex flex-row gap-2 flex-wrap"),
        class_name="pb-6 w-full items-start flex flex-col gap-4",
    )


# Default event triggers.
default_triggers = rx.Component.create().get_event_triggers()


def same_trigger(t1, t2):
    if t1 is None or t2 is None:
        return False
    t1 = t1 if not isinstance(t1, Sequence) else t1[0]
    t2 = t2 if not isinstance(t2, Sequence) else t2[0]
    args1 = inspect.getfullargspec(t1).args
    args2 = inspect.getfullargspec(t2).args
    return args1 == args2


def generate_event_triggers(comp: type[Component], src):
    prop_name_to_description = {
        prop.name: prop.description
        for prop in src.get_props()
        if prop.name.startswith("on_")
    }
    triggers = comp._unsafe_create(children=[]).get_event_triggers()
    custom_events = [
        event
        for event in triggers
        if not same_trigger(triggers.get(event), default_triggers.get(event))
    ]

    if not custom_events:
        return rx.box(
            rx.heading(
                "Event Triggers", as_="h3", class_name="font-large text-slate-12"
            ),
            rx.link(
                "See the full list of default event triggers",
                href="https://reflex.dev/docs/api-reference/event-triggers/",
                class_name="text-violet-11 font-base",
                is_external=True,
            ),
            class_name="py-2 overflow-x-auto justify-start flex flex-col gap-4",
        )
    table_header_class_name = (
        "font-small text-slate-12 text-normal w-auto justify-start pl-4 font-bold"
    )
    return rx.box(
        rx.heading("Event Triggers", as_="h3", class_name="font-large text-slate-12"),
        rx.link(
            "See the full list of default event triggers",
            href="https://reflex.dev/docs/api-reference/event-triggers/",
            class_name="text-violet-11 font-base",
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
                            "Trigger", class_name=table_header_class_name
                        ),
                        rx.table.column_header_cell(
                            "Description", class_name=table_header_class_name
                        ),
                    ),
                    class_name="bg-slate-3",
                ),
                rx.table.body(
                    *[
                        rx.table.row(
                            rx.table.cell(
                                rx.code(event, class_name="code-style"),
                                class_name="justify-start p-4",
                            ),
                            rx.table.cell(
                                prop_name_to_description.get(event)
                                or EVENTS[event]["description"],
                                class_name="justify-start p-4 text-slate-11 font-small",
                            ),
                        )
                        for event in custom_events
                    ],
                    class_name="bg-slate-2",
                ),
                variant="surface",
                size="1",
                class_name="w-full border border-slate-4",
            ),
            class_name="w-full justify-start overflow-hidden",
        ),
        class_name="pb-6 w-full justify-start flex flex-col gap-6 max-h-[40rem]",
    )


def component_docs(component_tuple, comp):
    """Generates documentation for a given component."""

    component = component_tuple[0]
    src = Source(component=component)
    props = generate_props(src, component, comp)
    triggers = generate_event_triggers(component, src)
    children = generate_valid_children(component)

    return rx.box(
        h2_comp(text=component_tuple[1]),
        rx.box(markdown(textwrap.dedent(src.get_docs())), class_name="pb-2"),
        props,
        children,
        triggers,
        class_name="pb-8 w-full text-left",
    )


def get_headings(
    comp: mistletoe.Document | mistletoe.token.Token,
) -> list[tuple[int, str]]:
    """Get the strings from markdown component."""
    if isinstance(comp, mistletoe.block_token.Heading):
        heading_text = comp.content
        return [(comp.level, heading_text)]

    # Recursively get the strings from the children.
    if not hasattr(comp, "children") or comp.children is None:
        return []

    headings = []
    for child in comp.children:
        headings.extend(get_headings(child))
    return headings


def get_table_of_contents(
    source: flexdown.Document,
    href: str,
    component_list: list[tuple[type, str]] | None = None,
):
    component_list = component_list or []

    # Generate the TOC
    # The environment used for execing and evaling code.
    env = source.metadata
    env["__xd"] = xd

    # Get the content of the document.
    source_str = source.content

    # Get the blocks in the source code.
    # Note: we must use reflex-web's special flexdown instance xd here - it knows about all custom block types (like DemoBlock)
    blocks = xd.get_blocks(source_str, href)

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
    for _, component_name in component_list:
        headings.append((2, component_name))
    return headings


def multi_docs(
    path: str,
    comp: flexdown.Document,
    component_list: tuple[str, list[tuple[type, str]]],
    title: str,
    chakra_components: dict[str, list[tuple[str, list[tuple[type, str]]]]],
):
    components = [
        component_docs(component_tuple, comp) for component_tuple in component_list[1]
    ]
    fname = path.strip("/") + ".md"

    @docpage(set_path=path, t=title, chakra_components=chakra_components)
    def out():
        table_of_contents = get_table_of_contents(comp, fname, component_list[1])
        return table_of_contents, rx.box(
            xd.render(comp, filename=fname),
            h1_comp(text="API Reference"),
            rx.box(*components, class_name="flex flex-col"),
            class_name="flex flex-col w-full",
        )

    return out
