---
components:
    - rc.Checkbox
---

# Checkbox

A checkbox is a common way to toggle boolean value.
The checkbox component can be used on its own or in a group.

```python exec
import reflex_chakra as rc
import reflex as rx
```

```python demo
rc.checkbox("Check Me!")
```

Checkboxes can range in size and styles.

```python demo
rc.hstack(
    rc.checkbox("Example", color_scheme="green", size="sm"),
    rc.checkbox("Example", color_scheme="blue", size="sm"),
    rc.checkbox("Example", color_scheme="yellow", size="md"),
    rc.checkbox("Example", color_scheme="orange", size="md"),
    rc.checkbox("Example", color_scheme="red", size="lg"),
)
```

Checkboxes can also have different visual states.

```python demo
rc.hstack(
    rc.checkbox(
        "Example", color_scheme="green", size="lg", is_invalid=True
    ),
    rc.checkbox(
        "Example", color_scheme="green", size="lg", is_disabled=True
    ),
)
```

Checkboxes can be hooked up to a state using the `on_change` prop.

```python demo exec
import reflex_chakra as rc
import reflex as rx


class CheckboxState(rx.State):
    checked: bool = False

    def toggle(self):
        self.checked = not self.checked


def checkbox_state_example():
    return rc.hstack(
        rx.cond(
            CheckboxState.checked,
            rc.text("Checked", color="green"),
            rc.text("Unchecked", color="red"),
        ),
        rc.checkbox(
            "Example",
            on_change=CheckboxState.set_checked,
        )
    )
```
