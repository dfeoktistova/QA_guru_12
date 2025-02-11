import os
import pytest
from selene import browser
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from utils import attach
from dotenv import load_dotenv
import allure

DEFAULT_BROWSER_VERSION = '120.0'


def pytest_addoption(parser):
    parser.addoption(
        '--browser',
        help='Браузер, на котором будут запущены тесты',
        choices=['chrome', 'firefox'],
        default='chrome'
    )

    parser.addoption(
        '--browser_version',
        help='Версия браузера, на котором будут запущены тесты',
        choices=['120.0', '100.0'],
        default='120.0'
    )


@pytest.fixture(scope='session', autouse=True)
def load_env():
    load_dotenv()


@pytest.fixture(scope='function')
def browser_management(request):
    with allure.step("Параметры браузера"):
        browser_name = request.config.getoption('--browser')
        browser_version = request.config.getoption('--browser_version')

        options = Options()
        selenoid_capabilities = {
            "browserName": browser_name,
            "browserVersion": browser_version,
            "selenoid:options": {
                "enableVNC": True,
                "enableVideo": True
            }
        }

    options.capabilities.update(selenoid_capabilities)

    driver = webdriver.Remote(
        command_executor=f"https://user1:1234@selenoid.autotests.cloud/wd/hub",
        options=options)

    browser.config.driver = driver

    options.page_load_strategy = 'eager'
    browser.config.base_url = 'https://demoqa.com'
    browser.config.timeout = 2.0
    browser.config.window_width = 1920
    browser.config.window_height = 1080

    yield browser

    attach.add_screenshot(browser)
    attach.add_logs(browser)
    attach.add_html(browser)
    attach.add_video(browser)

    browser.quit()
