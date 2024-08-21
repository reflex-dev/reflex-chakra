---
components:
    - rc.Container
---

# Container

```python exec
import reflex_chakra as rc
import reflex as rx
```

Containers are used to constrain a content's width to the current breakpoint, while keeping it fluid.

```python demo
rc.container(
    rc.box("Example", bg="blue", color="white", width="50%"),
    center_content=True,
    bg="lightblue",
)
```
