# reflex-chakra
Use [reflex](https://reflex.dev/) with chakra-ui components.

## Installation 

```commandline
pip install reflex-chakra
```

## Usage
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
Visit the [docs](https://reflex.dev/docs/library/chakra/datadisplay/badge/) for more info of chakra-ui components.