import pytest
import requests

from utils.api_client import ApiClient


@pytest.mark.api
def test_api_health(api_client: ApiClient, logger):
    """
    Simple health check to verify that the API is up and responding.
    """
    logger.info("Starting API health check")

    try:
        response = api_client.get("posts/1", timeout=5)
    except requests.exceptions.RequestException as exc:
        pytest.fail(f"API is not reachable: {exc}")

    logger.info(
        f"Health check status: {response.status_code}, body length: {len(response.text)}"
    )

    # Basic availability check
    assert 200 <= response.status_code < 300, "API should return a successful status code"

    # Optional minimal structure check
    body = response.json()
    assert "id" in body, "Response JSON should contain 'id' field"
