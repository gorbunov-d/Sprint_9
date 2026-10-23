from urllib.parse import urlparse

from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait

from config import BASE_URL, TIMEOUT


class BasePage:
    def __init__(self, driver):
        self._driver = driver
        self._wait = WebDriverWait(driver, TIMEOUT)

    def open(self, path="/"):
        self._driver.get(f"{BASE_URL}{path}")
        return self

    def click(self, locator):
        self._wait.until(EC.element_to_be_clickable(locator)).click()

    def fill(self, locator, value):
        element = self._wait.until(EC.visibility_of_element_located(locator))
        element.clear()
        element.send_keys(value)

    def visible(self, locator):
        return self._wait.until(EC.visibility_of_element_located(locator)).is_displayed()

    def is_at(self, path):
        return self._wait.until(lambda driver: urlparse(driver.current_url).path.rstrip("/") == path.rstrip("/"))
