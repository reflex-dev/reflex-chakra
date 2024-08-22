---
components:
    - rc.Center
    - rc.Circle
    - rc.Square
---

# Center

```python exec
import reflex_chakra as rc
import reflex as rx
```

Center, Square, and Circle are components that center its children within itself.

```python demo
rc.center(
    rc.text("Hello World!"),
    border_radius="15px",
    border_width="thick",
    width="50%",
)
```

Below are examples of circle and square.

```python demo
rc.hstack(
    rc.square(
        rc.vstack(rc.text("Square")),
        border_width="thick",
        border_color="purple",
        padding="1em",
    ),
    rc.circle(
        rc.vstack(rc.text("Circle")),
        border_width="thick",
        border_color="orange",
        padding="1em",
    ),
    spacing="2em",
)
```
