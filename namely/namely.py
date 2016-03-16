# -*- coding: utf-8 -*-
"""
Namely API client.
~~~~~~~~~~~~~~~~~~
Documenttation: https://developers.namely.com/v1
"""
from .api_client import ApiRequest
from .profiles import Profiles


class Namely(object):

    def __init__(self, subdomain, api_key):
        self.subdomain = subdomain
        self.api_key = api_key
        self.request = ApiRequest(subdomain=subdomain, api_key=api_key)
        self.profiles = Profiles(request=self.request)
