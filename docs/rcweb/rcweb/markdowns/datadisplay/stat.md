---
components:
    - rc.Stat
    - rc.StatLabel
    - rc.StatNumber
    - rc.StatHelpText
    - rc.StatArrow
    - rc.StatGroup
---

```python exec
import reflex_chakra as rc
import reflex as rx
```

# Stat

The stat component is a great way to visualize statistics in a clean and concise way.

```python demo
rc.stat(
    rc.stat_label("Example Price"),
    rc.stat_number("$25"),
    rc.stat_help_text("The price of the item."),
)
```

Example of a stats in a group with arrow.

```python demo
rc.stat_group(
        rc.stat(
            rc.stat_number("$250"),
            rc.stat_help_text("%50", rc.stat_arrow(type_="increase")),
        ),
        rc.stat(
            rc.stat_number("£100"),
            rc.stat_help_text("%50", rc.stat_arrow(type_="decrease")),
        ),
        width="100%",
)
```
