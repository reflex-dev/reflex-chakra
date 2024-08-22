"""Welcome to Reflex! This file outlines the steps to create a basic app."""

import os
from pathlib import Path
from collections import defaultdict
from types import SimpleNamespace

import reflex as rx
import reflex_chakra as rc
import flexdown

from .utils.flexdown import xd
from .utils.docpage import multi_docs
from .constants import css


def should_skip_compile(doc: flexdown.Document):
    """Skip compilation if the markdown file has not been modified since the last compilation."""
    if not os.environ.get("REFLEX_PERSIST_WEB_DIR", False):
        return False

    # Check if the doc has been compiled already.
    compiled_output = f".web/pages/{doc.replace('.md', '.js')}"
    # Get the timestamp of the compiled file.
    compiled_time = (
        os.path.getmtime(compiled_output) if os.path.exists(compiled_output) else 0
    )
    # Get the timestamp of the source file.
    source_time = os.path.getmtime(doc)
    return compiled_time > source_time


def find_flexdown_files(directory: str) -> list[str]:
    """Recursively find all Flexdown (.md) files in the given directory.

    Args:
        directory: The root directory to search.

    Returns:
        A list of paths to Flexdown files.
    """
    return [
        os.path.join(root, file).replace("\\", "/")
        for root, _, files in os.walk(directory)
        for file in files
        if file.endswith(".md")
    ]


def extract_components_from_metadata(document) -> list:
    """Extract components from the document metadata.

    Args:
        document: The document object containing metadata.

    Returns:
        A list of tuples containing component instances and their string representation.
    """
    components = []
    for comp_str in document.metadata.get("components", []):
        component = eval(comp_str)
        if isinstance(component, type):
            components.append((component, comp_str))
        elif hasattr(component, "__self__"):
            components.append((component.__self__, comp_str))
        elif isinstance(component, SimpleNamespace) and hasattr(component, "__call__"):
            components.append((component.__call__.__self__, comp_str))
    return components


def execute_document_blocks(document, href):
    """Execute the exec and demo blocks in the document.

    Args:
        document: The document object containing blocks.
        href: The reference link for the document.
    """
    source, env = document.content, document.metadata.copy()
    env.update({"__xd": xd, "__exec": True})
    blocks = [
        block
        for block in xd.get_blocks(source, href)
        if block.__class__.__name__ in ["ExecBlock", "DemoBlock"]
    ]
    for block in blocks:
        block.render(env)


def convert_to_title_case(text: str) -> str:
    """Convert a snake_case string to Title Case.

    Args:
        text: The snake_case string.

    Returns:
        The string converted to Title Case.
    """
    return " ".join(word.capitalize() for word in text.split("_"))


def create_doc_component(
    doc_path: str, base_dir: str, component_registry: defaultdict
) -> rx.Component:
    """Create a document component for a given file path.

    Args:
        doc_path: The path to the document file.
        base_dir: The base directory containing the document.
        component_registry: A defaultdict to store categorized components.

    Returns:
        A component object representing the document page.
    """
    doc_path = doc_path.replace("\\", "/")
    route_path = rx.utils.format.to_kebab_case(
        f"/{doc_path.removeprefix(base_dir).replace('.md', '/')}"
    ).replace("//", "/")
    category = os.path.basename(os.path.dirname(doc_path)).title()
    document = flexdown.parse_file(doc_path)
    title = rx.utils.format.to_snake_case(os.path.basename(doc_path).replace(".md", ""))
    component_list = [title, *extract_components_from_metadata(document)]
    component_registry[category].append(component_list)
    return multi_docs(
        path=route_path,
        comp=document,
        component_list=component_list,
        title=f"Chakra {convert_to_title_case(title)}",
        chakra_components=component_registry,
    )


def generate_document_routes(doc_paths: list[str], base_dir: str) -> list[rx.Component]:
    """Generate document components and routes from Flexdown file paths.

    Args:
        doc_paths: List of document file paths.
        base_dir: The base directory containing the documents.

    Returns:
        A list of document components.
    """
    component_registry = defaultdict(list)
    return [
        create_doc_component(doc_path, base_dir, component_registry)
        for doc_path in doc_paths
    ]


def setup_application_routes(
    app: rx.App, doc_routes: list[rx.Component], base_path: str
):
    """Set up application routes based on document components.

    Args:
        app: The Reflex app instance.
        doc_routes: List of document components.
        base_path: The base path for routing.
    """
    for route in doc_routes:
        app.add_page(
            route.component,
            route.path.removeprefix(base_path),
            route.title,
            image="/previews/index_preview.png",
            meta=[{"name": "theme-color", "content": route.background_color}],
        )
    app.add_page(lambda: rx.fragment(), route="/", on_load=rx.redirect("/introduction"))


def main():
    """Main function to set up and run the Reflex application."""
    # Define paths
    base_directory = str(Path(__file__).parent / "markdowns")
    # Find all Flexdown documents
    flexdown_docs = find_flexdown_files(base_directory)

    # Generate document routes
    doc_routes = generate_document_routes(flexdown_docs, base_directory)

    # Execute blocks in documents (if any)
    for doc, href in []:  # Placeholder for outblocks
        execute_document_blocks(doc, href)

    # Set up application routes
    setup_application_routes(app, doc_routes, base_directory)


app = rx.App(
    style=css.BASE_STYLE,
    stylesheets=css.STYLESHEETS,
    theme=rx.theme(
        has_background=True,
        radius="large",
        accent_color="violet",
    ),
)

main()
