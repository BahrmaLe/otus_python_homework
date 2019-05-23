import sys
import pytest
from selenium import webdriver
from selenium.webdriver import ChromeOptions, FirefoxOptions, IeOptions


def pytest_addoption(parser):
    parser.addoption("--address", action="store", default="http://192.168.56.103/", help="Opencart web address")
    parser.addoption("--browser", action="store", default="firefox", help="Browser name")


@pytest.fixture(scope="session", autouse=True)
def driver(request):
    browser = request.config.getoption("--browser")
    if browser == 'firefox':
        options = FirefoxOptions()
        # options.add_argument("--headless")
        capabilities = options.to_capabilities()
        wd = webdriver.Firefox(desired_capabilities=capabilities)
        wd.maximize_window()
    elif browser == 'chrome':
        options = ChromeOptions()
        # options.add_argument("--headless")
        capabilities = options.to_capabilities()
        wd = webdriver.Chrome(desired_capabilities=capabilities)
        wd.fullscreen_window()
    elif browser == 'ie':
        options = IeOptions()
        # options.add_argument("--headless")
        capabilities = options.to_capabilities()
        wd = webdriver.Ie(desired_capabilities=capabilities)
        wd.fullscreen_window()
    else:
        print('Unsupported browser!')
        sys.exit(1)
    yield wd
    wd.quit()



