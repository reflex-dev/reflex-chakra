"""Components that are based on Chakra-UI."""

from __future__ import annotations

import shutil
from pathlib import Path
from typing import Literal

from reflex.components.component import Component, field
from reflex.utils.imports import ImportDict, ImportVar
from reflex.vars.base import Var

from reflex_chakra import constants


class ChakraComponent(Component):
    """A component that wraps a Chakra component."""

    library = "@chakra-ui/react@2.6.1"
    lib_dependencies: list[str] = field(
        default_factory=lambda: [
            "@chakra-ui/system@2.5.7",
            "framer-motion@10.16.4",
        ],
        is_javascript_property=False,
    )

    @staticmethod
    def _get_app_wrap_components() -> dict[tuple[int, str], Component]:
        return {
            (60, "ChakraProvider"): chakra_provider,
        }

    def _get_style(self) -> dict:
        """Get the style for the component.

        Returns:
            The dictionary of the component style as value and the style notation as key.
        """
        return {"sx": self.style}

    @classmethod
    def create(cls, *children, **props) -> Component:
        """Create a new Chakra component.

        Args:
            *children: The children of the component.
            **props: The properties of the component.

        Returns:
            A new Chakra component.
        """
        # copy color mode provider file to client's asset dir if it doesnt exist.
        client_asset_dir = Path.cwd() / constants.ASSETS_DIR_NAME
        if (
            not (
                client_color_mode_provider := (
                    Path.cwd()
                    / constants.ASSETS_DIR_NAME
                    / constants.COLOR_MODE_PROVIDER_FILENAME
                )
            ).exists()
            or client_color_mode_provider.read_bytes()
            != (
                constants.ASSETS_DIR / constants.COLOR_MODE_PROVIDER_FILENAME
            ).read_bytes()
        ):
            client_asset_dir.mkdir(exist_ok=True)
            shutil.copy(
                constants.ASSETS_DIR / constants.COLOR_MODE_PROVIDER_FILENAME,
                client_color_mode_provider.parent,
            )

        new_prop_names = [
            prop for prop in cls.get_props() if prop in ["type", "min", "max"]
        ]
        for prop in new_prop_names:
            under_prop = f"{prop}_"
            if under_prop in props:
                props[prop] = props.pop(under_prop)

        return super().create(*children, **props)


class ChakraProvider(ChakraComponent):
    """Top level Chakra provider must be included in any app using chakra components."""

    tag = "ChakraProvider"

    theme: Var[str]

    @classmethod
    def create(cls) -> Component:
        """Create a new ChakraProvider component.

        Returns:
            A new ChakraProvider component.
        """
        return super().create(
            theme=Var(_js_expr="extendTheme(theme)", _var_type=str),
        )

    def add_imports(self) -> ImportDict:
        """Add imports for the ChakraProvider component.

        Returns:
            The import dict for the component.
        """
        return {
            self.library or "": ImportVar(tag="extendTheme", is_default=False),
            "$/utils/theme": ImportVar(tag="theme", is_default=True),
        }

    @staticmethod
    def _get_app_wrap_components() -> dict[tuple[int, str], Component]:
        return {
            (50, "ChakraColorModeProvider"): chakra_color_mode_provider,
        }


chakra_provider = ChakraProvider.create()


class ChakraColorModeProvider(Component):
    """Next-themes integration for chakra colorModeProvider."""

    library = "$/public/chakra_color_mode_provider"
    tag = "ChakraColorModeProvider"
    is_default = True


chakra_color_mode_provider = ChakraColorModeProvider.create()


LiteralColorScheme = Literal[
    "none",
    "gray",
    "red",
    "orange",
    "yellow",
    "green",
    "teal",
    "blue",
    "cyan",
    "purple",
    "pink",
    "whiteAlpha",
    "blackAlpha",
    "linkedin",
    "facebook",
    "messenger",
    "whatsapp",
    "twitter",
    "telegram",
]


LiteralVariant = Literal["solid", "subtle", "outline"]
LiteralDividerVariant = Literal["solid", "dashed"]
LiteralTheme = Literal["light", "dark"]


LiteralTagColorScheme = Literal[
    "gray",
    "red",
    "orange",
    "yellow",
    "green",
    "teal",
    "blue",
    "cyan",
    "purple",
    "pink",
]
LiteralTagAlign = Literal["center", "end", "start"]
LiteralTabsVariant = Literal[
    "line",
    "enclosed",
    "enclosed-colored",
    "soft-rounded",
    "solid-rounded",
    "unstyled",
]

LiteralStatus = Literal["success", "info", "warning", "error"]
LiteralAlertVariant = Literal["subtle", "left-accent", "top-accent", "solid"]
LiteralButtonVariant = Literal["ghost", "outline", "solid", "link", "unstyled"]
LiteralSpinnerPlacement = Literal["start", "end"]
LiteralLanguage = Literal[
    "en",
    "da",
    "de",
    "es",
    "fr",
    "ja",
    "ko",
    "pt_br",
    "ru",
    "zh_cn",
    "ro",
    "pl",
    "ckb",
    "lv",
    "se",
    "ua",
    "he",
    "it",
]
LiteralInputVariant = Literal["outline", "filled", "flushed", "unstyled"]
LiteralInputNumberMode = Literal[
    "text",
    "search",
    "none",
    "tel",
    "url",
    "email",
    "numeric",
    "decimal",
]
LiteralChakraDirection = Literal["ltr", "rtl"]
LiteralCardVariant = Literal["outline", "filled", "elevated", "unstyled"]
LiteralStackDirection = Literal["row", "column"]
LiteralImageLoading = Literal["eager", "lazy"]
LiteralTagSize = Literal["sm", "md", "lg"]
LiteralSpinnerSize = Literal[LiteralTagSize, "xs", "xl"]
LiteralAvatarSize = Literal[LiteralTagSize, "xl", "xs", "2xl", "full", "2xs"]
LiteralButtonSize = Literal["sm", "md", "lg", "xs"]
# Applies to AlertDialog and Modal
LiteralAlertDialogSize = Literal[
    "sm", "md", "lg", "xs", "2xl", "full", "3xl", "4xl", "5xl", "6xl"
]
LiteralDrawerSize = Literal[LiteralSpinnerSize, "xl", "full"]

LiteralMenuStrategy = Literal["fixed", "absolute"]
LiteralMenuOption = Literal["checkbox", "radio"]
LiteralPopOverTrigger = Literal["click", "hover"]

LiteralHeadingSize = Literal["lg", "md", "sm", "xs", "xl", "2xl", "3xl", "4xl"]
