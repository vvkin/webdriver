from selenium.webdriver.remote.webdriver import WebDriver
from selenium.webdriver.remote.webelement import WebElement
from selenium.webdriver.common.keys import Keys

from src.helpers.number import parse_int, scale_int
from .base import BasePO
from .locators import GithubLocators, RepositoryLocators
from .locators.format import format_locator


class GithubPO(BasePO):
    def __init__(self, driver: WebDriver) -> None:
        super().__init__(driver, 'https://github.com')

    def search(self, query: str) -> None:
        element = self.get_one(GithubLocators.SEARCH)
        element.send_keys(query)
        element.send_keys(Keys.ENTER)

    def get_related_topic(self) -> str:
        try:
            element = self.get_one(GithubLocators.RELATED_TOPIC)
            return element.text
        except Exception: return 'Not specified'

    def __get_nth_repo(self, repo_number: int) -> WebElement:
        locator = format_locator(GithubLocators.REPOSITORY, repo_number)
        return self.get_one(locator)

    def get_nth_repo_name(self, repo_number: int) -> str:
        repo = self.__get_nth_repo(repo_number)
        element = repo.find_element(*RepositoryLocators.NAME)
        return element.text

    def get_nth_repo_language(self, repo_number: int) -> str:
        repo = self.__get_nth_repo(repo_number)
        element = repo.find_element(*RepositoryLocators.LANGUAGE)
        return element.text

    def get_repo_count_from_menu(self) -> int:
        element = self.get_one(GithubLocators.COUNT_MENU)
        return parse_int(element.text)

    def get_repo_count_from_search(self) -> int:
        element = self.get_one(GithubLocators().COUNT_SEARCH)
        number = parse_int(element.text.split()[0])
        return scale_int(number)

    def get_related_languages(self) -> list[str]:
        elements = self.get_all(GithubLocators.RELATED_LANGUAGES)
        languages = [element.text.split('\n')[1] for element in elements]
        return languages
