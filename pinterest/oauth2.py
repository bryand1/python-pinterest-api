import random
from typing import Dict, List

from urllib.parse import urlencode

from .util import do_request


def authorization_url(app_id: str, redirect_uri: str, scope: List[str] = None) -> str:
    """Generate Pinterest OAuth2 authorization url"""
    if scope is None:
        scope = ['read_public', 'write_public', 'read_relationships', 'write_relationships']
    params = {
        'response_type': 'code',
        'client_id': app_id,
        'redirect_uri': redirect_uri,
        'state': _random_state(),
        'scope': ','.join(scope),
    }
    return 'https://api.pinterest.com/oauth/?' + urlencode(params)


def _random_state(k: int = 8) -> str:
    """Produce a random string for use in the Pinterest OAuth2 authorization url"""
    population = 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789'
    return random.choices(population, k=k)


def access_token(app_id: str, app_secret: str, code: str) -> Dict:
    """Use code from callback querystring parameter to generate permanent access token

    Sample response:

        {
          "access_token": "AjYjREC3BKx...",
          "token_type": "bearer",
          "scope": ["read_public", "write_public", "read_private", "write_private",
                    "read_relationships", "write_relationships", "read_write_all"]
        }

    """
    params = {
        'grant_type': 'authorization_code',
        'client_id': app_id,
        'client_secret': app_secret,
        'code': code
    }
    url = 'https://api.pinterest.com/v1/oauth/token?' + urlencode(params)
    resp = do_request('post', url)
    return resp.json()
