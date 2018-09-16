import requests
from requests.adapters import HTTPAdapter
from requests.packages.urllib3.util.retry import Retry

from .err import PinterestHttpException


def _requests_retry_session(
    retries=3,
    backoff_factor=0.3,
    status_forcelist=(500, 502, 504),
    session=None,
):
    session = session or requests.Session()
    retry = Retry(
        total=retries,
        read=retries,
        connect=retries,
        backoff_factor=backoff_factor,
        status_forcelist=status_forcelist,
    )
    adapter = HTTPAdapter(max_retries=retry)
    session.mount('http://', adapter)
    session.mount('https://', adapter)
    return session


# Initialize session to improve efficiency
_session = _requests_retry_session()


def do_request(req_type: str, url: str, *args, **kwargs) -> requests.Response:
    """
    Perform HTTP request

    req_type: Request method (e.g. get, post, patch, delete)

      >> do_request('post', 'https://api.pinterest.com/v1/pins/', data=data)
    """
    session = _session if _session else _requests_retry_session()
    resp = getattr(session, req_type)(url, *args, **kwargs)
    if resp.status_code // 100 != 2:
        raise PinterestHttpException(resp.status_code, url)
    return resp
