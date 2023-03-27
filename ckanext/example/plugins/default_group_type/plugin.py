from __future__ import annotations
from collections.abc import Iterable
import os
from typing import Any, Optional

import ckan.plugins as p
import ckan.plugins.toolkit as tk
from ckan.lib.plugins import DefaultGroupForm, DefaultTranslation


class ExampleDefaultGroupTypeIndex(
    p.SingletonPlugin, DefaultGroupForm, DefaultTranslation
):
    p.implements(p.IGroupForm, inherit=True)
    p.implements(p.ITranslation)
    p.implements(p.ITemplateHelpers)

    def is_fallback(self) -> bool:
        return True

    def group_types(self) -> Iterable[str]:
        return ["category"]

    def get_helpers(self):
        return {
            "humanize_entity_type": humanize_entity_type,
        }

    def i18n_domain(self) -> str:
        return "ckanext-example"

    def i18n_directory(self) -> str:
        return os.path.join(os.path.dirname(__file__), "i18n")


@tk.chained_helper
def humanize_entity_type(
    next_: Any, entity_type: str, object_type: str, purpose: str
) -> Optional[str]:
    # "group_type" is an unexpected value, which will disappear once #7500 is
    # merged
    if entity_type not in ("group", "group_type") or object_type != "category":
        from icecream import ic

        if purpose == "main nav":
            ic(entity_type, object_type)

        return next_(entity_type, object_type, purpose)

    templates = {
        "add link": tk._("Add category"),
        "breadcrumb": tk._("Categories"),
        "content tab": tk._("Categories"),
        "create label": tk._("Create category"),
        "create title": tk._("Create category"),
        "delete confirmation": tk._(
            "Are you sure you want to delete this category?"
        ),
        "description placeholder": tk._(
            "A little information about my category..."
        ),
        "edit label": tk._("Edit category"),
        "facet label": tk._("Categories"),
        "form label": tk._("Category Form"),
        "main nav": tk._("Categories"),
        "my label": tk._("My categories"),
        "view label": tk._("View category"),
        "name placeholder": tk._("My category"),
        "no any objects": tk._(
            "There are currently no categories for this site"
        ),
        "no associated label": tk._(
            "There are no categories associated with this dataset"
        ),
        "no description": tk._("There is no description for this category"),
        "no label": tk._("No category"),
        "page title": tk._("Categories"),
        "save label": tk._("Save category"),
        "search placeholder": tk._("Search categories..."),
        "you not member": tk._("You are not a member of any categories."),
        "update label": tk._("Update category"),
    }

    return templates.get(purpose, "Category")
