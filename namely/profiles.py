class Profiles(object):
    api_url = '{protocol}://{subdomain}.namely.com/api/v1/profiles.json'
    detail_url = '{protocol}://{subdomain}.namely.com/api/v1/profiles/{id}.json'

    def __init__(self, request):
        self.request = request

    def create(self, **kwargs):
        data = {'profiles': [kwargs.copy()]}
        r = self.request.post(self.api_url, data)
        return r.json(), r.status_code

    def list(self):
        r = self.request.get(self.api_url)
        return r.json(), r.status_code
