from __future__ import annotations

import dataclasses

import reflex as rx
from reflex.utils.format import to_kebab_case, to_snake_case, to_title_case

import reflex_chakra as rc
from rcweb.constants import fonts

chakra_lib_items = []


@dataclasses.dataclass
class SidebarItem:
    """A single item in the sidebar."""

    # The name to display in the sidebar.
    names: str = ""

    alt_name_for_next_prev: str = ""

    # The link to navigate to when the item is clicked.
    link: str = ""

    # The children items.
    children: list[SidebarItem] = dataclasses.field(default_factory=list)

    # Whether the item is a category. Occurs if a single item is at the top level of the sidebar for asthetics.
    outer = False


def get_component_link(category: str | None, category_title: str):
    component_name = to_kebab_case(category_title)
    # construct the component link. The component name points to the name of the md file.
    return "/".join(
        [
            category.lower().replace(" ", "-") if category else "",
            component_name.lower(),
        ]
    ).replace("//", "/")


def get_category_children(
    category: str, category_list: list[tuple[str, list[tuple[type, str]]]]
) -> SidebarItem | list[SidebarItem]:
    category = category.replace("-", " ")
    category_item_children = []
    for component_title, _ in category_list:
        component_name = to_snake_case(component_title)
        name = to_title_case(component_name)
        item = SidebarItem(
            names=name,
            link=get_component_link(category, component_title)
            if category != "Markdowns"
            else get_component_link(None, component_title),
        )
        category_item_children.append(item)
    return (
        SidebarItem(names=category, children=category_item_children)
        if category != "Markdowns"
        else category_item_children
    )


def get_sidebar_items_other_libraries(
    chakra_components: dict[str, list[tuple[str, list[tuple[type, str]]]]],
) -> list[SidebarItem]:
    chakra_children: list[SidebarItem] = []
    for category, category_list in chakra_components.items():
        category_item = get_category_children(category, category_list)
        if isinstance(category_item, list):
            chakra_children.extend(category_item)
        else:
            chakra_children.append(category_item)
    return chakra_children


def sidebar_link(*children, **props):
    """Create a sidebar link that closes the sidebar when clicked."""
    return rx.link(
        *children,
        underline="none",
        **props,
    )


def format_sidebar_route(route: str) -> str:
    if not route.endswith("/"):
        route += "/"
    return route.replace("_", "-")


def sidebar_leaf(
    item: SidebarItem,
    url: str,
) -> rx.Component:
    """Get the leaf node of the sidebar."""
    item.link = item.link.replace("_", "-")
    if not item.link.endswith("/"):
        item.link += "/"
    if item.outer:
        return sidebar_link(
            rx.flex(
                rx.text(
                    item.names,
                    color=rx.cond(
                        item.link == url,
                        rx.color("violet", 9),
                        rx.color("slate", 9),
                    ),
                    _hover={
                        "color": rx.color("slate", 11),
                        "text_decoration": "none",
                    },
                    transition="color 0.035s ease-out",
                    margin_left="0.5em",
                    margin_top="0.5em",
                    margin_bottom="0.2em",
                    width="100%",
                ),
            ),
            href=item.link,
        )

    return rx.list_item(
        rc.accordion_item(
            rx.cond(
                item.link == url,
                sidebar_link(
                    rx.flex(
                        rx.flex(
                            rx.text(
                                item.names,
                                color=rx.color("violet", 9),
                                style={**fonts.small},
                                transition="color 0.035s ease-out",
                            ),
                        ),
                        padding="0px 8px 0px 28px",
                        border_left=f"1.5px solid {rx.color('violet', 9)}",
                    ),
                    _hover={"text_decoration": "none"},
                    href=item.link,
                ),
                sidebar_link(
                    rx.flex(
                        rx.text(
                            item.names,
                            color=rx.color("slate", 9),
                            _hover={
                                "color": rx.color("slate", 11),
                                "text_decoration": "none",
                            },
                            transition="color 0.035s ease-out",
                            style={**fonts.small},
                            width="100%",
                        ),
                        padding="0px 8px 0px 28px",
                        border_left=f"1.5px solid {rx.color('slate', 4)}",
                        _hover={"border_left": f"1.5px solid {rx.color('slate', 8)}"},
                    ),
                    _hover={"text_decoration": "none"},
                    href=item.link,
                ),
            ),
            border="none",
            width="100%",
        ),
        width="100%",
    )


def sidebar_item_comp(
    item: SidebarItem,
    index: list[int],
    url: str,
):
    return rx.cond(
        len(item.children) == 0,
        sidebar_leaf(item=item, url=url)
        if item.names not in ("Introduction",)
        else rc.accordion_item(
            rc.accordion_button(
                rx.link(
                    rx.text(
                        item.names,
                        style=fonts.small,
                        color=rx.cond(
                            format_sidebar_route(item.link) == url,
                            rx.color("violet", 9),
                            rx.color("slate", 9),
                        ),
                        _hover={
                            "color": rx.color("slate", 11),
                            "text_decoration": "none",
                        },
                    ),
                    href=format_sidebar_route(item.link),
                ),
                rx.box(
                    flex_grow=1,
                ),
                align_items="center",
                transition="color 0.035s ease-out",
                _hover={
                    "color": rx.color("slate", 11),
                },
                style={
                    "&[aria-expanded='true']": {
                        "color": rx.color("slate", 11),
                    },
                },
                color=rx.color("slate", 9),
                width="100%",
                padding_y="8px",
                padding_left="8px",
                padding_right="0px",
            ),
            border="none",
            width="100%",
        ),
        rc.accordion_item(
            rc.accordion_button(
                rx.text(
                    item.names,
                    style=fonts.small,
                ),
                rx.box(
                    flex_grow=1,
                ),
                rc.accordion_icon(width="16px", height="16px"),
                align_items="center",
                transition="color 0.035s ease-out",
                _hover={
                    "color": rx.color("slate", 11),
                },
                style={
                    "&[aria-expanded='true']": {
                        "color": rx.color("slate", 11),
                    },
                },
                color=rx.color("slate", 9),
                width="100%",
                padding_y="8px",
                padding_left="8px",
                padding_right="0px",
            ),
            rc.accordion_panel(
                rc.accordion(
                    rx.unordered_list(
                        *[
                            sidebar_item_comp(item=child, index=index, url=url)
                            for child in item.children
                        ],
                        align_items="flex-start",
                        flex_direction="column",
                        gap="16px",
                        display="flex",
                        margin_left="15px !important",
                        box_shadow=f"inset 1px 0 0 0 {rx.color('slate', 4)}",
                        list_style_type="none",
                    ),
                    margin_y="8px",
                    allow_multiple=True,
                    default_index=rx.cond(index, index[1:2], []),
                ),
                padding="0px",
                width="100%",
            ),
            border="none",
            width="100%",
        ),
    )


def create_sidebar_section(items: list[SidebarItem], url: str):
    return rx.list_item(
        rc.accordion(
            *[
                sidebar_item_comp(
                    item=item,
                    index=[-1],
                    url=url,
                )
                for item in items
            ],
            allow_multiple=True,
            default_index=[],
            width="100%",
            padding_left="0em",
            margin_left="0em",
            margin_top="5em",
        ),
        margin_left="0em",
        direction="column",
        width="100%",
        flex_direction="column",
        display="flex",
        align_items="left",
    )


@rx.memo
def sidebar_comp(
    url: str,
    width: str = "100%",
):
    ul_style = {
        "display": "flex",
        "flex_direction": "column",
        "align_items": "flex-start",
    }
    return rx.flex(
        rx.unordered_list(
            create_sidebar_section(
                chakra_lib_items,
                url,
            ),
            style=ul_style,
            margin_left="0px !important",
            list_style_type="none",
            padding="0px 16px 0px 8px",
            gap="24px",
        ),
        direction="column",
        align_items="left",
        overflow_y="scroll",
        max_height="90%",
        width=width,
        gap="24px",
        padding=["8px", "8px", "8px", "0px", "0px"],
        padding_bottom="6em !important",
        position="fixed",
        scrollbar_width="none",
        scroll_padding="1em",
        style={
            "&::-webkit-scrollbar-thumb": {
                "background_color": "transparent",
            },
            "&::-webkit-scrollbar": {
                "background_color": "transparent",
            },
        },
    )


class MobileAndTabletSidebarState(rx.State):
    drawer_is_open: bool = False

    @rx.event
    def toggle_drawer(self):
        self.drawer_is_open = not (self.drawer_is_open)


def sidebar_on_mobile_and_tablet(component):
    return rc.vstack(
        rc.drawer(
            rc.drawer_overlay(
                rc.drawer_content(
                    rc.box(
                        component,
                        margin_top="2em",
                    ),
                    rc.drawer_footer(
                        rc.icon_button(
                            rx.icon(
                                "x",
                                size=24,
                                style={
                                    "[data-state=open] &": {
                                        "display": "flex",
                                    },
                                    "[data-state=closed] &": {
                                        "display": "none",
                                    },
                                },
                                class_name="!text-slate-9 shrink-0",
                            ),
                            on_click=MobileAndTabletSidebarState.toggle_drawer,
                        )
                    ),
                    bg="rgba(0, 0, 0)",
                ),
            ),
            size="full",
            is_open=MobileAndTabletSidebarState.drawer_is_open,
            width="100vw",
        ),
        on_unmount=MobileAndTabletSidebarState.set_drawer_is_open(False),
    )


def get_sidebar_content(
    chakra_components: dict[str, list[tuple[str, list[tuple[type, str]]]]],
    url: str | None = None,
    width: str = "100%",
):
    global chakra_lib_items
    chakra_lib_items = get_sidebar_items_other_libraries(chakra_components)
    return sidebar_comp(
        url=url,
        width=width,
    )


def sidebar(
    chakra_components: dict[str, list[tuple[str, list[tuple[type, str]]]]],
    url: str | None = None,
    width: str = "100%",
) -> rx.Component:
    """Render the sidebar.

    Args:
        chakra_components: The components to display in the sidebar.
        url: The current URL to highlight the active link.
        width: The width of the sidebar.

    Returns:
        A sidebar component with the given components and URL.
    """
    return rx.flex(
        sidebar_on_mobile_and_tablet(
            get_sidebar_content(chakra_components, url, "100%")
        ),
        get_sidebar_content(chakra_components, url, width),
        width="100%",
        height="100%",
        justify="end",
    )
