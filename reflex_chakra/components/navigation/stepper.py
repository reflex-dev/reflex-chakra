"""A component to indicate progress through a multi-step process."""

from typing import Literal

from reflex.components.component import Component
from reflex.vars.base import Var

from reflex_chakra.components import ChakraComponent, LiteralColorScheme


class Stepper(ChakraComponent):
    """The parent container for a stepper."""

    tag = "Stepper"

    # The orientation of Stepper: 'vertical' | 'horizontal'. Default: 'horizontal'
    orientation: Var[Literal["vertical", "horizontal"]]

    # The color scheme to use for the stepper; default is blue.
    colorScheme: Var[LiteralColorScheme]  # noqa: N815

    # Chakra provides a useSteps hook to control the stepper.
    # Instead, use an integer state value to set progress in the stepper.

    # The index of the current step.
    index: Var[int]

    # The size of the steps in the stepper.
    size: Var[str]

    @classmethod
    def create(cls, *children, items: list[tuple] | None = None, **props) -> Component:
        """Create a Stepper component.

        If the kw-args `items` is provided and is a list, they will be added as children.

        Args:
            *children: The children of the component.
            items (list): The child components for each step.
            **props: The properties of the component.

        Returns:
            The stepper component.
        """
        if len(children) == 0:
            children = []
            for indicator, layout, separator in items or []:
                children.append(
                    Step.create(
                        StepIndicator.create(indicator),
                        layout,
                        StepSeparator.create(separator),
                    )
                )
        return super().create(*children, **props)


class Step(ChakraComponent):
    """A component for an individual step in the stepper."""

    tag = "Step"


class StepDescription(ChakraComponent):
    """The description text for a step component."""

    tag = "StepDescription"


class StepIcon(ChakraComponent):
    """The icon displayed in a step indicator component."""

    tag = "StepIcon"


class StepIndicator(ChakraComponent):
    """The component displaying the status of a step."""

    tag = "StepIndicator"


class StepNumber(ChakraComponent):
    """The number of a step displayed in a step indicator component."""

    tag = "StepNumber"


class StepSeparator(ChakraComponent):
    """The component separting steps."""

    tag = "StepSeparator"


class StepStatus(ChakraComponent):
    """A component that displays a number or icon based on the status of a step."""

    tag = "StepStatus"

    # The CSS class name to apply when a step is the currently active step.
    active: Var[str]

    # The CSS class name to apply when a step is completed.
    complete: Var[str]

    # The CSS class name to apply when a step is incomplete.
    incomplete: Var[str]


class StepTitle(ChakraComponent):
    """The title text for a step component."""

    tag = "StepTitle"
