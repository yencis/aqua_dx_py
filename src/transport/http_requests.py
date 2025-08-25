import requests
from urllib.parse import urlencode
from ..exceptions import NotFoundError


class HTTPRequest:
    def __init__(self):
        self.session = requests.Session()

    def perform_request(self, method: str, url: str, params=None, body=None, timeout=None, headers=None):
        if params:
            url = f"{url}?{urlencode(params)}"
        request = requests.Request(method=method, headers=headers, url=url, data=body)
        prepared = self.session.prepare_request(request)
        response = self.session.send(prepared)
        if not (200 <= response.status_code <= 300):
            # TODO: exception handling code
            if response.status_code == 404:
                raise NotFoundError
            else:
                response.raise_for_status()
        else:
            return response
