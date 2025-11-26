from selenium.webdriver.common.by import By
from .base_page import BasePage


class CheckoutPage(BasePage):
    """Page Object Model for the SauceDemo checkout pages."""

    FIRST_NAME_INPUT = (By.ID, "first-name")
    LAST_NAME_INPUT = (By.ID, "last-name")
    POSTAL_CODE_INPUT = (By.ID, "postal-code")
    CONTINUE_BUTTON = (By.ID, "continue")

    OVERVIEW_CONTAINER = (By.ID, "checkout_summary_container")
    FINISH_BUTTON = (By.ID, "finish")
    SUCCESS_MESSAGE = (By.CLASS_NAME, "complete-header")

    def fill_customer_information(self, first_name: str, last_name: str, postal_code: str) -> None:
        """Fill checkout step one form and go to overview page."""
        self.type_text(self.FIRST_NAME_INPUT, first_name)
        self.type_text(self.LAST_NAME_INPUT, last_name)
        self.type_text(self.POSTAL_CODE_INPUT, postal_code)
        self.click(self.CONTINUE_BUTTON)

    def wait_for_overview_page(self) -> None:
        """Wait until checkout overview page is displayed."""
        self.wait_for_element_visible(self.OVERVIEW_CONTAINER)

    def finish_checkout(self) -> None:
        """Finish checkout on overview page."""
        self.wait_for_overview_page()
        self.click(self.FINISH_BUTTON)

    def get_success_message(self) -> str:
        """Return the success message text after completing the order."""
        return self.get_text(self.SUCCESS_MESSAGE)
