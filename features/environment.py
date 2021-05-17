from behave import fixture, use_fixture
from behave.runner import Context
from selenium.webdriver import Firefox
from typing import Generator

from src.po import GithubPO


@fixture
def init_firefox_driver(context: Context) -> Generator[Context, None, None]:
    driver = Firefox()
    github = GithubPO(driver)
    context.github = github

    yield context
    driver.quit()


def before_all(context: Context) -> None:
    use_fixture(init_firefox_driver, context)
