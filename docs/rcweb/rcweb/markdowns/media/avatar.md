---
components:
    - rc.Avatar
    - rc.AvatarBadge
    - rc.AvatarGroup
---

```python exec
import reflex_chakra as rc
import reflex as rx
```

# Avatar

The Avatar component is used to represent a user, and displays the profile picture, initials or fallback icon.

```python demo
rc.hstack(
    rc.avatar(size="sm"),
    rc.avatar(name="Barack Obama", size="md"),
    rc.avatar(name="Donald Trump", size="lg"),
    rc.avatar(name="Joe Biden", size="xl"),
)
```

Avatar components can be grouped into avatar groups for easier display.

```python demo
rc.avatar_group(
    rc.avatar(name="Barack Obama"),
    rc.avatar(name="Donald Trump"),
    rc.avatar(name="Joe Biden"),
)
```

Badges can also be applied to show elements about the avatar such as activity.

```python demo
rc.avatar_group(
    rc.avatar(
        rc.avatar_badge(
            box_size="1.25em", bg="green.500", border_color="green.500"
        ),
        name="Barack Obama",
    ),
    rc.avatar(
        rc.avatar_badge(
            box_size="1.25em", bg="yellow.500", border_color="red.500"
        ),
        name="Donald Trump",
    ),
)
```

If there are too many avatar to display a limit can be set using the `max_` prop.

```python demo
rc.avatar_group(
    *([rc.avatar(name="Barack Obama")] * 5),
    size="md",
    max_=3,
)
```
