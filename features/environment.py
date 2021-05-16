from behave import fixture, use_fixture
from selenium import webdriver
from src.po.github import GithubPO


@fixture
def init_firefox_driver(context) -> None:
    driver = webdriver.Firefox()
    github = GithubPO(driver)
    context.github = github

    yield context

    driver.quit()


def before_all(context) -> None:
    use_fixture(init_firefox_driver, context)
