---
components:
    - rc.Spacer
---

# Spacer

```python exec
import reflex_chakra as rc
import reflex as rx
```

Creates an adjustable, empty space that can be used to tune the spacing between child elements within Flex.

```python demo
rc.flex(
    rc.center(rc.text("Example"), bg="lightblue"),
    rc.spacer(),
    rc.center(rc.text("Example"), bg="lightgreen"),
    rc.spacer(),
    rc.center(rc.text("Example"), bg="salmon"),
    width="100%",
)
```
