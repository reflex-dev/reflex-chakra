---
components:
    - rc.Image
---

```python exec
import reflex_chakra as rc
import reflex as rx
```

# Image

The Image component can display an image given a `src` path as an argument.
This could either be a local path from the assets folder or an external link.

```python demo
rc.image(src="/reflex_banner.png", width="100px", height="auto")
```

Image composes a box and can be styled simlarly.

```python demo
rc.image(
    src="/reflex_banner.png",
    width="100px",
    height="auto",
    border_radius="15px 50px",
    border="5px solid #555",
    box_shadow="lg",
)
```

You can also pass a `PIL` image object as the `src`.

```python demo box
rc.vstack(
    rc.image(src="https://picsum.photos/id/1/200/300", alt="An Unsplash Image")
)
```

```python
from PIL import Image
import requests


class ImageState(rx.State):
    url = f"https://picsum.photos/id/1/200/300"
    image = Image.open(requests.get(url, stream=True).raw)


def image_pil_example():
    return rc.vstack(
        rc.image(src=ImageState.image)
    )
```
