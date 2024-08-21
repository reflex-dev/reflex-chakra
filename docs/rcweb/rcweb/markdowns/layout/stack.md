---
components:
    - rc.Stack
    - rc.Hstack
    - rc.Vstack
---

# Stack

```python exec
import reflex_chakra as rc
import reflex as rx
```

Below are two examples the different types of stack components vstack and hstack for ordering items on a page.

```python demo
rc.hstack(
    rc.box("Example", bg="red", border_radius="md", width="10%"),
    rc.box("Example", bg="orange", border_radius="md", width="10%"),
    rc.box("Example", bg="yellow", border_radius="md", width="10%"),
    rc.box("Example", bg="lightblue", border_radius="md", width="10%"),
    rc.box("Example", bg="lightgreen", border_radius="md", width="60%"),
    width="100%",
)
```

```python demo
rc.vstack(
    rc.box("Example", bg="red", border_radius="md", width="20%"),
    rc.box("Example", bg="orange", border_radius="md", width="40%"),
    rc.box("Example", bg="yellow", border_radius="md", width="60%"),
    rc.box("Example", bg="lightblue", border_radius="md", width="80%"),
    rc.box("Example", bg="lightgreen", border_radius="md", width="100%"),
    width="100%",
)
```
