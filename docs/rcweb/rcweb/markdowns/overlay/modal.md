---
components:
    - rc.Modal
    - rc.ModalOverlay
    - rc.ModalContent
    - rc.ModalHeader
    - rc.ModalBody
    - rc.ModalFooter
---

```python exec
import reflex_chakra as rc
import reflex as rx
```

# Modal

A modal dialog is a window overlaid on either the primary window or another dialog window.
Content behind a modal dialog is inert, meaning that users cannot interact with it.

```python demo exec
class ModalState(rx.State):
    show: bool = False

    def change(self):
        self.show = not (self.show)


def modal_example():
    return rc.vstack(
    rc.button("Confirm", on_click=ModalState.change),
    rc.modal(
        rc.modal_overlay(
            rc.modal_content(
                rc.modal_header("Confirm"),
                rc.modal_body("Do you want to confirm example?"),
                rc.modal_footer(rc.button("Close", on_click=ModalState.change)),
            )
        ),
        is_open=ModalState.show,
    ),
)
```
