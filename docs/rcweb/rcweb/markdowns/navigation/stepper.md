---
components:
    - rc.Stepper
    - rc.Step
    - rc.StepDescription
    - rc.StepIcon
    - rc.StepIndicator
    - rc.StepNumber
    - rc.StepSeparator
    - rc.StepStatus
    - rc.StepTitle
---

```python exec
import reflex_chakra as rc
import reflex as rx
```

# Stepper

A `stepper` can be used to guide users through a sequence of steps, making complex processes more manageable by breaking them into distinct stages.

```python demo
rc.stepper(
    rc.step(
        rc.step_indicator(
	
           rc.step_status(incomplete="1",active="1"),
        ),
        rc.box(
            rc.step_title("First"),
            rc.step_description("Contact Info")
        ),
        rc.step_separator(),
    ),
    rc.step(
        rc.step_indicator(
           rc.step_status(incomplete="2",active="2"),
        ),
        rc.box(
            rc.step_title("Second"),
            rc.step_description("Date & Time")
        ),
        rc.step_separator()
    ),
    rc.step(
        rc.step_indicator(
          rc.step_status(incomplete="3",active="3"),
        ),
        rc.box(
            rc.step_title("Third"),
            rc.step_description("Select Rooms")
        ),
    ),
    size='lg',
    colorScheme='purple',
    index=1,
    orientation="horizontal",
    width="700px",
    gap='10px',
)
```

Below is an example on how `on_click` event handler can be used to set an `step_status` to `active`.

```python demo
class ProgressBar(rx.State):
    index: int =1

    def setactive(self,value :int):
        self.index=value

def example():
    return rc.stepper(
        rc.step(
            rc.step_indicator(
               rc.step_status(complete="✅",active="1",incomplete="1"),
            ),
            rc.box(
                rc.step_title("First"),
                rc.step_description("Contact Info")
            ),
            rc.step_separator(),
            on_click=ProgressBar.setactive(1)
        ),
        rc.step(
            rc.step_indicator(
               rc.step_status(complete="✅",active="2",incomplete="2"),
            ),
            rc.box(
                rc.step_title("Second"),
                rc.step_description("Date & Time")
            ),
            rc.step_separator(),
            on_click=ProgressBar.setactive(2)
        ),
        rc.step(
            rc.step_indicator(
              rc.step_status(complete="✅",active="3",incomplete="3"),
            ),
            rc.box(
                rc.step_title("Third"),
                rc.step_description("Select Rooms")
            ),
            rc.step_separator(),
            on_click=ProgressBar.setactive(3)
        ),
        size='lg',
        colorScheme='gray',
        index=ProgressBar.index,
        orientation="horizontal",
        width="700px",
    )
```

