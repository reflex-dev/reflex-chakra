---
components:
    - rc.Link
---

```python exec
import reflex_chakra as rc
import reflex as rx
```

# Link

Links are accessible elements used primarily for navigation.

```python demo
rc.link("Example", href="https://reflex.dev/", color="rgb(107,99,246)")
```

You can also provide local links to other pages in your project without writing the full url.

```python demo
rc.link("Example", href="/docs/library", color="rgb(107,99,246)")
```

The link component can be used to wrap other components to make them link to other pages.

```python demo
rc.link(rc.button("Example"), href="https://reflex.dev/", color="rgb(107,99,246)", button=True)
```

You can also create anchors to link to specific parts of a page using the id prop.

```python demo
rc.box("Example", id="example")
```

To reference an anchor, you can use the href prop of the link component.
The `href` should be in the format of the page you want to link to followed by a `#` and the `id` of the anchor.

```python demo
rc.link("Example", href="/docs/library/navigation/link#example", color="rgb(107,99,246)")
```
