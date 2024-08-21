---
components:
    - rc.Table
    - rc.TableCaption
    - rc.Thead
    - rc.Tbody
    - rc.Tfoot
    - rc.Tr
    - rc.Th
    - rc.Td
    - rc.TableContainer
---

```python exec
import reflex_chakra as rc
import reflex as rx
```

# Table

Tables are used to organize and display data efficiently.
The table component differs from the `data_table`` component in that it is not meant to display large amounts of data.
It is meant to display data in a more organized way.

Tables can be created with a shorthand syntax or by explicitly creating the table components.
The shorthand syntax is great for simple tables, but if you need more control over the table you can use the explicit syntax.

Let's start with the shorthand syntax.
The shorthand syntax has `headers`, `rows`, and `footers` props.

```python demo
rc.table_container(
    rc.table(
        headers=["Name", "Age", "Location"],
        rows=[
            ("John", 30, "New York"),
            ("Jane", 31, "San Francisco"),
            ("Joe", 32, "Los Angeles")
        ],
        footers=["Footer 1", "Footer 2", "Footer 3"],
        variant='striped'
    )
)
```

Let's create a simple table explicitly. In this example we will make a table with 2 columns: `Name` and `Age`.

```python demo
rc.table(
    rc.thead(
        rc.tr(
            rc.th("Name"),
            rc.th("Age"),
        )
    ),
    rc.tbody(
        rc.tr(
            rc.td("John"),
            rc.td(30),
        )
    ),
)
```

In the examples we will be using this data to display in a table.

```python exec
columns = ["Name", "Age", "Location"]
data = [
    ["John", 30, "New York"],
    ["Jane", 25, "San Francisco"],
]
footer = ["Footer 1", "Footer 2", "Footer 3"]
```

```python
columns = ["Name", "Age", "Location"]
data = [
    ["John", 30, "New York"],
    ["Jane", 25, "San Francisco"],
]
footer = ["Footer 1", "Footer 2", "Footer 3"]
```

Now lets create a table with the data we created.

```python eval
rc.center(
    rc.table_container(
        rc.table(
            rc.table_caption("Example Table"),
            rc.thead(
                rc.tr(
                    *[rc.th(column) for column in columns]
                )
            ),
            rc.tbody(
                *[rc.tr(*[rc.td(item) for item in row]) for row in data]
            ),
            rc.tfoot(
                rc.tr(
                    *[rc.th(item) for item in footer]
                )
            ),
        )
    )
)
```

Tables can also be styled with the variant and color_scheme arguments.

```python demo
rc.table_container(
    rc.table(
        rc.thead(
        rc.tr(
            rc.th("Name"),
            rc.th("Age"),
            rc.th("Location"),
            )
        ),
        rc.tbody(
            rc.tr(
                rc.td("John"),
                rc.td(30),
                rc.td("New York"),
            ),
            rc.tr(
                rc.td("Jane"), 
                rc.td(31),
                rc.td("San Francisco"),
            ),
            rc.tr(
                rc.td("Joe"),
                rc.td(32),
                rc.td("Los Angeles"),
            )
        ),
        variant='striped',
        color_scheme='teal'
    )
)
```
