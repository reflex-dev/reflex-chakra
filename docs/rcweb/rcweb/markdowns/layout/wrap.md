---
components:
    - rc.Wrap
    - rc.WrapItem
---

# Wrap

```python exec
import reflex_chakra as rc
import reflex as rx
```

Wrap is a layout component that adds a defined space between its children.

It wraps its children automatically if there isn't enough space to fit any more in the same row. Think of it as a smarter flex-wrap with spacing support.

```python demo
rc.wrap(
    rc.wrap_item(rc.box("Example", bg="lightgreen", w="100px", h="80px")),
    rc.wrap_item(rc.box("Example", bg="lightblue", w="200px", h="80px")),
    rc.wrap_item(rc.box("Example", bg="red", w="300px", h="80px")),
    rc.wrap_item(rc.box("Example", bg="orange", w="400px", h="80px")),
    width="100%",
    spacing="2em",
    align="center",
)
```
