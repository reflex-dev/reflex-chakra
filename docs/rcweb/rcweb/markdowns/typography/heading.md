---
components:
    - rc.Heading
---

```python exec
import reflex_chakra as rc
import reflex as rx
```

# Heading

The Heading component takes in a string and displays it as a heading.

```python demo
rc.heading("Hello World!")
```

The size can be changed using the `size` prop.

```python demo
rc.vstack(
    rc.heading("Hello World!", size= "sm", color="red"),
    rc.heading("Hello World!", size= "md", color="blue"),
    rc.heading("Hello World!", size= "lg", color="green"),
    rc.heading("Hello World!", size= "xl", color="blue"),
    rc.heading("Hello World!", size= "2xl", color="red"),
    rc.heading("Hello World!", size= "3xl", color="blue"),
    rc.heading("Hello World!", size= "4xl", color="green"),
)
```

It can also be styled using regular CSS styles.

```python demo
rc.heading("Hello World!", font_size="2em")
```
