import os
import pytest
from selene import browser
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from utils import attach
from dotenv import load_dotenv
import allure

DEFAULT_BROWSER_VERSION = '126.0'


def pytest_addoption(parser):
    parser.addoption(
        '--browser_version',
        default='120.0'
    )


@pytest.fixture(scope='session', autouse=True)
def load_env():
    load_dotenv()


@pytest.fixture(autouse=True, scope='function')
def browser_management(request):
    with allure.step("Параметры браузера"):
        browser_version = request.config.getoption('--browser_version')

        browser_version = browser_version if browser_version != '' else DEFAULT_BROWSER_VERSION
        options = Options()
        selenoid_capabilities = {
            "browserName": "chrome",
            "browserVersion": browser_version,
            "selenoid:options": {
                "enableVNC": True,
                "enableVideo": True
            }
        }

    options.capabilities.update(selenoid_capabilities)

    login = os.getenv('LOGIN')
    password = os.getenv('PASSWORD')
    selenoid_host = os.getenv('SELENOID_HOST')

    driver = webdriver.Remote(
        command_executor=f'https://{login}:{password}@{selenoid_host}/wd/hub',
        options=options)

    browser.config.driver = driver

    driver_options = webdriver.ChromeOptions()
    driver_options.page_load_strategy = 'eager'
    browser.config.driver_options = driver_options

    browser.config.timeout = 2.0
    browser.config.window_width = 1920
    browser.config.window_height = 1080

    yield browser

    attach.add_screenshot(browser)
    attach.add_logs(browser)
    attach.add_html(browser)
    attach.add_video(browser)

    browser.quit()
