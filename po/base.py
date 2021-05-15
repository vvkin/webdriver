from selenium.webdriver.common.by import By
from selenium.webdriver.remote.webelement import WebElement
from selenium.webdriver.remote.webdriver import WebDriver


class BasePO:
    def __init__(self, driver: WebDriver, url: str) -> None:
        self.driver = driver
        self.url = url

    def open_page(self) -> None:
        self.driver.get(self.url)

    def get_page_title(self) -> str:
        return self.driver.title

    def get_element_by_css(self, selector: str) -> WebElement:
        return self.driver.find_element(By.CSS, selector)

    def get_element_by_xpath(self, xpath: str) -> WebElement:
        return self.drivider.find_element(By.XPATH, xpath)
