import pytest

from pages.login_page import LoginPage
from pages.inventory_page import InventoryPage
from pages.cart_page import CartPage

VALID_USERNAME = "standard_user"
VALID_PASSWORD = "secret_sauce"
TEST_PRODUCT_NAME = "Sauce Labs Backpack"


@pytest.mark.ui
def test_add_product_to_cart(driver, logger):
    """
    Flow:
    - Login with valid credentials
    - Add a product to the cart
    - Go to cart and verify the product is present
    """
    logger.info("Starting test_add_product_to_cart")

    login_page = LoginPage(driver)
    inventory_page = InventoryPage(driver)
    cart_page = CartPage(driver)

    login_page.login(VALID_USERNAME, VALID_PASSWORD)
    assert inventory_page.is_page_displayed(), "Inventory page should be displayed after login"

    inventory_page.add_product_to_cart_by_name(TEST_PRODUCT_NAME)
    inventory_page.go_to_cart()

    cart_products = cart_page.get_cart_product_names()
    logger.info(f"Products in cart: {cart_products}")

    assert TEST_PRODUCT_NAME in cart_products, "Selected product should be present in the cart"


@pytest.mark.ui
def test_logout_from_inventory(driver, logger):
    """
    Flow:
    - Login
    - Logout from inventory page
    - Verify that login page is displayed again
    """
    logger.info("Starting test_logout_from_inventory")

    login_page = LoginPage(driver)
    inventory_page = InventoryPage(driver)

    login_page.login(VALID_USERNAME, VALID_PASSWORD)
    assert inventory_page.is_page_displayed(), "Inventory page should be displayed after login"

    inventory_page.logout()

    # Wait for login page to load again after logout
    login_page.wait_for_page_loaded()

    assert login_page.is_page_displayed(), "Login page should be displayed after logout"
