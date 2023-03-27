from __future__ import annotations
from typing import Any

import ckan.plugins as p
import ckan.plugins.toolkit as tk

class ExampleSearchIndex(p.SingletonPlugin):
    p.implements(p.IPackageController, inherit=True)
    p.implements(p.IFacets, inherit=True)


    def dataset_facets(self, facets_dict, package_type):
        facets_dict['vocab_formats'] = tk._('Resource Formats')
        return facets_dict

    def before_index(self, pkg: dict[str, Any]):
        # compute formats somehow, for example:
        # >>> formats = [res["format"] for res in pkg["resources"]]
        pkg["vocab_formats"] = ["ASCII", "JPEG"]
        return pkg
