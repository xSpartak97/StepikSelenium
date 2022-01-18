from selenium import webdriver
from selenium.webdriver.chrome.options import Options
import pytest


def pytest_addoption(parser):
    # Опция выбора языка
    parser.addoption('--language', action='store', default="en",
                     help="Choose language.")


@pytest.fixture(scope="function")
def browser(request):
    user_language = request.config.getoption("language")
    options = Options()
    options.add_experimental_option('prefs', {'intl.accept_languages': user_language})
    browser = webdriver.Chrome(options=options)
    browser.set_window_size(1552, 840)
    browser.maximize_window()
    yield browser
    print("\nquit browser..")
    browser.quit()