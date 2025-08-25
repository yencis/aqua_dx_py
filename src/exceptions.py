from requests.exceptions import HTTPError


class NotFoundError(HTTPError):
    """Not found error"""
