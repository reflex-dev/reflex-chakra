---
components:
    - rc.Box
---

# Box

```python exec
import reflex_chakra as rc
import reflex as rx
```

Box is a generic container component that can be used to group other components.

```python demo
rc.vstack(
    rc.box("Example", bg="yellow", border_radius="sm", width="20%"),
    rc.box("Example", bg="orange", border_radius="md", width="40%"),
    rc.box("Example", bg="red", border_radius="md", width="60%"),
    rc.box("Example", bg="lightblue", border_radius="lg", width="80%"),
    rc.box("Example", bg="lightgreen", border_radius="xl", width="100%"),
    width="100%",
)
```

Below is an example of how a box component can contain other components.

```python demo
rc.box(
    rc.button("Click Me"),
    bg="lightgreen",
    border_radius="15px",
    border_color="green",
    border_width="thick",
    padding=5,
)
```

Box can also compose videos and iframe elements.

```python demo
rc.box(
    element= "iframe",
    src="https://www.youtube.com/embed/9bZkp7q19f0",
    width = "100%",
)
```
