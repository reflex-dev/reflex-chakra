from crm.state import State, LoginState
import reflex as rx
import reflex_chakra as rc


def navbar():
    return rc.box(
        rc.hstack(
            rc.link("Pyneknown", href="/", font_weight="medium"),
            rc.hstack(
                rx.cond(
                    State.user,
                    rc.hstack(
                        rc.link(
                            "Log out",
                            color="blue.600",
                            on_click=LoginState.log_out,
                        ),
                        rc.avatar(name=State.user.email, size="md"),
                        spacing="1rem",
                    ),
                    rc.box(),
                )
            ),
            justify_content="space-between",
        ),
        width="100%",
        padding="1rem",
        margin_bottom="2rem",
        border_bottom="1px solid black",
    )
