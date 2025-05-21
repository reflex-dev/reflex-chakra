---
components:
    - rc.Form
---

```python exec
import reflex_chakra as rc
import reflex as rx
```

# Form

Forms are used to collect user input. The `rc.form` component is used to group inputs and submit them together.

The form component's children can be form controls such as `rc.input`, `rc.checkbox`, or `rc.switch`. The controls should have an `name` attribute that is used to identify the control in the form data. The `on_submit` event trigger submits the form data as a dictionary to the `handle_submit` event handler.

The form is submitted when the user clicks the submit button or presses enter on the form controls.

```python demo exec
class FormState(rx.State):
    form_data: dict = {}

    def handle_submit(self, form_data: dict):
        """Handle the form submit."""
        self.form_data = form_data


def form_example():
    return rc.vstack(
        rc.form(
            rc.vstack(
                rc.input(placeholder="First Name", name="first_name"),
                rc.input(placeholder="Last Name", name="last_name"),
                rc.hstack(
                    rc.checkbox("Checked", name="check"),
                    rc.switch("Switched", name="switch"),
                ),
                rc.button("Submit", type_="submit"),
            ),
            on_submit=FormState.handle_submit,
            reset_on_submit=True,
        ),
        rc.divider(),
        rc.heading("Results"),
        rc.text(FormState.form_data.to_string()),
    )
```

```markdown alert warning
# When using the form you must include a button or input with `type_='submit'`.
```

## Dynamic Forms

Forms can be dynamically created by iterating through state vars using `rx.foreach`.

This example allows the user to add new fields to the form prior to submit, and all
fields will be included in the form data passed to the `handle_submit` function.

```python demo exec
class DynamicFormState(rx.State):
    form_data: dict = {}
    form_fields: list[str] = ["first_name", "last_name", "email"]

    @rx.var(cache=True)
    def form_field_placeholders(self) -> list[str]:
        return [
            " ".join(w.capitalize() for w in field.split("_"))
            for field in self.form_fields
        ]

    def add_field(self, form_data: dict):
        new_field = form_data.get("new_field")
        if not new_field:
            return
        field_name = new_field.strip().lower().replace(" ", "_")
        self.form_fields.append(field_name)

    def handle_submit(self, form_data: dict):
        self.form_data = form_data


def dynamic_form():
    return rc.vstack(
        rc.form(
            rc.vstack(
                rx.foreach(
                    DynamicFormState.form_fields,
                    lambda field, idx: rc.input(
                        placeholder=DynamicFormState.form_field_placeholders[idx],
                        name=field,
                    ),
                ),
                rc.button("Submit", type_="submit"),
            ),
            on_submit=DynamicFormState.handle_submit,
            reset_on_submit=True,
        ),
        rc.form(
            rc.hstack(
                rc.input(placeholder="New Field", name="new_field"),
                rc.button("+", type_="submit"),
            ),
            on_submit=DynamicFormState.add_field,
            reset_on_submit=True,
        ),
        rc.divider(),
        rc.heading("Results"),
        rc.text(DynamicFormState.form_data.to_string()),
    )
```
