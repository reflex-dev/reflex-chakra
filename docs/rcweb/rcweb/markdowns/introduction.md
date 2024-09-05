## Welcome to reflex-chakra's documentation!

### Introduction

`reflex-chakra` is a third-party library for Reflex that integrates Chakra UI components, providing a rich set of UI elements to build modern, responsive web applications with ease. 
This library leverages the power of both Reflex and Chakra UI to offer a seamless development experience.

### Installation

To get started with `reflex-chakra`, you need to install the library using pip. Run the following command in your terminal:

```sh
pip install reflex-chakra
```

### Basic Usage
Once installed, you can start using reflex-chakra components in your Reflex applications.
Here’s a simple example to get you started:

```python
import reflex as rx
import reflex_chakra as rc

def index():
   return rx.fragment(
       rc.vstack(
           rc.heading("This is a header"),
           rc.center("This text is centered"),
           rc.button(
               "click me",
               on_click=rx.toast("show toast!"),
               bg="purple",
               border_radius="0.5em",
               pl="10px"
           )
       ),
       
   )

app = rx.App()
app.add_page(index)
```