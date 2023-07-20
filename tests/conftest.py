import os

import dotenv
import pytest
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selene import Browser, Config
from dotenv import load_dotenv
from webdriver_manager.chrome import ChromeDriverManager

DEFAULT_BROWSER_VERSION = "100.0"

def pytest_addoption(parser):
    parser.addoption(
        '--browser_version',
        default='100.0'
    )

@pytest.fixture(scope='session', autouse=True)
def load_env():
    dotenv.load_dotenv('../.env')

@pytest.fixture(scope='session')
def setup_browser(request):
    browser_version = request.config.getoption('--browser_version')
    browser_version = browser_version if browser_version != "" else DEFAULT_BROWSER_VERSION

    options = Options()
    selenoid_capabilities = {
        "browserName": "chrome",
        "browserVersion": browser_version,
        "selenoid:options": {
            "enableVNC": True,
            "enableVideo": True
        }
    }
    options.add_argument('--disable-dev-shm-usage')

    options.capabilities.update(selenoid_capabilities)

    login = os.getenv('LOGIN')
    password = os.getenv('PASSWORD!')
    try:
        driver = webdriver.Remote(
            command_executor=f"https://{login}:{password}@selenoid.autotests.cloud/wd/hub",
            options=options
        )
        print("Successfully connected to Selenoid.")
    except Exception as e:
        print(f"Failed to connect to Selenoid: {e}")
        raise

    browser = Browser(Config(driver))


    yield browser


#         attach.add_html(browser)
#         attach.add_screenshot(browser)
#         attach.add_logs(browser)
#         attach.add_video(browser)
#         browser.quit()
