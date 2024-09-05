---
components:
    - rc.AspectRatio
---

# Aspect Ratio

```python exec
import reflex_chakra as rc
import reflex as rx
```

Preserve the ratio of the components contained within a region.

```python demo
rc.box(element="iframe", src="https://bit.ly/naruto-sage", border_color="red")
```

```python demo
rc.aspect_ratio(
    rc.box(
        element="iframe",
        src="https://bit.ly/naruto-sage",
        border_color="red"
    ),
    ratio=4/3
)
```
