from __future__ import annotations

import reflex as rx
import reflex_chakra as rc
from ..constants import fonts

chakra_lib_items = []


class SidebarItem(rx.Base):
    """A single item in the sidebar."""

    # The name to display in the sidebar.
    names: str = ""

    alt_name_for_next_prev: str = ""

    # The link to navigate to when the item is clicked.
    link: str = ""

    # The children items.
    children: list[SidebarItem] = []

    # Whether the item is a category. Occurs if a single item is at the top level of the sidebar for asthetics.
    outer = False


def calculate_index(sidebar_items, url: str):
    if isinstance(sidebar_items, list):
        return None
    if not isinstance(sidebar_items, list):
        sidebar_items = [sidebar_items]
    if url is None:
        return None
    for item in sidebar_items:
        if not item.link.endswith("/"):
            item.link = item.link + "/"
    if not url.endswith("/"):
        url = url + "/"
    sub = 0
    for i, item in enumerate(sidebar_items):
        if len(item.children) == 0:
            sub += 1
        if item.link == url:
            return [i - sub]
        index = calculate_index(item.children, url)
        if index is not None:
            return [i - sub] + index
    return None


def get_component_link(category: str | None, clist, prefix="") -> str:
    component_name = rx.utils.format.to_kebab_case(clist[0])
    # construct the component link. The component name points to the name of the md file.
    return "/".join(
        [prefix, category.lower().replace(' ', '-') if category else '', component_name.lower()]).replace("//", "/")


def get_category_children(category, category_list, prefix="") -> SidebarItem | list[SidebarItem]:
    category = category.replace("-", " ")
    if isinstance(category_list, dict):
        category_children = []
        for c in category_list:
            category_child = get_category_children(c, category_list[c])
            category_children.extend(category_child) if isinstance(category_child, list) else category_children.append(
                category_child)

        return SidebarItem(
            names=category,
            children=[
                category_children
            ],
        )
    category_item_children = []
    for c in category_list:
        component_name = rx.utils.format.to_snake_case(c[0])
        name = rx.utils.format.to_title_case(component_name)
        item = SidebarItem(
            names=name,
            link=get_component_link(category, c) if not category == "Markdowns" else get_component_link(None, c),
        )
        category_item_children.append(item)
    return SidebarItem(names=category,
                       children=category_item_children) if not category == "Markdowns" else category_item_children


def get_sidebar_items_other_libraries(chakra_components):
    chakra_children = []
    for category in chakra_components:
        category_item = get_category_children(
            category,
            chakra_components[category],
        )
        chakra_children.extend(category_item) if isinstance(category_item, list) else chakra_children.append(
            category_item)
    return chakra_children


class NavbarState(rx.State):
    """The state for the navbar component."""

    # Whether the sidebar is open.
    sidebar_open: bool = False

    search_input: str = ""

    enter: bool = False

    banner: bool = True

    ai_chat: bool = True

    current_category = "All"

    def toggle_banner(self):
        self.banner = not self.banner

    def toggle_sidebar(self):
        self.sidebar_open = not self.sidebar_open

    def toggle_ai_chat(self):
        self.ai_chat = not self.ai_chat

    def update_category(self, tag):
        self.current_category = tag


def sidebar_link(*children, **props):
    """Create a sidebar link that closes the sidebar when clicked."""
    on_click = props.pop("on_click", NavbarState.set_sidebar_open(False))
    return rx.link(
        *children,
        on_click=on_click,
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


def sidebar_icon(name):
    mappings = {
        "Getting Started": "rocket",
        "Tutorial": "life-buoy",
        "Components": "layers",
    }

    if name in mappings:
        return rx.icon(
            tag=mappings[name],
            size=16,
            margin_right="20px",
        )
    else:
        return rx.fragment()


def sidebar_item_comp(
        item: SidebarItem,
        index: list[int],
        url: str,
):
    return rx.cond(
        len(item.children) == 0,
        sidebar_leaf(item=item, url=url)
        if not item.names in ("Introduction",)
        else rc.accordion_item(
            rc.accordion_button(
                sidebar_icon(item.names),
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
                    href=format_sidebar_route(item.link)
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
                sidebar_icon(item.names),
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


def create_sidebar_section(items, index, url):
    nested = False
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
            default_index=rx.cond(index, index, []),
            width="100%",
            padding_left="0em",
            margin_left="0em",
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
        other_libs_index: list[int],
        width: str = "100%",
):
    ul_style = {
        "display": "flex",
        "flex_direction": "column",
        "align_items": "flex-start",
    }
    return rx.flex(
        # rx.link(
        #     rx.heading(
        #         "introduction",
        #         as_="h5",
        #         style={
        #             "color": rx.color("slate", 12),
        #             "font-family": "Instrument Sans",
        #             "font-size": "14px",
        #             "font-style": "normal",
        #             "font-weight": "600",
        #             "line-height": "20px",
        #             "letter-spacing": "-0.21px",
        #             "transition": "color 0.035s ease-out",
        #             "_hover": {
        #                 "color": rx.color("violet", 9),
        #             },
        #         },
        #     ),
        #     underline="none",
        #     padding_y="12px",
        #     href="/introduction",
        # ),
        rx.unordered_list(
            create_sidebar_section(
                chakra_lib_items,
                other_libs_index,
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


def sidebar(chakra_components, url=None, width: str = "100%") -> rx.Component:
    """Render the sidebar."""
    global chakra_lib_items
    chakra_lib_items = get_sidebar_items_other_libraries(chakra_components)
    other_libs_index = calculate_index(chakra_lib_items, url)
    return rx.flex(
        sidebar_comp(
            url=url,
            other_libs_index=other_libs_index,
            width=width,
        ),
        width="100%",
        height="100%",
        justify="end",
    )
