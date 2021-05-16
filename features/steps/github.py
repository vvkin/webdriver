from behave import given, when, then


@given('I open the GitHub website')
def step_impl(context):
    context.github.open_page()
    url = context.github.get_page_url()
    assert url == 'https://github.com/'


@when('I enter the {query} repository')
def step_impl(context, query: str):
    context.github.search(query)
    context.github.wait_for_redirect(5)


@then('I am being redirected to the page with {query} results')
def step_impl(context, query: str):
    expected_title = f'Search · {query} · GitHub'
    assert context.github.get_page_title() == expected_title


@then('repositories number is greater than null')
def step_impl(context):
    actual_m_count = context.github.get_repo_count_from_menu()
    actual_s_count = context.github.get_repo_count_from_search()
    assert actual_m_count == actual_s_count
    assert actual_m_count > 0


@then('the related topic is {topic}')
def step_impl(context, topic: str):
    actual_topic = context.github.get_related_topic()
    assert actual_topic == topic


@then('the first repository is {repository}')
def step_impl(context, repository: str):
    actual_name = context.github.get_nth_repo_name(1)
    assert actual_name == repository


@then('its language is {language}')
def step_impl(context, language: str):
    actual_language = context.github.get_nth_repo_language(1)
    assert actual_language == language


@then('{language} is present within related languages')
def step_impl(context, language: str):
    actual_languages = context.github.get_related_languages()
    assert language in actual_languages
