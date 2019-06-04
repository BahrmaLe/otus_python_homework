"""Fixtures to testing Opencart login page"""
import sys
import time

import pytest
from selenium import webdriver
from Selenium.Opencart_login_page.models.page_objects.page_objects import LoginPage


def pytest_addoption(parser):
    """Setting base URL Openacart and parametrize command line options for select browsers"""
    parser.addoption("--address", action="store", default="http://192.168.56.103/",
                     help="Opencart web address")
    parser.addoption("--browser", action="store", default="firefox", help="Browser name")


@pytest.fixture(scope="session")
def open_login_page(driver, request):
    """Get base URL and attend admin link"""
    url = 'opencart/admin/'
    return driver.get("".join([request.config.getoption("--address"), url]))


@pytest.fixture(scope="function", autouse=True)
def login_page(open_login_page, driver):
    """Use class from  page objects module for managing elements on the page"""
    return LoginPage(driver)


@pytest.fixture(scope="function", autouse=True)
def browser_action(login_page, request):
    """Get browser from command line key"""
    browser_name = request.config.getoption("--browser")
    print(browser_name)
    login_page.set_username("admin")
    login_page.set_password("")
    if browser_name == "firefox":
        login_page.login()
        time.sleep(2)
    elif browser_name == "chrome":
        login_page.submit()
        time.sleep(5)
    message = login_page.alerttext()
    time.sleep(5)
    yield message
    login_page.alert_close_button()
    time.sleep(1)



# @pytest.fixture(scope="function",)
# def login(login_page):
#     """Set Username and Password"""
#     login_page.set_username("admin")
#     login_page.set_password("")
#     login_page.login()
#     time.sleep(3)
#
#
# @pytest.fixture(scope="function",)
# def submit(login_page):
#     """Set Username and Password by another element(locator)"""
#     login_page.set_username("admin")
#     login_page.set_password("")
#     login_page.submit()
#     time.sleep(3)


@pytest.fixture(scope="session", autouse=True)
def driver(request):
    """Launching webdriver"""
    browser_name = request.config.getoption("--browser")
    if browser_name == 'firefox':
        capabilities = webdriver.DesiredCapabilities.FIREFOX.copy()
        capabilities['timeouts'] = {'implicit': 300000, 'pageLoad': 300000, 'script': 30000}
        capabilities['loggingPrefs'] = {'browser': 'ALL', 'client': 'ALL', 'driver': 'ALL',
                                        'performance': 'ALL', 'server': 'ALL'}
        profile = webdriver.FirefoxProfile()
        profile.set_preference('app.update.auto', False)
        profile.set_preference('app.update.enabled', False)
        profile.accept_untrusted_certs = True
        wd = webdriver.Firefox(firefox_profile=profile, capabilities=capabilities)
        wd.maximize_window()
    elif browser_name == 'chrome':
        capabilities = webdriver.DesiredCapabilities.CHROME.copy()
        capabilities['acceptSslCerts'] = True
        capabilities['acceptInsecureCerts'] = True
        wd = webdriver.Chrome(desired_capabilities=capabilities)
        wd.fullscreen_window()
    # elif browser == 'ie':
    #     capabilities = webdriver.DesiredCapabilities.INTERNETEXPLORER.copy()
    #     capabilities.pop("platform", None)
    #     capabilities.pop("version", None)
    #     wd = webdriver.Ie(desired_capabilities=capabilities)
    #     wd.fullscreen_window()
    else:
        print('Unsupported browser!')
        sys.exit(1)
    yield wd
    wd.quit()
