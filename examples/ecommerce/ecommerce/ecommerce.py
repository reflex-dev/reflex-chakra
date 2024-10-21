"""Welcome to Reflex! This file outlines the steps to create a basic app."""
from rxconfig import config

import reflex as rx
import reflex_chakra as rc
import json
from icecream import ic
from datetime import datetime
import pandas as pd


SEARCH_LABELS = {
    "input_name": "Name",
    "input_qty": "Quantity",
    "input_price": "Unit Price",
}

PAGE_WIDTH = "60vw"
FULL = "100%"

FILTERS_TAG = [
    "contains",
    "does not contains",
    "is empty",
    "is not empty",
]


class Product(rx.Base):
    name: str
    quantity: int
    price: float
    created_at: str

    def __init__(self, row):
        name = row.get("name") or row.get("input_name")
        qty = row.get("quantity") or int(row.get("input_qty"))
        price = row.get("price") or float(row.get("input_price"))
        super().__init__(
            name=name,
            quantity=qty,
            price=price,
            created_at=datetime.now().isoformat(),
        )

    def sum_value(self):
        return self.quantity * self.unit_price


class State(rx.State):
    """The app state."""

    input_name: str = ""
    input_qty: int = 0
    input_price: float = 0.0

    search_input: str = ""
    invalid_inputs: dict[str, bool] = {
        "input_name": False,
        "input_qty": False,
        "input_price": False,
    }

    products: list[Product] = []

    export_path: str = ""

    def load_products(self):
        with open("products.json") as product_file:
            data = json.load(product_file)
            self.products = [Product(row) for row in data]

    def dump_products(self):
        with open("product.json", mode="w") as product_file:
            ic("fake serialization")

    @rx.var
    def product_data(self) -> list[list]:
        return [
            [p.name, p.quantity, f"${p.price}", p.created_at]
            for p in self.products
            if self.search_input.lower() in p.name.lower()
        ]

    def add_product(self, form_data: dict):
        ic("add new product", form_data)
        invalid = False
        for field in form_data.keys():
            ic(
                field,
            )
            if not form_data.get(field):
                self.invalid_inputs[field] = True
                invalid = True
            else:
                try:
                    type(getattr(self, field))(form_data.get(field))
                    self.invalid_inputs[field] = False
                except:
                    self.invalid_inputs[field] = True
                    invalid = True

        if not invalid:
            self.products.append(Product(form_data))
            for field in form_data.keys():
                yield rx.set_value(field, "")

    def export(self):
        df = pd.DataFrame(self.product_data)
        self.export_path = rx.get_asset_path("data.csv")
        df.to_csv(rx.get_asset_path("data.csv"))
        yield rx.download("")


def inventory():
    search_bar = rc.hstack(
        rc.icon(tag="info_outline"),
        rc.heading("Products", size="md"),
        rc.spacer(),
        rc.icon(tag="search"),
        rc.input(
            placeholder="Search by name", width="20%", on_change=State.set_search_input
        ),
        width=FULL,
    )
    table = rx.data_table(
        columns=["Name", "Quantity", "Price", "Created date"],
        data=State.product_data,
        pagination=True,
        sort=True,
        # search=True,
    )
    return rc.vstack(search_bar, table)


def field_input(var, placeholder):
    return rc.hstack(
        rc.spacer(),
        rc.text(SEARCH_LABELS[var._var_name]),
        rc.form_control(
            rc.input(
                id=var._var_name,
                placeholder=placeholder,
                is_invalid=State.invalid_inputs[var._var_name],
            ),
            width="50%",
            is_required=True,
        ),
        width=FULL,
    )


def filters():
    ...
    return rx.fragment()


def add_item():
    return rc.vstack(
        rc.hstack(
            rc.icon(tag="add"),
            rc.heading("Add a New Product", size="md"),
            rc.spacer(),
            width=FULL,
        ),
        rc.form(
            rc.box(
                rc.vstack(
                    field_input(State.input_name, "Product Name"),
                    field_input(State.input_qty, "Product Quantity"),
                    field_input(State.input_price, "Product price (in cents)"),
                    align="right",
                ),
                padding="15px",
                border="black solid 1px",
            ),
            rc.hstack(rc.spacer(), rc.button("Add Product", type_="submit")),
            on_submit=State.add_product,
            width=FULL,
        ),
        width=FULL,
    )


def index() -> rx.Component:
    return rc.center(
        rc.vstack(
            rc.heading("E-Commerce Inventory"),
            inventory(),
            add_item(),
            rc.spacer(),
            width=PAGE_WIDTH,
            height="70%",
        ),
        height="100vh",
    )


app = rx.App()
app.add_page(index, on_load=State.load_products)
