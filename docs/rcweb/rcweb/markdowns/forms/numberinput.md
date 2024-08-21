---
components:
    - rc.NumberInput
    - rc.NumberInputField
    - rc.NumberInputStepper
    - rc.NumberIncrementStepper
    - rc.NumberDecrementStepper
---

```python exec
import reflex_chakra as rc
import reflex as rx
```

# NumberInput

The NumberInput component is similar to the Input component, but it has controls for incrementing or decrementing numeric values.

```python demo exec
class NumberInputState(rx.State):
    number: int


def number_input_example():
    return rc.number_input(
        value=NumberInputState.number,
        on_change=NumberInputState.set_number,
    )
```
