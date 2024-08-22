---
components:
    - rc.CircularProgress
    - rc.CircularProgressLabel
---

```python exec
import reflex_chakra as rc
import reflex as rx
```

# CircularProgress

The CircularProgress component is used to indicate the progress for determinate and indeterminate processes.
Determinate progress: fills the circular track with color, as the indicator moves from 0 to 360 degrees.
Indeterminate progress: grows and shrinks the indicator while moving along the circular track.

```python demo
rc.hstack(
    rc.circular_progress(value=0),
    rc.circular_progress(value=25),
    rc.circular_progress(rc.circular_progress_label(50), value=50),
    rc.circular_progress(value=75),
    rc.circular_progress(value=100),
    rc.circular_progress(is_indeterminate=True),
)
```
