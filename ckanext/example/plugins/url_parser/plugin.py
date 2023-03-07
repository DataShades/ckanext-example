import re
from flask import Blueprint

import ckan.plugins as p
import ckan.plugins.toolkit as tk

# name of the config option that holds all possible patterns
CONFIG_PATTERNS = "ckanext.example_url_parser.patterns"
# default patterns if config option is missing
DEFAULT_PATTERNS = ["dataset=(?P<name>\w+)"]

# Blueprint that contains all views provided by the extension
bp = Blueprint("example_url_parser", __name__)

# Plugin that registers blueprint
class ExampleUrlParser(p.SingletonPlugin):
    p.implements(p.IBlueprint)

    def get_blueprint(self):
        return [bp]



# View that does the trick
@bp.route("/example_url_parser/parse/url")
def view():
    """Get a `url` parameter from query string and extract dataset id from it.

    Returns 404 if dataset ID not found
    Redirects to the dataset page otherwise
    """
    # get the `url` from query string
    url = tk.request.args.get("url")

    # show 404 if `url` isn't provided
    if not url:
        return tk.abort(404)

    # fetch all patterns from the config file(or get the default ones)
    patterns = tk.aslist(
        tk.config.get(CONFIG_PATTERNS, DEFAULT_PATTERNS)
    )

    # try to extract ID from the url using each pattern
    for pattern in patterns:

        match = re.search(pattern, url)
        if not match:
            # if ID not found, go to the next pattern
            continue

        # redirect to the dataset with the extracted ID
        return tk.redirect_to("dataset.read", id=match.group("name"))

    # none of the patterns matched. Show the 404 page.
    return tk.abort(404)
