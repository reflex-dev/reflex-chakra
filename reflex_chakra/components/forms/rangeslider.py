"""A range slider component."""

from __future__ import annotations

from reflex.components.component import Component
from reflex.event import EventHandler
from reflex.utils import format
from reflex.vars.base import Var

from reflex_chakra.components import ChakraComponent, LiteralChakraDirection


class RangeSlider(ChakraComponent):
    """The RangeSlider is a multi thumb slider used to select a range of related values. A common use-case of this component is a price range picker that allows a user to set the minimum and maximum price."""

    tag = "RangeSlider"

    # State var to bind the input.
    value: Var[list[int]]

    # The default values.
    default_value: Var[list[int]]

    # The writing mode ("ltr" | "rtl")
    direction: Var[LiteralChakraDirection]

    # If false, the slider handle will not capture focus when value changes.
    focus_thumb_on_change: Var[bool]

    # If true, the slider will be disabled
    is_disabled: Var[bool]

    # If true, the slider will be in `read-only` state.
    is_read_only: Var[bool]

    # If true, the value will be incremented or decremented in reverse.
    is_reversed: Var[bool]

    # The minimum value of the slider.
    min_: Var[int]

    # The maximum value of the slider.
    max_: Var[int]

    # The minimum distance between slider thumbs. Useful for preventing the thumbs from being too close together.
    min_steps_between_thumbs: Var[int]

    # The name of the form field
    name: Var[str]

    # Fired when the value changes.
    on_change: EventHandler[lambda e0: [e0]]

    # Fired when the value starts changing.
    on_change_start: EventHandler[lambda e0: [e0]]

    # Fired when the value stops changing.
    on_change_end: EventHandler[lambda e0: [e0]]

    def get_ref(self):
        """Get the ref of the component.

        Returns:
            The ref of the component.
        """
        return

    def _get_ref_hook(self):
        """Override the base _get_ref_hook to handle array refs.

        Returns:
            The overrided hooks.
        """
        if self.id:
            ref = format.format_array_ref(self.id, None)
            if ref:
                return Var(
                    f"const {ref} = Array.from({{length:2}}, () => useRef(null)); "
                    f"{Var(_js_expr=ref)._as_ref()!s} = {ref}",
                )
            return super()._get_ref_hook()
        return None

    @classmethod
    def create(cls, *children, **props) -> Component:
        """Create a RangeSlider component.

        If no children are provided, a default RangeSlider will be created.

        Args:
            *children: The children of the component.
            **props: The properties of the component.

        Returns:
            The RangeSlider component.
        """
        if len(children) == 0:
            _id = props.get("id")
            if _id:
                children = [
                    RangeSliderTrack.create(
                        RangeSliderFilledTrack.create(),
                    ),
                    RangeSliderThumb.create(index=0, id=_id),
                    RangeSliderThumb.create(index=1, id=_id),
                ]
            else:
                children = [
                    RangeSliderTrack.create(
                        RangeSliderFilledTrack.create(),
                    ),
                    RangeSliderThumb.create(index=0),
                    RangeSliderThumb.create(index=1),
                ]
        return super().create(*children, **props)


class RangeSliderTrack(ChakraComponent):
    """A range slider track."""

    tag = "RangeSliderTrack"


class RangeSliderFilledTrack(ChakraComponent):
    """A filled range slider track."""

    tag = "RangeSliderFilledTrack"


class RangeSliderThumb(ChakraComponent):
    """A range slider thumb."""

    tag = "RangeSliderThumb"

    # The position of the thumb.
    index: Var[int]

    def _get_ref_hook(self) -> None:
        # hook is None because RangeSlider is handling it.
        return None

    def get_ref(self):
        """Get an array ref for the range slider thumb.

        Returns:
            The array ref.
        """
        if self.id:
            return format.format_array_ref(self.id, self.index)
        return None
