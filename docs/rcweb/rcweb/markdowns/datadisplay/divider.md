---
components:
    - rc.Divider
---

```python exec
import reflex_chakra as rc
import reflex as rx
```

# Divider

Dividers are a quick built in way to separate sections of content.

```python demo
rc.vstack(
    rc.text("Example"),
    rc.divider(border_color="black"),
    rc.text("Example"),
    rc.divider(variant="dashed", border_color="black"),
    width="100%",
)
```

If the vertical orientation is used, make sure that the parent component is assigned a height.

```python demo
rc.center(
    rc.divider(
        orientation="vertical", 
        border_color = "black"
    ), 
    height = "4em"
)
```
