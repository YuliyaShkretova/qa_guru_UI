import webbrowser

import pytest
from selene.support.shared import browser


@pytest.fixture(scope='session',autouse=True)
def browser_setup():
    browser.config.driver_name = 'chrome'
    browser.config.base_url = 'https://demoqa.com'
    browser.config.window_width = 903
    browser.config.window_height = 1166
    browser.config.timeout = 10

    yield
    browser.quit()
