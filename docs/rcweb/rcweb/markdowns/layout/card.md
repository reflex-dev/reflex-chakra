---
components:
    - rc.Card
    - rc.CardHeader
    - rc.CardBody
    - rc.CardFooter
---

```python exec
import reflex_chakra as rc
import reflex as rx
```

# Card

Card is a flexible component used to group and display content in a clear and concise format.

```python demo
rc.card(
    rc.text("Body of the Card Component"), 
    header=rc.heading("Header", size="lg"), 
    footer=rc.heading("Footer",size="sm"),
)
```

You can pass a header with `header=` and/or a footer with `footer=`.
