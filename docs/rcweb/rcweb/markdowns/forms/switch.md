---
components:
    - rc.Switch
---

```python exec
import reflex_chakra as rc
import reflex as rx
```

# Switch

The Switch component is used as an alternative for the Checkbox component.
You can switch between enabled or disabled states.

```python demo exec
class SwitchState1(rx.State):
    checked: bool = False
    is_checked: bool = "Switch off!"

    def change_check(self, checked: bool):
        self.checked = checked
        if self.checked:
            self.is_checked = "Switch on!"
        else:
            self.is_checked = "Switch off!"


def switch_example():
    return rc.vstack(
        rc.heading(SwitchState1.is_checked),
        rc.switch(
            is_checked=SwitchState1.checked, on_change=SwitchState1.change_check
        ),
    )
```

You can also change the color scheme of the Switch component by passing the `color_scheme` argument.
The default color scheme is blue.

```python demo
rc.hstack(
    rc.switch(color_scheme="red"),
    rc.switch(color_scheme="green"),
    rc.switch(color_scheme="yellow"),
    rc.switch(color_scheme="blue"),
    rc.switch(color_scheme="purple"),
)
```
