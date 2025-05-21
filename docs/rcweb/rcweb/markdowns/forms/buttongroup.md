---
components:
    - rc.ButtonGroup
---

```python exec
import reflex_chakra as rc
import reflex as rx


basic_button_group = (
"""rc.button_group(
            rc.button('Option 1'),
            rc.button('Option 2'),
            rc.button('Option 3'),
        )
"""
)

button_group_attached = (
"""rc.button_group(
            rc.button('Option 1'),
            rc.button('Option 2'),
            rc.button('Option 3'),
            is_attached=True,
        )

"""  
)

button_group_variant = (
"""rc.button_group(
            rc.button('Option 1'),
            rc.button('Option 2'),
            rc.button('Option 3'),
            variant='ghost',
        )

"""  
)

button_group_sizes = (
"""rc.button_group(
            rc.button('Large Button', size='lg'),
            rc.button('Medium Button', size='md'),
            rc.button('Small Button', size='sm'),
        )

"""  
)

button_group_disable = (
"""rc.button_group(
            rc.button('Option 1'),
            rc.button('Option 2'),
            rc.button('Option 3'),
            is_disabled=True,
        )

"""  
)

button_group_spacing = (
"""rc.button_group(
            rc.button('Option 1'),
            rc.button('Option 2'),
            rc.button('Option 3'),
            spacing=8,
        )

"""  

)
```

# Button Group

The `rc.button_group` component allows you to create a group of buttons that are visually connected and styled together.
This is commonly used to group related actions or options in your application's user interface.

## Basic Usage

Here's an example of how to use the `rc.button_group` component to create a simple group of buttons:



In this example, a button group is created with three buttons. The buttons are visually connected, and there
is a default spacing of `2` pixels between them.

## Adjusting ButtonGroup Properties

You can customize the appearance and behavior of the `rc.button_group` component by adjusting
its properties. For instance, you can set `is_attached` prop to `True` to make the buttons
appear flushed together:


In this example, the `is_attached` property is set to `True`, resulting in the buttons having a seamless appearance.

## ButtonGroup Variants

Just like the `button` component, you can customize the visual style of your buttons using the `variant` prop.
This will apply to all buttons in the group.



In this example, the `variant` prop is set to `ghost`, applying the variant style to all buttons in the group.

## ButtonGroup Sizes

Similarly, you can adjust the size of buttons within a button group using the `size` prop.
This prop allows you to choose from different size options, affecting all buttons within the group.



In this example, the `size` prop is used to set the size of all buttons within the group, with options such as `"lg"` (large), `"md"` (medium), and `"sm"` (small).

## Disabling ButtonGroup

You can also disable all the buttons within a button group by setting the `is_disabled` prop to `True`:



In this case, all the buttons within the group will be disabled and unclickable.

## Customizing Spacing

The `spacing` prop allows you to control the gap between buttons within the group. Here's an example of setting a custom spacing of `8` pixels:



By setting `spacing` to `8`, the buttons will have a larger gap between them.

```markdown alert info
- You can nest other components or elements within the button group to create more complex layouts.
- Button groups are a useful way to visually organize related actions or options in your application, providing a consistent and cohesive user interface.
- Experiment with different combinations of props to achieve the desired styling and behavior for your button groups in Reflex-based applications.
```
