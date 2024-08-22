---
components:
    - rc.PinInput
---

```python exec
import reflex_chakra as rc
import reflex as rx
```

# PinInput

The PinInput component is similar to the Input component, but it is optimized for entering sequences of digits

```python demo exec
class PinInputState(rx.State):
    pin: str


def basic_pininput_example():
    return rc.vstack(
        rc.heading(PinInputState.pin),
        rc.box(
            rc.pin_input(
                length=4,
                on_change=PinInputState.set_pin,
                mask=True,
            ),
        ),
    )
```

The PinInput component can also be customized as seen below.

```python demo
rc.center(
    rc.pin_input(
        rc.pin_input_field(color="red"),
        rc.pin_input_field(border_color="green"),
        rc.pin_input_field(shadow="md"),
        rc.pin_input_field(color="blue"),
        rc.pin_input_field(border_radius="md"),
        on_change=PinInputState.set_pin,
    )
)
```
