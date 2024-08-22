---
components:
    - rc.List
    - rc.ListItem
    - rc.UnorderedList
    - rc.OrderedList
---

```python exec
import reflex_chakra as rc
import reflex as rx
```

# List

There are three types of lists: regular lists, ordered, unordered.

The shorthand syntax used to create a list is by passing in a list of items.
These items can be components or Python primitives.

```python demo
rc.list(
    items=["Example 1", "Example 2", "Example 3"],
    spacing=".25em"
)
```

The examples below have the explicit syntax of list and list_items.
Regular lists are used to display a list of items.
They have no bullet points or numbers and stack the list items vertically.

```python demo
rc.list(
    rc.list_item("Example 1"),
    rc.list_item("Example 2"),
    rc.list_item("Example 3"),
)
```

Unordered have bullet points to display the list items.

```python demo
rc.unordered_list(
    rc.list_item("Example 1"),
    rc.list_item("Example 2"),
    rc.list_item("Example 3"),
)
```

Ordered lists have numbers to display the list items.

```python demo
rc.ordered_list(
    rc.list_item("Example 1"),
    rc.list_item("Example 2"),
    rc.list_item("Example 3"),
)
```

Lists can also be used with icons.

```python demo
rc.list(
    rc.list_item(rc.icon(tag="check_circle", color = "green"), "Allowed"),
    rc.list_item(rc.icon(tag="not_allowed", color = "red"), "Not"),
    rc.list_item(rc.icon(tag="settings", color = "grey"), "Settings"),
    spacing = ".25em"
)
```
