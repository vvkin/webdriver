from selenium.webdriver.common.by import By


class GithubLocators:
    SEARCH = (
        By.CSS_SELECTOR,
        'input[name="q"]'
    )

    RELATED_TOPIC = (
        By.XPATH,
        './/a[text()="See topic"]/../h3'
    )

    RELATED_LANGUAGES = (
        By.XPATH,
        './/ul[contains(@class, "filter-list")]/li/a[@class="filter-item"]'
    )

    REPOSITORY = (
        By.XPATH,
        './/ul[contains(@class, "repo-list")][{0}]'
    )

    COUNT_SEARCH = (
        By.CSS_SELECTOR,
        'div.codesearch-results h3:not([class])'
    )

    COUNT_MENU = (
        By.CSS_SELECTOR,
        'nav.menu > a.selected > span'
    )
