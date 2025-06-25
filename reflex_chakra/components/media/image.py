"""An image component."""

from __future__ import annotations

from typing import Any

from reflex.components.component import Component
from reflex.event import EventHandler, no_args_event_spec
from reflex.vars.base import Var

from reflex_chakra.components.base import ChakraComponent, LiteralImageLoading


class Image(ChakraComponent):
    """Display an image."""

    tag = "Image"
    alias = "ChakraImage"
    # How to align the image within its bounds. It maps to css `object-position` property.
    align: Var[str]

    # Fallback Reflex component to show if image is loading or image fails.
    fallback: Var[Component]

    # Fallback image src to show if image is loading or image fails.
    fallback_src: Var[str]

    # How the image to fit within its bounds. It maps to css `object-fit` property.
    fit: Var[str]

    # The native HTML height attribute to the passed to the img.
    html_height: Var[str]

    # The native HTML width attribute to the passed to the img.
    html_width: Var[str]

    # If true, opt out of the fallbackSrc logic and use as img.
    ignore_fallback: Var[bool]

    # "eager" | "lazy"
    loading: Var[LiteralImageLoading]

    # The path/url to the image or PIL image object.
    src: Var[Any]

    # The alt text of the image.
    alt: Var[str]

    # Provide multiple sources for an image, allowing the browser
    # to select the most appropriate source based on factors like
    # screen resolution and device capabilities.
    # Learn more _[here](https://developer.mozilla.org/en-US/docs/Learn/HTML/Multimedia_and_embedding/Responsive_images)_
    src_set: Var[str]

    # Fired when the image fails to load.
    on_error: EventHandler[no_args_event_spec]

    # Fired when the image is loaded.
    on_load: EventHandler[no_args_event_spec]
