---
components:
    - rc.RadioGroup
    - rc.Radio
---

```python exec
import reflex_chakra as rc
import reflex as rx
```

# Radio

Radios are used when only one choice may be selected in a series of options.

```python demo exec
from typing import List
options: List[str] = ["Option 1", "Option 2", "Option 3"]

class RadioState(rx.State):
    text: str = "No Selection"


def basic_radio_example():
    return rc.vstack(
        rc.badge(RadioState.text, color_scheme="green"),
        rc.radio_group(
            options,
            on_change=RadioState.set_text,
        ),
    )
```

The `default_value` and `default_checked` arguments can be used to set the default value of the radio group.

```python demo
rc.vstack(
    rc.radio_group(
        options,
        default_value="Option 2",
        default_checked=True,
    ),
)
```

A hstack with the `spacing` argument can be used to set the spacing between the radio buttons.

```python demo
rc.radio_group(
    rc.radio_group(
        rc.hstack(
            rx.foreach(
                options,
                lambda option: rc.radio(option),
            ),
        spacing="2em",
        ),
    ),
)
```

A vstack can be used to stack the radio buttons vertically.

```python demo
rc.radio_group(
    rc.radio_group(
        rc.vstack(
            rx.foreach(
                options,
                lambda option: rc.radio(option),
            ),
        ),
    ),
)
```
