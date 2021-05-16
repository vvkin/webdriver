from selenium.webdriver.remote.webdriver import WebDriver
from selenium.webdriver.common.by import By
from selenium.webdriver.remote.webelement import WebElement
from selenium.webdriver.common.keys import Keys
from src.po.base import BasePO
from src.helpers.parse_ci import parse_int


class GithubPO(BasePO):
    def __init__(self, driver: WebDriver) -> None:
        super().__init__(driver, 'https://github.com')

    def search(self, query: str) -> None:
        element = self.get_by_css('input[name="q"]')
        element.send_keys(query)
        element.send_keys(Keys.ENTER)

    def get_related_topic(self) -> str:
        try:
            selector = 'div.codesearch-results h3.mb-1'
            element = self.get_by_css(selector)
            return element.text
        except: return 'Not specified'

    def __get_nth_repo(self, repo_number: int) -> WebElement:
        selector = f'ul.repo-list :nth-child({repo_number})'
        element = self.get_by_css(selector)
        return element

    def get_nth_repo_name(self, repo_number: int) -> str:
        repo = self.__get_nth_repo(repo_number)
        selector = 'a.v-align-middle'
        name = repo.find_element(By.CSS_SELECTOR, selector)
        return name.text

    def get_nth_repo_language(self, repo_number: int) -> str:
        repo = self.__get_nth_repo(repo_number)
        selector = 'span[itemprop="programmingLanguage"]'
        language = repo.find_element(By.CSS_SELECTOR, selector)
        return language.text

    def get_repo_count_from_menu(self) -> int:
        selector = 'span.js-codesearch-count[data-search-type="Repositories"]'
        element = self.get_by_css(selector)
        return parse_int(element.text)

    def get_repo_count_from_search(self) -> int:
        selector = 'div.codesearch-results h3:not(.mb-1)'
        element = self.get_by_css(selector)
        return parse_int(element.text.split()[0])

    def get_related_languages(self) -> list[str]:
        lang_list = self.get_by_css('ul.filter-list')
        lang_items = lang_list.find_elements(By.CSS_SELECTOR, 'a.filter-item')
        languages = [item.text.split('\n')[1] for item in lang_items]
        return languages
