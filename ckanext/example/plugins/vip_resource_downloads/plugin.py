from __future__ import annotations
from typing import Optional, Union

import ckan.plugins as p
import ckan.plugins.toolkit as tk

from ckanext.vip_portal.interfaces import IVipPortal, Access


class ExampleVipResourceDownloads(p.SingletonPlugin):
    p.implements(IVipPortal, inherit=True)

    def check_vip_access_for_endpoint(
        self,
        endpoint: Union[tuple[str, str], tuple[None, None]],
        user: Optional[str],
    ):
        blueprint, action = endpoint

        # a bit silly check. You probably want to check blueprint here as well
        if action == "download":
            # use `user` here for additional checks
            return Access.forbidden

        return Access.unknown
