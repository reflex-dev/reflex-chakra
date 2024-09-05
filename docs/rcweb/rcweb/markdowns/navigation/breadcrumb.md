---
components:
    - rc.Breadcrumb
    - rc.BreadcrumbItem
    - rc.BreadcrumbLink
---

```python exec
import reflex_chakra as rc
import reflex as rx
```

# Breadcrumb

Breadcrumbs, or a breadcrumb navigation, can help enhance how users navigate to previous page levels of a website.

This is userful for websites with a lot of pages.

```python demo
rc.breadcrumb(
    rc.breadcrumb_item(rc.breadcrumb_link("Home", href="#")),
    rc.breadcrumb_item(rc.breadcrumb_link("Docs", href="#")),
    rc.breadcrumb_item(rc.breadcrumb_link("Breadcrumb", href="#")),
)
```

The separator prop can be used to change the default separator.

```python demo
rc.breadcrumb(
    rc.breadcrumb_item(rc.breadcrumb_link("Home", href="#")),
    rc.breadcrumb_item(rc.breadcrumb_link("Docs", href="#")),
    rc.breadcrumb_item(rc.breadcrumb_link("Breadcrumb", href="#")),
    separator=">",
    color="rgb(107,99,246)"
)
```
