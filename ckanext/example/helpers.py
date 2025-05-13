"""Template helpers of the example plugin.

All non-private functions defined here are registered inside `tk.h` collection.
"""

from __future__ import annotations

from ckan.plugins import toolkit as tk


def get_dcat_profile() -> str|None:
    return tk.config.get("ckanext.dcat.rdf.profiles")


def example_hello() -> str:
    """Greet the user.

    Returns:
        greeting with the plugin name.
    """
    return "Hello, example!"
