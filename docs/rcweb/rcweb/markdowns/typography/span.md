---
components:
    - rc.span
---

```python exec
import reflex_chakra as rc
import reflex as rx
```

# Span

The span component can be used to style inline text without creating a new line.

```python demo
rc.box(
    "Write some ",
    rc.span("stylized ", color="red"),    
    rc.span("text ", color="blue"),
    rc.span("using spans.", font_weight="bold")
)
```
