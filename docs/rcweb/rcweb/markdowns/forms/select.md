---
components:
    - rc.Select
---

```python exec
import reflex_chakra as rc
import reflex as rx
```

# Select

The Select component is used to create a list of options, which allows a user to select one or more options from it.

```python demo exec
from typing import List
options: List[str] = ["Option 1", "Option 2", "Option 3"]

class SelectState(rx.State):
    option: str = "No selection yet."


def basic_select_example():
    return rc.vstack(
        rc.heading(SelectState.option),
        rc.select(
            options,
            placeholder="Select an example.",
            on_change=SelectState.set_option,
            color_schemes="twitter",
        ),
    )
```

Select can also have multiple options selected at once.

```python demo exec
from typing import List
options: List[str] = ["Option 1", "Option 2", "Option 3"]

class MultiSelectState(rx.State):
    option: List[str] = []


def multiselect_example():
    return rc.vstack(
        rc.heading(MultiSelectState.option),
        rc.select(
            options, 
            placeholder="Select examples", 
            is_multi=True,
            on_change=MultiSelectState.set_option,
            close_menu_on_select=False,
            color_schemes="twitter",
        ),
    )
```

The component can also be customized and styled as seen in the next examples.

```python demo
rc.vstack(
    rc.select(options, placeholder="Select an example.", size="xs"),
    rc.select(options, placeholder="Select an example.", size="sm"),
    rc.select(options, placeholder="Select an example.", size="md"),
    rc.select(options, placeholder="Select an example.", size="lg"),
)
```

```python demo
rc.vstack(
    rc.select(options, placeholder="Select an example.", variant="outline"),
    rc.select(options, placeholder="Select an example.", variant="filled"),
    rc.select(options, placeholder="Select an example.", variant="flushed"),
    rc.select(options, placeholder="Select an example.", variant="unstyled"),
)
```

```python demo
rc.select(
    options,
    placeholder="Select an example.",
    color="white",
    bg="#68D391",
    border_color="#38A169",
)
```
