from typing import Dict, Tuple
import reflex as rx
from reflex.components.component import NoSSRComponent


def _on_error_signature(err: rx.Var[dict]) -> Tuple[rx.Var[str]]:
    return err.message,


class QrScanner(NoSSRComponent):
    library = "@yudiel/react-qr-scanner@^1.2.10"
    tag = "QrScanner"

    # The delay between scans in milliseconds.
    scan_delay: rx.Var[int]

    # The id of the element to disaply the video preview
    video_id: rx.Var[str]

    # Whether to display the scan count overlay on the video.
    hide_count: rx.Var[bool]

    container_style: rx.Var[Dict[str, str]]
    video_style: rx.Var[Dict[str, str]]

    on_result: rx.EventHandler[rx.event.passthrough_event_spec(dict)]
    on_decode: rx.EventHandler[rx.event.passthrough_event_spec(str)]
    on_error: rx.EventHandler[_on_error_signature]


qr_scanner = QrScanner.create
