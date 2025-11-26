from pathlib import Path
from datetime import datetime
from selenium.webdriver.remote.webdriver import WebDriver


def save_screenshot(driver: WebDriver, test_name: str) -> Path:
    root_dir = Path(__file__).resolve().parents[2]
    screenshots_dir = root_dir / "screenshots"
    screenshots_dir.mkdir(parents=True, exist_ok=True)

    timestamp = datetime.now().strftime("%Y-%m-%d_%H-%M-%S")
    file_name = f"{test_name}_{timestamp}.png"
    file_path = screenshots_dir / file_name

    driver.save_screenshot(str(file_path))
    return file_path
