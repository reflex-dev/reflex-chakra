import reflex as rx


class Customer(rx.Model, table=True):
    """The customer model."""

    customer_name: str
    email: str
    age: int
    gender: str
    location: str
    job: str
    salary: int
