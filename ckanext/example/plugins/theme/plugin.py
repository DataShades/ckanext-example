from __future__ import annotations


import ckan.plugins as p
import ckan.plugins.toolkit as tk


class ExampleTheme(p.SingletonPlugin):
    p.implements(p.IConfigurer)

    def update_config(self, config: tk.CKANConfig):
        tk.add_public_directory(config, "assets")
        tk.add_public_directory(config, "public")

        tk.add_resource("assets", "example_theme")
        tk.add_template_directory(config, "templates")
