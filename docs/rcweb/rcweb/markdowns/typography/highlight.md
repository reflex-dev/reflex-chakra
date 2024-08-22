---
components:
    - rc.Highlight
---

```python exec
import reflex_chakra as rc
import reflex as rx
```

# Highlight

The highlight component take in a string and display some of the words as highlighted text.

The words to highlight can be selected using the `query` prop.

You can also customize how the hightlight will be rendered with the `styles` prop.

```python demo
rc.highlight("Hello World, we have some highlight", query=['World','some'], styles={ 'px': '2', 'py': '1', 'rounded': 'full', 'bg': 'grey' })
```
