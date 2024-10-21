import reflex as rx
import reflex_chakra as rc


def navbar():
    return rc.box(
        rc.hstack(
            rc.hstack(
                rc.image(src="/nba.png", width="50px"),
                rc.heading("NBA Data"),
                rc.flex(
                    rc.badge("2015-2016 Season", color_scheme="blue"),
                ),
            ),
            rc.menu(
                rc.menu_button(
                    "Menu", bg="black", color="white", border_radius="md", px=4, py=2
                ),
                rc.menu_list(
                    rc.link(rc.menu_item("Graph"), href="/"),
                    rc.menu_divider(),
                    rc.link(
                        rc.menu_item(
                            rc.hstack(rc.text("20Dataset"), rc.icon(tag="download"))
                        ),
                        href="https://media.geeksforgeeks.org/wp-content/uploads/nba.csv",
                    ),
                ),
            ),
            justify="space-between",
            border_bottom="0.2em solid #F0F0F0",
            padding_x="2em",
            padding_y="1em",
            bg="rgba(255,255,255, 0.97)",
        ),
        position="fixed",
        width="100%",
        top="0px",
        z_index="500",
    )
