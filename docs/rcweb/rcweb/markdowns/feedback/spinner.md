---
components:
    - rc.Spinner
---

```python exec
import reflex_chakra as rc
import reflex as rx
```

# Spinner

Spinners provide a visual cue that an event is either processing, awaiting a course of change or a result.

```python demo
rc.hstack(
    rc.spinner(color="red", size="xs"),
    rc.spinner(color="orange", size="sm"),
    rc.spinner(color="green", size="md"),
    rc.spinner(color="blue", size="lg"),
    rc.spinner(color="purple", size="xl"),
)
```

Along with the color you can style further with props such as speed, empty color, and thickness.

```python demo
rc.hstack(
    rc.spinner(color="lightgreen", thickness=1, speed="1s", size="xl"),
    rc.spinner(color="lightgreen", thickness=5, speed="1.5s", size="xl"),
    rc.spinner(
        color="lightgreen",
        thickness=10,
        speed="2s",
        empty_color="red",
        size="xl",
    ),
)
```
