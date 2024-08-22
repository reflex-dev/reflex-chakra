---
components:
    - rc.Skeleton
    - rc.SkeletonCircle
    - rc.SkeletonText
---

```python exec
import reflex_chakra as rc
import reflex as rx
```

# Skeleton

Skeleton is used to display the loading state of some components.

```python demo
rc.stack(
    rc.skeleton(height="10px", speed=1.5),
    rc.skeleton(height="15px", speed=1.5),
    rc.skeleton(height="20px", speed=1.5),
    width="50%",
)
```

Along with the basic skeleton box there are also a skeleton circle and text for ease of use.

```python demo
rc.stack(
    rc.skeleton_circle(size="30px"),
    rc.skeleton_text(no_of_lines=8),
    width="50%",
)
```

Another feature of skeleton is the ability to animate colors.
We provide the args start_color and end_color to animate the color of the skeleton component(s).

```python demo
rc.stack(
    rc.skeleton_text(
        no_of_lines=5, start_color="pink.500", end_color="orange.500"
    ),
    width="50%",
)
```

You can prevent the skeleton from loading by using the `is_loaded` prop.

```python demo
rc.vstack(
    rc.skeleton(rc.text("Text is already loaded."), is_loaded=True),
    rc.skeleton(rc.text("Text is already loaded."), is_loaded=False),
)
```
