---
components:
    - rc.Icon
---

```python exec
import reflex_chakra as rc
import reflex as rx
```

# Icon

The Icon component is used to display an icon from a library of icons.

```python demo
rc.icon(tag="calendar")
```

Use the tag prop to specify the icon to display.

```markdown alert success
Below is a list of all available icons.
```

```python eval
rc.box(
    rc.divider(),
    rc.responsive_grid(
        *[
            rc.vstack(
                rc.icon(tag=icon),
                rc.text(icon),
                bg="white",
                border="1px solid #EAEAEA",
                border_radius="0.5em",
                padding=".75em",
            )
            for icon in rc.media.icon.ICON_LIST
        ],
        columns=[2, 2, 3, 3, 4],
        spacing="1em",
    )
)
```
