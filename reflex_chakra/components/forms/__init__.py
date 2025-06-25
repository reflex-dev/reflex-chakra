"""Convenience functions to define core components."""

from reflex.components.el.elements.forms import Option

from .button import Button, ButtonGroup
from .checkbox import Checkbox, CheckboxGroup
from .colormodeswitch import (
    ColorModeButton,
    ColorModeScript,
    ColorModeSwitch,
)
from .date_picker import DatePicker
from .date_time_picker import DateTimePicker
from .editable import Editable, EditableInput, EditablePreview, EditableTextarea
from .email import Email
from .form import Form, FormControl, FormErrorMessage, FormHelperText, FormLabel
from .iconbutton import IconButton
from .input import (
    Input,
    InputGroup,
    InputLeftAddon,
    InputLeftElement,
    InputRightAddon,
    InputRightElement,
)
from .numberinput import (
    NumberDecrementStepper,
    NumberIncrementStepper,
    NumberInput,
    NumberInputField,
    NumberInputStepper,
)
from .password import Password
from .pininput import PinInput, PinInputField
from .radio import Radio, RadioGroup
from .rangeslider import (
    RangeSlider,
    RangeSliderFilledTrack,
    RangeSliderThumb,
    RangeSliderTrack,
)
from .select import Select
from .slider import Slider, SliderFilledTrack, SliderMark, SliderThumb, SliderTrack
from .switch import Switch
from .textarea import TextArea
from .time_picker import TimePicker

__all__ = [
    "Button",
    "ButtonGroup",
    "Checkbox",
    "CheckboxGroup",
    "ColorModeButton",
    "ColorModeScript",
    "ColorModeSwitch",
    "DatePicker",
    "DateTimePicker",
    "Editable",
    "EditableInput",
    "EditablePreview",
    "EditableTextarea",
    "Email",
    "Form",
    "FormControl",
    "FormErrorMessage",
    "FormHelperText",
    "FormLabel",
    "IconButton",
    "Input",
    "InputGroup",
    "InputLeftAddon",
    "InputLeftElement",
    "InputRightAddon",
    "InputRightElement",
    "NumberDecrementStepper",
    "NumberIncrementStepper",
    "NumberInput",
    "NumberInputField",
    "NumberInputStepper",
    "Option",
    "Password",
    "PinInput",
    "PinInputField",
    "Radio",
    "RadioGroup",
    "RangeSlider",
    "RangeSliderFilledTrack",
    "RangeSliderThumb",
    "RangeSliderTrack",
    "Select",
    "Slider",
    "SliderFilledTrack",
    "SliderMark",
    "SliderThumb",
    "SliderTrack",
    "Switch",
    "TextArea",
    "TimePicker",
]
