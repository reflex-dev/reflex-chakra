---
components:
    - rc.ResponsiveGrid
---

# Responsive Grid

```python exec
import reflex_chakra as rc
import reflex as rx
```

ResponsiveGrid provides a friendly interface to create responsive grid layouts with ease. SimpleGrid composes Box so you can pass all the Box props and css grid props with addition to the ones below.

Specify a fixed number of columns for the grid layout.

```python demo
rc.responsive_grid(
    rc.box(height="5em", width="5em", bg="lightgreen"),
    rc.box(height="5em", width="5em", bg="lightblue"),
    rc.box(height="5em", width="5em", bg="purple"),
    rc.box(height="5em", width="5em", bg="tomato"),
    rc.box(height="5em", width="5em", bg="orange"),
    rc.box(height="5em", width="5em", bg="yellow"),
    columns=[3],
    spacing="4",
)
```

```python demo
rc.responsive_grid(
    rc.box(height="5em", width="5em", bg="lightgreen"),
    rc.box(height="5em", width="5em", bg="lightblue"),
    rc.box(height="5em", width="5em", bg="purple"),
    rc.box(height="5em", width="5em", bg="tomato"),
    rc.box(height="5em", width="5em", bg="orange"),
    rc.box(height="5em", width="5em", bg="yellow"),
    columns=[1, 2, 3, 4, 5, 6],
)
```
