from selenium.webdriver.remote.webdriver import WebDriver
from po.base import BasePO


class GithubPO(BasePO):
    def __init__(self, driver: WebDriver) -> None:
        super().__init__(driver, 'https://github.com')
