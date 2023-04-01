# -*- coding: utf-8 -*-
# Always prefer setuptools over distutils
from setuptools import setup, find_packages
from codecs import open  # To use a consistent encoding
from os import path

here = path.abspath(path.dirname(__file__))

# Get the long description from the relevant file
with open(path.join(here, "README.md"), encoding="utf-8") as f:
    long_description = f.read()

setup(
    description="""""",
    long_description=long_description,
    long_description_content_type="text/markdown",
    # The project's main homepage.
    url="https://github.com/DataShades/ckanext-example",
    # Author details
    author="""Sergey Motornyuk""",
    author_email="""sergey.motornyuk@linkddigital.com.au""",
    # Choose your license
    license="AGPL",
    # See https://pypi.python.org/pypi?%3Aaction=list_classifiers
    classifiers=[
        # How mature is this project? Common values are
        # 3 - Alpha
        # 4 - Beta
        # 5 - Production/Stable
        "Development Status :: 4 - Beta",
        # Pick your license as you wish (should match "license" above)
        (
            "License :: OSI Approved :: GNU Affero General Public License v3"
            " or later (AGPLv3+)"
        ),
        # Specify the Python versions you support here. In particular, ensure
        # that you indicate whether you support Python 2, Python 3 or both.
        "Programming Language :: Python :: 2.7",
    ],
    # What does your project relate to?
    keywords="""CKAN""",
    # You can just specify the packages manually here if your project is
    # simple. Or you can use find_packages().
    packages=find_packages(exclude=["contrib", "docs", "tests*"]),
    namespace_packages=["ckanext"],
    install_requires=[
        # CKAN extensions should not list dependencies here, but in a separate
        # ``requirements.txt`` file.
        #
        # http://docs.ckan.org/en/latest/extensions/best-practices.html
        # add-third-party-libraries-to-requirements-txt
    ],
    # If there are data files included in your packages that need to be
    # installed, specify them here.  If using Python 2.6 or less, then these
    # have to be included in MANIFEST.in as well.
    include_package_data=True,
    package_data={},
    # Although 'package_data' is the preferred approach, in some case you may
    # need to place data files outside of your packages.
    # see http://docs.python.org/3.4/distutils/setupscript.html
    # installing-additional-files
    # In this case, 'data_file' will be installed into '<sys.prefix>/my_data'
    data_files=[],
    # To provide executable scripts, use entry points in preference to the
    # "scripts" keyword. Entry points provide cross-platform support and allow
    # pip to create the appropriate form of executable for the target platform.
    entry_points="""
        [ckan.plugins]
        example_vip_resource_downloads=ckanext.example.plugins.vip_resource_downloads.plugin:ExampleVipResourceDownloads
        example_theme=ckanext.example.plugins.theme.plugin:ExampleTheme
        example_url_parser=ckanext.example.plugins.url_parser.plugin:ExampleUrlParser
        example_search_index=ckanext.example.plugins.search_index.plugin:ExampleSearchIndex
        example_default_group_type=ckanext.example.plugins.default_group_type.plugin:ExampleDefaultGroupTypeIndex

        [babel.extractors]
        ckan = ckan.lib.extract:extract_ckan
    """,
    # If you are changing from the default layout of your extension, you may
    # have to change the message extractors, you can read more about babel
    # message extraction at
    # http://babel.pocoo.org/docs/messages/#extraction-method-mapping-and-configuration
    message_extractors={
        "ckanext": [
            ("**.py", "python", None),
            ("**.js", "javascript", None),
            ("**/templates/**.html", "ckan", None),
        ],
    },
)
