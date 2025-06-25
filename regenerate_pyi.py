"""Generate .pyi files for type hinting in Reflex Chakra components."""

from reflex.utils.pyi_generator import PyiGenerator

PyiGenerator().scan_all(["reflex_chakra"])
