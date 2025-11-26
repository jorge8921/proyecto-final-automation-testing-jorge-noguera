import json
from pathlib import Path
import pytest

from utils.api_client import ApiClient


def load_api_test_data() -> dict:
    """Load API test data from JSON file if it exists, otherwise use defaults."""
    root_dir = Path(__file__).resolve().parents[3]
    data_path = root_dir / "data" / "api_test_data.json"

    if data_path.exists():
        with open(data_path, "r", encoding="utf-8") as f:
            return json.load(f)

    # Fallback default data
    return {
        "existing_post_id": 1,
        "new_post": {
            "title": "foo",
            "body": "bar",
            "userId": 1
        },
        "post_to_delete_id": 1,
    }


api_data = load_api_test_data()


@pytest.mark.api
def test_get_single_post_success(api_client: ApiClient, logger):
    """
    API Test 1
    GET /posts/{id}
    - Verify status code 200
    - Verify basic JSON structure
    """
    post_id = api_data["existing_post_id"]
    logger.info(f"Starting test_get_single_post_success for post_id={post_id}")

    response = api_client.get(f"posts/{post_id}")
    logger.info(f"Response status: {response.status_code}, body: {response.text}")

    assert response.status_code == 200, "Expected status code 200 for existing post"

    body = response.json()
    assert body.get("id") == post_id, "Returned post id should match requested id"
    assert "title" in body, "Response should contain 'title' field"
    assert "body" in body, "Response should contain 'body' field"


@pytest.mark.api
def test_create_post_success(api_client: ApiClient, logger):
    """
    API Test 2
    POST /posts
    - Verify status code 201
    - Verify returned fields (title, body, userId, id)
    """
    payload = api_data["new_post"]
    logger.info(f"Starting test_create_post_success with payload={payload}")

    response = api_client.post("posts", json_body=payload)
    logger.info(f"Response status: {response.status_code}, body: {response.text}")

    assert response.status_code == 201, "Expected status code 201 when creating a post"

    body = response.json()
    assert body.get("title") == payload["title"], "Response title should match request payload"
    assert body.get("body") == payload["body"], "Response body should match request payload"
    assert body.get("userId") == payload["userId"], "Response userId should match request payload"
    assert "id" in body, "Response should contain an 'id' field"


@pytest.mark.api
def test_delete_post_success(api_client: ApiClient, logger):
    """
    API Test 3
    DELETE /posts/{id}
    - Verify status code 200
    - Verify response body is an empty object {}
    """
    post_id = api_data["post_to_delete_id"]
    logger.info(f"Starting test_delete_post_success for post_id={post_id}")

    response = api_client.delete(f"posts/{post_id}")
    logger.info(f"Response status: {response.status_code}, body: {response.text}")

    assert response.status_code == 200, "Expected status code 200 when deleting a post"

    # JSONPlaceholder returns {} as body
    if response.text:
        body = response.json()
        assert body == {}, "Expected an empty JSON object as response body"
