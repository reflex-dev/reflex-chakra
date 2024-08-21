---
components:
    - rc.RangeSlider
    - rc.RangeSliderTrack
    - rc.RangeSliderFilledTrack
    - rc.RangeSliderThumb
---

```python exec
import reflex_chakra as rc
import reflex as rx
```

# RangeSlider

The range slider is used to allow users to make selections from a range of values.

```python demo exec
from typing import List

class RangeSliderState(rx.State):
    value: List[int] = [0, 100]


def range_slider_example():
    return rc.vstack(
        rc.heading(f"{RangeSliderState.value[0]} : {RangeSliderState.value[1]}"),
        rc.range_slider(
            on_change_end=RangeSliderState.set_value
        ),
        width="100%",
    )
```

If you want to trigger state change on every slider movement, you can use the `on_change` event handler.
This is not recommended for performance reasons and should only be used if you need to perform an event on every slider movement.

```python demo
rc.vstack(
    rc.heading(f"{RangeSliderState.value[0]} : {RangeSliderState.value[1]}"),
    rc.range_slider(
        on_change=RangeSliderState.set_value
    ),
    width="100%",
)
```
