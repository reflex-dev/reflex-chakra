---
components:
    - rc.Popover
    - rc.PopoverTrigger
    - rc.PopoverContent
    - rc.PopoverHeader
    - rc.PopoverBody
    - rc.PopoverFooter
    - rc.PopoverArrow
    - rc.PopoverAnchor
---

```python exec
import reflex_chakra as rc
import reflex as rx
```

# Popover

Popover is a non-modal dialog that floats around a trigger.
It is used to display contextual information to the user, and should be paired with a clickable trigger element.

```python demo
rc.popover(
    rc.popover_trigger(rc.button("Popover Example")),
    rc.popover_content(
        rc.popover_header("Confirm"),
        rc.popover_body("Do you want to confirm example?"),
        rc.popover_footer(rc.text("Footer text.")),
        rc.popover_close_button(),
    ),
)
```
