from __future__ import annotations

from flask import Blueprint

import ckan.plugins as p
import ckan.plugins.toolkit as tk


class ExampleEndpoint(p.SingletonPlugin):
    p.implements(p.IConfigurer)
    p.implements(p.IBlueprint)

    def update_config(self, config: tk.CKANConfig):
        tk.add_template_directory(config, "templates")
        tk.add_resource("assets", "xxx")


    def get_blueprint(self):
        return [example_blueprint]


# first argument, example_ednpoint, is a name of our new blueprint
example_blueprint = Blueprint("example_endpoint", __name__)


@example_blueprint.route("/organization/<org_id>/new_tab") # URL of the new page
def new_tab(org_id): # name of the function is used inside the endpoint name
    # organization is required inside template
    organization = tk.get_action("organization_show")({}, {"id": org_id})

    # render the html template
    return tk.render("organization/new_tab.html", {
        "group_dict": organization,
        "group_type": organization["type"]
    })
