from selenium.webdriver.common.by import By
from selenium.webdriver.remote.webelement import WebElement
from selenium.webdriver.remote.webdriver import WebDriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.support import expected_conditions as EC


class BasePO:
    def __init__(self, driver: WebDriver, url: str) -> None:
        self.driver = driver
        self.url = url

    def get_wait(self, timeout: int) -> WebDriverWait:
        return WebDriverWait(self.driver, timeout)

    def wait(self, timeout: int) -> None:
        self.driver.implicitly_wait(timeout)

    def wait_for_redirect(self, timeout: int) -> None:
        wait = self.get_wait(timeout)
        prev_url = self.get_page_url()
        condition = lambda driver: driver.title and\
            driver.current_url != prev_url
        wait.until(condition)

    def open_page(self) -> None:
        self.driver.get(self.url)

    def get_page_title(self) -> str:
        return self.driver.title

    def get_page_url(self) -> str:
        return self.driver.current_url

    def __get_by_locator(self, locator: tuple[str, str], timeout: int) -> WebElement:
        try:
            wait = self.get_wait(timeout)
            return wait.until(EC.presence_of_element_located(locator))
        except TimeoutException:
            raise Exception('Could not find element')

    def get_by_css(self, selector: str, timeout: int = 0) -> WebElement:
        return self.__get_by_locator((By.CSS_SELECTOR, selector), timeout)

    def get_by_xpath(self, xpath: str, timeout: int = 0) -> WebElement:
        return self.__get_by_locator((By.XPATH, xpath), timeout)
