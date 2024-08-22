---
components:
    - rc.Text
---

```python exec
import reflex_chakra as rc
import reflex as rx
```

# Text

The text component displays a paragraph of text.

```python demo
rc.text("Hello World!", font_size="2em")
```

The text element can be visually modified using the `as_` prop.

```python demo
rc.vstack(
    rc.text("Hello World!", as_="i"),
    rc.text("Hello World!", as_="s"),
    rc.text("Hello World!", as_="mark"),
    rc.text("Hello World!", as_="sub"),
)
```
