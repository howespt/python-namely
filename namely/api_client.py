import json
from requests import Request, Session

__all__ = ('ApiRequest', )


class ApiRequest(object):
    """API request class, this will create prepared reqeusts and have
    basic auth data prepared on the request.
    """
    protocol = 'https'

    def __init__(self, api_key, subdomain):
        self.session = Session()
        self.subdomain = subdomain
        self.api_key = api_key

    def _prepare_request(self, api_url, method='GET', data=None):
        url = api_url.format(protocol=self.protocol, subdomain=self.subdomain)
        request = Request(
            url=url, method=method,
            headers={'authorization': 'Bearer {}'.format(self.api_key),
                     'Content-type': 'application/json'},
            data=json.dumps(data))
        return self.session.prepare_request(request)

    def post(self, api_url, data, headers={}):
        prepared_request = self._prepare_request(
            api_url=api_url, method="POST", data=data)
        return self.session.send(prepared_request)

    def get(self, api_url):
        prepared_request = self._prepare_request(api_url=api_url)
        return self.session.send(prepared_request)
