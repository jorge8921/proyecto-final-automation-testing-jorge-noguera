from selenium.webdriver.remote.webdriver import WebDriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class BasePage:
    """Base page object with common Selenium helpers."""

    def __init__(self, driver: WebDriver, timeout: int = 20) -> None:
        # Slightly higher timeout to make tests more stable in slow environments
        self.driver = driver
        self.timeout = timeout

    def wait_for_element_visible(self, locator: tuple) -> object:
        """Wait until element is visible and return it."""
        return WebDriverWait(self.driver, self.timeout).until(
            EC.visibility_of_element_located(locator)
        )

    def wait_for_element_clickable(self, locator: tuple) -> object:
        """Wait until element is clickable and return it."""
        return WebDriverWait(self.driver, self.timeout).until(
            EC.element_to_be_clickable(locator)
        )

    def click(self, locator: tuple) -> None:
        """Click element located by locator."""
        element = self.wait_for_element_clickable(locator)
        element.click()

    def type_text(self, locator: tuple, text: str) -> None:
        """Type text into input located by locator."""
        element = self.wait_for_element_visible(locator)
        element.clear()
        element.send_keys(text)

    def get_text(self, locator: tuple) -> str:
        """Get text from element located by locator."""
        element = self.wait_for_element_visible(locator)
        return element.text

    def is_element_displayed(self, locator: tuple) -> bool:
        """Return True if element is displayed, False otherwise."""
        try:
            element = self.wait_for_element_visible(locator)
            return element.is_displayed()
        except Exception:
            return False
