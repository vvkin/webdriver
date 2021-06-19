from behave import given, when, then
from behave.runner import Context


@given('I open the GitHub website')
def step_impl(context: Context) -> None:
    context.github.open_page()
    actual_url = context.github.get_page_url()
    assert actual_url == 'https://github.com/'


@when('I enter the {query} repository')
def step_impl(context: Context, query: str) -> None:
    context.github.search(query)
    context.github.wait_for_redirect(5)


@then('I am being redirected to the page with {query} results')
def step_impl(context: Context, query: str) -> None:
    expected_title = f'Search · {query} · GitHub'
    actual_title = context.github.get_page_title()
    assert actual_title == expected_title


@then('repositories number is greater than null')
def step_impl(context: Context) -> None:
    actual_m_count = context.github.get_repo_count_from_menu()
    actual_s_count = context.github.get_repo_count_from_search()
    assert actual_m_count == actual_s_count
    assert actual_m_count > 0


@then('the related topic is {topic}')
def step_impl(context: Context, topic: str) -> None:
    actual_topic = context.github.get_related_topic()
    assert actual_topic == topic


@then('the first repository is {repository}')
def step_impl(context: Context, repository: str) -> None:
    actual_repository = context.github.get_nth_repo_name(1)
    assert actual_repository == repository


@then('its language is {language}')
def step_impl(context: Context, language: str) -> None:
    actual_language = context.github.get_nth_repo_language(1)
    assert actual_language == language


@then('{language} is present within related languages')
def step_impl(context: Context, language: str) -> None:
    actual_languages = context.github.get_related_languages()
    assert language in actual_languages
