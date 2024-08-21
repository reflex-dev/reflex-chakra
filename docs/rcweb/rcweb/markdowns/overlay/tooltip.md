---
components:
    - rc.Tooltip
---

```python exec
import reflex_chakra as rc
import reflex as rx
```

# Tooltip

A tooltip is a brief, informative message that appears when a user interacts with an element.
Tooltips are usually initiated in one of two ways: through a mouse-hover gesture or through a keyboard-hover gesture.

```python demo
rc.tooltip(
    rc.text("Example", font_size=30),
    label="Tooltip helper.",
)
```
