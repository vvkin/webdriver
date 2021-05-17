from selenium.webdriver.common.by import By


class RepositoryLocators:
    NAME = (
        By.CSS_SELECTOR,
        'a[class="v-align-middle"]'
    )

    LANGUAGE = (
        By.CSS_SELECTOR,
        'span[itemprop="programmingLanguage"]'
    )
