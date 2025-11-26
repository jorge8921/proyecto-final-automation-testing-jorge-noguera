from selenium.webdriver.common.by import By
from .base_page import BasePage


class CartPage(BasePage):
    """Page Object Model for the SauceDemo cart page."""

    CART_ITEM = (By.CLASS_NAME, "cart_item")
    CART_ITEM_NAME = (By.CLASS_NAME, "inventory_item_name")
    CHECKOUT_BUTTON = (By.ID, "checkout")

    def get_cart_product_names(self) -> list[str]:
        """Return a list with product names in the cart."""
        self.wait_for_element_visible(self.CART_ITEM)
        items = self.driver.find_elements(*self.CART_ITEM)
        names: list[str] = []
        for item in items:
            name_el = item.find_element(*self.CART_ITEM_NAME)
            names.append(name_el.text)
        return names

    def proceed_to_checkout(self) -> None:
        """Click the Checkout button."""
        self.click(self.CHECKOUT_BUTTON)
