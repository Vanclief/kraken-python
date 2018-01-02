import requests
import json


class Requester(object):

    def __init__(self, api_base):
        self.api_base = api_base

    def _construct_url(self, endpoint):
        """
        Construct the url
        """

        return self.api_base + endpoint

    def get(self, endpoint):
        """
        Make get http request, return status and response
        """

        url = self._construct_url(endpoint)

        r = requests.request("GET", url)
        status_code = r.status_code
        response = json.loads(r.text)

        return status_code, response

