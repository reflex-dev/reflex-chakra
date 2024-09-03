import reflex as rx
import reflex_chakra as rc


class User(rx.Model, table=True):
    email: str
    password: str


class Contact(rx.Model, table=True):
    user_email: str
    contact_name: str
    email: str
    stage: str = "lead"
