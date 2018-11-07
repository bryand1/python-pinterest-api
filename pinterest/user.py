from typing import Dict, List

from . import config
from .util import pinterest_request


class User:

    def __init__(self, token, username):
        self.token = token
        self.username = username

    def fetch(self, fields: List[str] = None) -> Dict:
        """
        Return a user's information

        fields: account_type, bio, counts, created_at,
                first_name, id, image, last_name, url, username

        GET/v1/users/<user>/
        """
        if fields is None:
            fields = ['first_name', 'id', 'last_name', 'url']
        url = config.api_url + '/v1/users/{username}/'.format(username=self.username)
        params = {'access_token': self.token, 'fields': ','.join(fields)}
        return pinterest_request('get', url, params=params)
