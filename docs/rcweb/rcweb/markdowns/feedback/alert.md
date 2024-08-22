---
components:
    - rc.Alert
    - rc.AlertIcon
    - rc.AlertTitle
    - rc.AlertDescription
---

```python exec
import reflex_chakra as rc
import reflex as rx
```

# Alert

Alerts are used to communicate a state that affects a system, feature or page.
An example of the different alert statuses is shown below.

```python demo
rc.vstack(
    rc.alert(
        rc.alert_icon(),
        rc.alert_title("Error Reflex version is out of date."),
        status="error",
    ),
    rc.alert(
        rc.alert_icon(),
        rc.alert_title("Warning Reflex version is out of date."),
        status="warning",
    ),
    rc.alert(
        rc.alert_icon(),
        rc.alert_title("Reflex version is up to date."),
        status="success",
    ),
    rc.alert(
        rc.alert_icon(),
        rc.alert_title("Reflex version is 0.1.32."),
        status="info",
    ),
    width="100%",
)
```

Along with different status types, alerts can also have different style variants and an optional description.
By default the variant is 'subtle'.

```python demo
rc.vstack(
    rc.alert(
        rc.alert_icon(),
        rc.alert_title("Reflex version is up to date."),
        rc.alert_description("No need to update."),
        status="success",
        variant="subtle",
    ),
    rc.alert(
        rc.alert_icon(),
        rc.alert_title("Reflex version is up to date."),
        status="success",
        variant="solid",
    ),
    rc.alert(
        rc.alert_icon(),
        rc.alert_title("Reflex version is up to date."),
        status="success",
        variant="top-accent",
    ),
    width="100%",
)
```
