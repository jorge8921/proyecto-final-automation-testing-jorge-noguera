import pytest

from pages.login_page import LoginPage
from pages.inventory_page import InventoryPage
from pages.cart_page import CartPage
from pages.checkout_page import CheckoutPage

VALID_USERNAME = "standard_user"
VALID_PASSWORD = "secret_sauce"
TEST_PRODUCT_NAME = "Sauce Labs Backpack"


@pytest.mark.ui
def test_full_checkout_flow(driver, logger):
    """
    Flow:
    - Login
    - Add a product
    - Go to cart
    - Proceed to checkout
    - Fill customer information
    - Finish order and verify success message
    """
    logger.info("Starting test_full_checkout_flow")

    login_page = LoginPage(driver)
    inventory_page = InventoryPage(driver)
    cart_page = CartPage(driver)
    checkout_page = CheckoutPage(driver)

    login_page.login(VALID_USERNAME, VALID_PASSWORD)
    assert inventory_page.is_page_displayed(), "Inventory page should be displayed after login"

    inventory_page.add_product_to_cart_by_name(TEST_PRODUCT_NAME)
    inventory_page.go_to_cart()

    cart_products = cart_page.get_cart_product_names()
    logger.info(f"Products in cart before checkout: {cart_products}")
    assert TEST_PRODUCT_NAME in cart_products, "Selected product should be present before checkout"

    cart_page.proceed_to_checkout()

    checkout_page.fill_customer_information(
        first_name="Jorge",
        last_name="Noguera",
        postal_code="1000",
    )
    checkout_page.finish_checkout()

    success_message = checkout_page.get_success_message()
    logger.info(f"Success message: {success_message}")

    assert "THANK YOU" in success_message.upper(), "Order completion message should be displayed"
