---
components:
    - rc.Menu
    - rc.MenuButton
    - rc.MenuList
    - rc.MenuItem
    - rc.MenuDivider
    - rc.MenuGroup
    - rc.MenuOptionGroup
    - rc.MenuItemOption
---

```python exec
import reflex_chakra as rc
import reflex as rx
```

# Menu

An accessible dropdown menu for the common dropdown menu button design pattern.

```python demo
rc.menu(
    rc.menu_button("Menu"),
    rc.menu_list(
        rc.menu_item("Example"),
        rc.menu_divider(),
        rc.menu_item("Example"),
        rc.menu_item("Example"),
    ),
)
```
