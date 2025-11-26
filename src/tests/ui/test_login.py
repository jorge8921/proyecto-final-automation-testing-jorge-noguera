import json
from pathlib import Path
import pytest

from pages.login_page import LoginPage
from pages.inventory_page import InventoryPage


def load_ui_test_data() -> dict:
    """Load UI test data from JSON file."""
    root_dir = Path(__file__).resolve().parents[3]
    data_path = root_dir / "data" / "ui_test_data.json"
    with open(data_path, "r", encoding="utf-8") as f:
        return json.load(f)


ui_data = load_ui_test_data()


@pytest.mark.ui
@pytest.mark.parametrize(
    "username,password,description",
    [
        (
            ui_data["valid_logins"][0]["username"],
            ui_data["valid_logins"][0]["password"],
            ui_data["valid_logins"][0]["description"],
        )
    ],
)
def test_login_success(driver, logger, username, password, description):
    """Validate that a valid user can login and see the inventory page."""
    logger.info(f"Starting positive login test for: {description}")
    login_page = LoginPage(driver)
    inventory_page = InventoryPage(driver)

    login_page.login(username, password)

    assert inventory_page.is_page_displayed(), "Inventory page should be displayed after successful login"
    products = inventory_page.get_all_product_names()
    logger.info(f"Products visible after login: {products}")
    assert len(products) > 0, "There should be at least one product visible after login"


@pytest.mark.ui
@pytest.mark.parametrize(
    "username,password,description",
    [
        (
            invalid["username"],
            invalid["password"],
            invalid["description"],
        )
        for invalid in ui_data["invalid_logins"]
    ],
)
def test_login_invalid_credentials(driver, logger, username, password, description):
    """Validate login failure for invalid credentials."""
    logger.info(f"Starting negative login test for: {description}")
    login_page = LoginPage(driver)

    login_page.login(username, password)

    assert login_page.is_page_displayed(), "Login page should still be displayed after failed login"
    error_message = login_page.get_error_message()
    logger.info(f"Error message displayed: {error_message}")
    assert error_message != "", "Error message should be displayed for invalid login"
