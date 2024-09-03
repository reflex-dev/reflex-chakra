from crm.state import State
from crm.state.models import Contact
import reflex as rx
import reflex_chakra as rc


class CRMState(State):
    contacts: list[Contact] = []
    query = ""

    def get_contacts(self) -> list[Contact]:
        with rx.session() as sess:
            if self.query != "":
                print("Query...")
                self.contacts = (
                    sess.query(Contact)
                    .filter(Contact.user_email == self.user.email)
                    .filter(Contact.contact_name.contains(self.query))
                    .all()
                )
                return
            print("All...")
            self.contacts = (
                sess.query(Contact).filter(Contact.user_email == self.user.email).all()
            )

    def filter(self, query):
        self.query = query
        print("Returning...")
        return self.get_contacts()

    @rx.var
    def num_contacts(self):
        return len(self.contacts)


class AddModalState(CRMState):
    show: bool = False
    name: str = ""
    email: str = ""

    def toggle(self):
        self.show = not self.show

    def add_contact(self):
        if not self.user:
            raise ValueError("No user logged in")
        with rx.session() as sess:
            sess.expire_on_commit = False
            sess.add(
                Contact(
                    user_email=self.user.email, contact_name=self.name, email=self.email
                )
            )
            sess.commit()
            self.toggle()
            return self.get_contacts()


def add_modal():
    return rc.modal(
        rc.modal_overlay(
            rc.modal_content(
                rc.modal_header("Add"),
                rc.modal_body(
                    rc.input(
                        on_change=AddModalState.set_name,
                        placeholder="Name",
                        margin_bottom="0.5rem",
                    ),
                    rc.input(on_change=AddModalState.set_email, placeholder="Email"),
                    padding_y=0,
                ),
                rc.modal_footer(
                    rc.button("Close", on_click=AddModalState.toggle),
                    rc.button(
                        "Add", on_click=AddModalState.add_contact, margin_left="0.5rem"
                    ),
                ),
            )
        ),
        is_open=AddModalState.show,
    )


def contact_row(
    contact,
):
    return rc.tr(
        rc.td(contact.contact_name),
        rc.td(contact.email),
        rc.td(rc.badge(contact.stage)),
    )


def crm():
    return rc.box(
        rc.button("Refresh", on_click=CRMState.get_contacts),
        rc.hstack(
            rc.heading("Contacts"),
            rc.button("Add", on_click=AddModalState.toggle),
            justify_content="space-between",
            align_items="flex-start",
            margin_bottom="1rem",
        ),
        rc.responsive_grid(
            rc.box(
                rc.stat(
                    rc.stat_label("Contacts"), rc.stat_number(CRMState.num_contacts)
                ),
                border="1px solid #eaeaef",
                padding="1rem",
                border_radius=8,
            ),
            columns=["5"],
            margin_bottom="1rem",
        ),
        add_modal(),
        rc.input(placeholder="Filter by name...", on_change=CRMState.filter),
        rc.table_container(
            rc.table(rc.tbody(rx.foreach(CRMState.contacts, contact_row))),
            margin_top="1rem",
        ),
        width="100%",
        max_width="960px",
        padding_x="0.5rem",
    )
