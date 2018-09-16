import random
from typing import List

from urllib.parse import urlencode


def authorization_url(app_id: str, redirect_uri: str, scope: List[str] = None):
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
