from selenium.webdriver.common.by import By
from .base_page import BasePage


class LoginPage(BasePage):
    """Page Object Model for the SauceDemo Login page."""

    USERNAME_INPUT = (By.ID, "user-name")
    PASSWORD_INPUT = (By.ID, "password")
    LOGIN_BUTTON = (By.ID, "login-button")
    ERROR_MESSAGE = (By.CSS_SELECTOR, "[data-test='error']")

    def login(self, username: str, password: str) -> None:
        """Perform login action with given credentials."""
        self.type_text(self.USERNAME_INPUT, username)
        self.type_text(self.PASSWORD_INPUT, password)
        self.click(self.LOGIN_BUTTON)

    def get_error_message(self) -> str:
        """Return the error message text after a failed login."""
        return self.get_text(self.ERROR_MESSAGE)

    def is_page_displayed(self) -> bool:
        """Check if login page is displayed."""
        return self.is_element_displayed(self.USERNAME_INPUT)

    def wait_for_page_loaded(self) -> None:
        """Wait until login page is fully loaded."""
        self.wait_for_element_visible(self.USERNAME_INPUT)
