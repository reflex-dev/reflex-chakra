import reflex as rx
import reflex_chakra as rc

answer_style = {
    "border_radius": "10px",
    "border": "1px solid #ededed",
    "padding": "0.5em",
    "align_items": "left",
    "shadow": "0px 0px 5px 0px #ededed",
}


def render_answer(State, index):
    return rc.tr(
        rc.td(index + 1),
        rc.td(
            rx.cond(
                State.answers[index].to_string() == State.answer_key[index].to_string(),
                rc.icon(tag="check", color="green"),
                rc.icon(tag="close", color="red"),
            )
        ),
        rc.td(State.answers[index].to_string()),
        rc.td(State.answer_key[index].to_string()),
    )


def results(State):
    """The results view."""
    return rc.center(
        rc.vstack(
            rc.heading("Results"),
            rc.text("Below are the results of the quiz."),
            rc.divider(),
            rc.center(
                rc.circular_progress(
                    rc.circular_progress_label(State.percent_score),
                    value=State.score,
                    size="3em",
                )
            ),
            rc.table(
                rc.thead(
                    rc.tr(
                        rc.th("#"),
                        rc.th("Result"),
                        rc.th("Your Answer"),
                        rc.th("Correct Answer"),
                    )
                ),
                rx.foreach(State.answers, lambda answer, i: render_answer(State, i)),
            ),
            rc.box(rc.link(rc.button("Take Quiz Again"), href="/")),
            bg="white",
            padding_x="5em",
            padding_y="2em",
            border_radius="25px",
            align_items="left",
            overflow="auto",
        ),
        padding="1em",
        height="100vh",
        align_items="top",
        bg="#ededed",
        overflow="auto",
    )
