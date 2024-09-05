---
components:
    - rc.AlertDialog
    - rc.AlertDialogOverlay
    - rc.AlertDialogContent
    - rc.AlertDialogHeader
    - rc.AlertDialogBody
    - rc.AlertDialogFooter
---

```python exec
import reflex_chakra as rc
import reflex as rx
```

# AlertDialog

AlertDialog component is used to interrupt the user with a mandatory confirmation or event.
The component will appear in front of the page prompting the user to conplete an event.

```python demo exec
class AlertDialogState(rx.State):
    show: bool = False

    def change(self):
        self.show = not (self.show)


def alertdialog_example():
    return rc.vstack(
        rc.button("Show Alert Dialog", on_click=AlertDialogState.change),
        rc.alert_dialog(
            rc.alert_dialog_overlay(
                rc.alert_dialog_content(
                    rc.alert_dialog_header("Confirm"),
                    rc.alert_dialog_body("Do you want to confirm example?"),
                    rc.alert_dialog_footer(
                        rc.button("Close", on_click=AlertDialogState.change)
                    ),
                )
            ),
            is_open=AlertDialogState.show,
        ),
        width="100%",
    )
```
