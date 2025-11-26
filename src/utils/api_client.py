from pathlib import Path
import json
import requests


class ApiClient:
    def __init__(self) -> None:
        root_dir = Path(__file__).resolve().parents[2]
        config_path = root_dir / "config" / "config.json"
        with open(config_path, "r", encoding="utf-8") as f:
            config = json.load(f)

        self.base_url = config.get("api_base_url", "").rstrip("/")

    def get(self, path: str, **kwargs) -> requests.Response:
        url = f"{self.base_url}/{path.lstrip('/')}"
        return requests.get(url, **kwargs)

    def post(self, path: str, json_body: dict | None = None, **kwargs) -> requests.Response:
        url = f"{self.base_url}/{path.lstrip('/')}"
        return requests.post(url, json=json_body, **kwargs)

    def delete(self, path: str, **kwargs) -> requests.Response:
        url = f"{self.base_url}/{path.lstrip('/')}"
        return requests.delete(url, **kwargs)
