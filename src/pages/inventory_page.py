from selenium.webdriver.common.by import By
from .base_page import BasePage


class InventoryPage(BasePage):
    """Page Object Model for the SauceDemo inventory (products) page."""

    INVENTORY_CONTAINER = (By.ID, "inventory_container")
    INVENTORY_ITEM = (By.CLASS_NAME, "inventory_item")
    INVENTORY_ITEM_NAME = (By.CLASS_NAME, "inventory_item_name")
    CART_ICON = (By.ID, "shopping_cart_container")

    MENU_BUTTON = (By.ID, "react-burger-menu-btn")
    LOGOUT_LINK = (By.ID, "logout_sidebar_link")

    def is_page_displayed(self) -> bool:
        """Check if inventory page is displayed."""
        return self.is_element_displayed(self.INVENTORY_CONTAINER)

    def get_all_product_names(self) -> list[str]:
        """Return a list with all product names displayed."""
        self.wait_for_element_visible(self.INVENTORY_CONTAINER)
        items = self.driver.find_elements(*self.INVENTORY_ITEM)
        names: list[str] = []
        for item in items:
            name_el = item.find_element(*self.INVENTORY_ITEM_NAME)
            names.append(name_el.text)
        return names

    def add_product_to_cart_by_name(self, product_name: str) -> None:
        """Click Add to cart button for a product by its name."""
        self.wait_for_element_visible(self.INVENTORY_CONTAINER)
        items = self.driver.find_elements(*self.INVENTORY_ITEM)
        for item in items:
            name_el = item.find_element(*self.INVENTORY_ITEM_NAME)
            if name_el.text.strip() == product_name:
                add_button = item.find_element(By.TAG_NAME, "button")
                add_button.click()
                break

    def go_to_cart(self) -> None:
        """Click the cart icon to go to the cart page."""
        self.click(self.CART_ICON)

    def open_menu(self) -> None:
        """Open the side menu."""
        self.click(self.MENU_BUTTON)

    def logout(self) -> None:
        """Logout using the side menu."""
        self.open_menu()
        self.click(self.LOGOUT_LINK)
