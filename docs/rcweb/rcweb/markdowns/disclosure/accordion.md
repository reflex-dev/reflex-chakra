---
components:
    - rc.Accordion
    - rc.AccordionItem
    - rc.AccordionButton
    - rc.AccordionPanel
    - rc.AccordionIcon
---

```python exec
import reflex_chakra as rc
import reflex as rx
```

# Accordion

Accordions allow you to hide and show content in a container under a header.

Accordion consist of an outer accordion component and inner accordion items.
Each item has a optional button and panel. The button is used to toggle the panel's visibility.

```python demo
rc.accordion(
    rc.accordion_item(
        rc.accordion_button(
            rc.heading("Example"),
            rc.accordion_icon(),
        ),
        rc.accordion_panel(
            rc.text("This is an example of an accordion component.")
        )
    ),
    allow_toggle = True,
    width = "100%"
)
```

An accordion can have multiple items.

```python demo
rc.accordion(
    rc.accordion_item(
        rc.accordion_button(
            rc.heading("Example 1"),
            rc.accordion_icon(),
        ),
        rc.accordion_panel(
            rc.text("This is an example of an accordion component.")
        ),
    ),
    rc.accordion_item(
        rc.accordion_button(
            rc.heading("Example 2"),
            rc.accordion_icon(),
        ),
        rc.accordion_panel(
            rc.text("This is an example of an accordion component.")
        ),
    ),
    allow_multiple = True,
    bg="black",
    color="white",
    width = "100%"
)
```

You can create multilevel accordions by nesting accordions within the outer accordion panel.

```python demo
rc.accordion(
    rc.accordion_item(
        rc.accordion_button(
            rc.accordion_icon(),
            rc.heading("Outer"),
            
        ),
        rc.accordion_panel(
            rc.accordion(
            rc.accordion_item(
                rc.accordion_button(
                    rc.accordion_icon(),
                    rc.heading("Inner"),    
                ),
                rc.accordion_panel(
                    rc.badge("Inner Panel", variant="solid", color_scheme="green"),
                )
            )
            ),
        )  
    ),
    width = "100%"
)
```

You can also create an accordion using the shorthand syntax.
Pass a list of tuples to the `items` prop.
Each tuple should contain a label and a panel.

```python demo
rc.accordion(
   items=[("Label 1", rc.center("Panel 1")), ("Label 2", rc.center("Panel 2"))],
   width="100%"
)
```
