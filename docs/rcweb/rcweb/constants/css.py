"""App styling."""

import reflex as rx

import reflex_chakra as rc

from . import fonts

font_weights = {
    "bold": "800",
    "heading": "700",
    "subheading": "600",
    "section": "600",
}


def get_code_style(color: str):
    return {
        "color": rx.color(color, 9),
        "border_radius": "4px",
        "border": f"1px solid {rx.color(color, 4)}",
        "background": rx.color(color, 3),
        **fonts.code,
        "line_height": "1.5",
    }


def get_code_style_rdx(color: str):
    return {
        "color": rx.color(color, 11),
        "border_radius": "4px",
        "border": f"1px solid {rx.color(color, 5)}",
        "background": rx.color(color, 3),
        **fonts.code,
        "line_height": "1.5",
    }


cell_style = {
    **fonts.small,
    "color": rx.color("slate", 11),
    "line_height": "1.5",
}


# General styles.
SANS = "Instrument Sans"
MONO = "IBM Plex Mono, Menlo, Consolas, DejaVu Sans Mono, monospace"
BOLD_WEIGHT = font_weights["bold"]
NAVBAR_LOGO = "/Reflex.svg"
LOGO_URL = "/Reflex_white.svg"
PADDING_X = ["1em", "1.5em", "1.5em", "1.5em", "3em"]
PADDING_X2 = ["1em", "2em", "10em"]
HERO_FONT_SIZE = ["2em", "3em", "3em", "4em"]
H1_FONT_SIZE = ["2.2em", "2.4em", "2.5em"]
H2_FONT_SIZE = "1.5em"
H3_FONT_SIZE = "1.35em"
H4_FONT_SIZE = "1.15em"

DOC_BORDER_RADIUS = "6px"

# The base application style.
BASE_STYLE = {
    "background_color": rx.color("mauve", 1),
    "::selection": {
        "background_color": rx.color("accent"),
    },
    "font_family": SANS,
    rc.text: {
        "font_family": SANS,
        "font_size": 16,
    },
    rx.heading: {
        "font_family": SANS,
    },
    rx.divider: {"margin_bottom": "1em", "margin_top": "0.5em"},
    rx.vstack: {"align_items": "center"},
    rx.hstack: {"align_items": "center"},
    rc.divider: {"margin_bottom": "1em", "margin_top": "0.5em"},
    rc.code: {"color": "#1F1944", "bg": "#EAE4FD"},
    rc.alert: {
        "border_radius": "8px",
    },
    rc.link: {"text_decoration": "none", "_hover": {}},
    rx.markdown: {
        "background": "transparent",
    },
}

# Fonts to include.
STYLESHEETS = [
    "https://fonts.googleapis.com/css2?family=Instrument+Sans:ital,wght@0,400;0,500;0,600;0,700;1,400;1,500;1,600;1,700&family=Space+Mono:ital,wght@0,400;0,700;1,400;1,700&family=IBM+Plex+Mono:ital,wght@0,500;0,600;1,600&family=Source+Code+Pro:wght@400;500&display=swap",
    # "custom-colors.css",
]

shadows = {
    "small": "0px 2px 4px 0px rgba(28, 32, 36, 0.05);",
    "medium": "0px 4px 8px 0px rgba(28, 32, 36, 0.04);",
    "large": "0px 24px 12px 0px rgba(28, 32, 36, 0.02), 0px 8px 8px 0px rgba(28, 32, 36, 0.02), 0px 2px 6px 0px rgba(28, 32, 36, 0.02);",
}
