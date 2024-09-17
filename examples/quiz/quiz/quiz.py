"""Welcome to Reflex! This file outlines the steps to create a basic app."""
import reflex as rx
import reflex_chakra as rc
import copy
from .results import results
from typing import Any
from typing import List

question_style = {
    "bg": "white",
    "padding": "2em",
    "border_radius": "25px",
    "w": "100%",
    "align_items": "left",
}


class State(rx.State):
    """The app state."""

    default_answers = [None, None, [False, False, False, False, False]]
    answers: List[Any]
    answer_key = ["False", "[10, 20, 30, 40]", [False, False, True, True, True]]
    score: int

    def onload(self):
        self.answers = copy.deepcopy(self.default_answers)

    def set_answers(self, answer, index, sub_index=None):
        if sub_index is None:
            self.answers[index] = answer
        else:
            self.answers[index][sub_index] = answer

    def submit(self):
        total, correct = 0, 0
        for i in range(len(self.answers)):
            if self.answers[i] == self.answer_key[i]:
                correct += 1
            total += 1
        self.score = int(correct / total * 100)
        return rx.redirect("/result")

    @rx.var
    def percent_score(self):
        return f"{self.score}%"


def header():
    return rc.vstack(
        rc.heading("Python Quiz"),
        rc.divider(),
        rc.text("Here is an example of a quiz made in Reflex."),
        rc.text("Once submitted the results will be shown in the results page."),
        style=question_style,
    )


def question1():
    """The main view."""
    return rc.vstack(
        rc.heading("Question #1"),
        rc.text(
            "In Python 3, the maximum value for an integer is 26",
            rc.text("3", as_="sup"),
            " - 1",
        ),
        rc.divider(),
        rc.radio_group(
            ["True", "False"],
            default_value=State.default_answers[0],
            default_checked=True,
            on_change=lambda answer: State.set_answers(answer, 0),
        ),
        style=question_style,
    )


def question2():
    return rc.vstack(
        rc.heading("Question #2"),
        rc.text("What is the output of the following addition (+) operator?"),
        rc.code_block(
            """a = [10, 20]
b = a
b += [30, 40]
print(a)""",
            language="python",
        ),
        rc.radio_group(
            ["[10, 20, 30, 40]", "[10, 20]"],
            default_value=State.default_answers[1],
            default_check=True,
            on_change=lambda answer: State.set_answers(answer, 1),
        ),
        style=question_style,
    )


def question3():
    return rc.vstack(
        rc.heading("Question #3"),
        rc.text(
            "Which of the following are valid ways to specify the string literal ",
            rc.code("foo'bar"),
            " in Python:",
        ),
        rc.vstack(
            rc.checkbox(
                rc.code("foo'bar"),
                on_change=lambda answer: State.set_answers(answer, 2, 0),
            ),
            rc.checkbox(
                rc.code("'foo''bar'"),
                on_change=lambda answer: State.set_answers(answer, 2, 1),
            ),
            rc.checkbox(
                rc.code("'foo\\\\'bar'"),
                on_change=lambda answer: State.set_answers(answer, 2, 2),
            ),
            rc.checkbox(
                rc.code('''"""foo'bar"""'''),
                on_change=lambda answer: State.set_answers(answer, 2, 3),
            ),
            rc.checkbox(
                rc.code('''"foo'bar"'''),
                on_change=lambda answer: State.set_answers(answer, 2, 4),
            ),
            align_items="left",
        ),
        style=question_style,
    )


def index():
    """The main view."""
    return rc.center(
        rc.vstack(
            header(),
            question1(),
            question2(),
            question3(),
            rc.button(
                "Submit",
                bg="black",
                color="white",
                width="6em",
                padding="1em",
                on_click=State.submit,
            ),
            spacing="1em",
        ),
        padding_y="2em",
        height="100vh",
        align_items="top",
        bg="#ededed",
        overflow="auto",
    )


def result():
    return results(State)


app = rx.App()
app.add_page(index, title="Reflex Quiz", on_load=State.onload)
app.add_page(result, title="Quiz Results")
