---
components:
    - rc.Tabs
    - rc.TabList
    - rc.Tab
    - rc.TabPanel
    - rc.TabPanels
---

```python exec
import reflex_chakra as rc
import reflex as rx
```

# Tabs

Tab components allow you display content in multiple pages within a container.
These page are organized by a tab list and the corresponding tab panel can take in children components if needed.

```python demo
rc.tabs(
    rc.tab_list(
        rc.tab("Tab 1"),
        rc.tab("Tab 2"),
        rc.tab("Tab 3"),
    ),
    rc.tab_panels(
        rc.tab_panel(rc.text("Text from tab 1.")),
        rc.tab_panel(rc.checkbox("Text from tab 2.")),
        rc.tab_panel(rc.button("Text from tab 3.", color="black")),
    ),
    bg="black",
    color="white",
    shadow="lg",
)
```

You can create a tab component using the shorthand syntax.
Pass a list of tuples to the `items` prop.
Each tuple should contain a label and a panel.

```python demo
rc.tabs(
    items = [("Tab 1", rc.text("Text from tab 1.")), ("Tab 2", rc.checkbox("Text from tab 2.")), ("Tab 3", rc.button("Text from tab 3.", color="black"))],
    bg="black",
    color="white",
    shadow="lg",
)
```
