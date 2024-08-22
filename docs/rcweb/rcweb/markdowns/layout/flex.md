---
components:
    - rc.Flex
---

# Flex

```python exec
import reflex_chakra as rc
import reflex as rx
```

Flexbox is a layout model that allows elements to align and distribute space within a container. Using flexible widths and heights, elements can be aligned to fill a space or distribute space between elements, which makes it a great tool to use for responsive design systems.

```python demo
rc.flex(
    rc.center("Center", bg="lightblue"),
    rc.square("Square", bg="lightgreen", padding=10),
    rc.box("Box", bg="salmon", width="150px"),
)
```

Combining flex with spacer allows for stackable and responsive components.

```python demo
rc.flex(
    rc.center("Center", bg="lightblue"),
    rc.spacer(),
    rc.square("Square", bg="lightgreen", padding=10),
    rc.spacer(),
    rc.box("Box", bg="salmon", width="150px"),
    width = "100%",
)
```
