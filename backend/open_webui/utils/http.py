import logging
from typing import Iterable

import requests
from requests.adapters import HTTPAdapter, Retry

log = logging.getLogger(__name__)


def http_request_with_retry(
    method: str,
    url: str,
    *,
    timeout: float | int = 10,
    retries: int = 3,
    backoff_factor: float = 0.5,
    status_forcelist: Iterable[int] = (500, 502, 503, 504),
    **kwargs,
) -> requests.Response:
    """Send an HTTP request with retry logic.

    Parameters
    ----------
    method: HTTP method such as "get" or "post".
    url: URL to request.
    timeout: Timeout in seconds for the request.
    retries: Number of retry attempts on failure.
    backoff_factor: Factor for calculating sleep time between retries.
    status_forcelist: HTTP status codes that trigger a retry.

    Returns
    -------
    requests.Response
        Response object from ``requests``.
    """

    session = requests.Session()
    retry = Retry(total=retries, backoff_factor=backoff_factor, status_forcelist=status_forcelist)
    adapter = HTTPAdapter(max_retries=retry)
    session.mount("http://", adapter)
    session.mount("https://", adapter)

    log.debug(f"HTTP {method.upper()} request to {url} with timeout={timeout}")
    response = session.request(method, url, timeout=timeout, **kwargs)
    return response
