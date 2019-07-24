import pytest
from selenium import webdriver
import sys
import pytest
from selenium import webdriver
from Selenium.Opencart_login_page.models.page_objects.page_objects import LoginPage


def pytest_addoption(parser):
    """Setting base URL Openacart and parametrize command line options for select browsers and set username or
    password """
    parser.addoption("--address", action="store", default="http://demo23.opencart.pro/",
                     help="Opencart web address")
    parser.addoption("--browser", action="store", default="cloud", help="Browser name")
    parser.addoption("--username", action="store", default="demo", help="User Name")
    parser.addoption("--password", action="store", default="demo", help="User Name")


@pytest.fixture(scope="session")
def open_login_page(driver, request):
    """Get base URL and attend admin link"""
    url = 'admin/'
    return driver.get("".join([request.config.getoption("--address"), url]))


@pytest.fixture(scope="function", autouse=True)
def login_page(open_login_page, driver):
    """Use class from  page objects module for managing elements on the page"""
    return LoginPage(driver)


@pytest.fixture(scope="function", autouse=True)
def login_action(login_page, request, driver):
    """Set username/password by command line parameters and do login"""
    login_page.set_username(request.config.getoption("--username"))
    login_page.set_password(request.config.getoption("--password"))


@pytest.fixture(scope="function")
def current_url(request, driver, login_action, login_page):
    """Use login button element depends from browser and get current page url"""
    browser_name = request.config.getoption("--browser")
    print(browser_name)
    if browser_name == "firefox":
        login_page.login()
        driver.implicitly_wait(1)
    elif browser_name == "cloud":
        login_page.submit()
        driver.implicitly_wait(1)
    yield driver.current_url


@pytest.fixture(scope="session", autouse=True)
def driver(request):
    """Getting driver according to command line option"""
    browser = request.config.getoption("--browser")
    if browser == 'chrome':
        chrome_options = webdriver.ChromeOptions()
        capabilities = webdriver.DesiredCapabilities.CHROME.copy()
        capabilities['acceptSslCerts'] = True
        capabilities['acceptInsecureCerts'] = True
        capabilities['loggingPrefs'] = {'performance': 'ALL'}
        wd = webdriver.Chrome(desired_capabilities=capabilities, options=chrome_options)
        wd.implicitly_wait(5)
        wd.maximize_window()
    elif browser == 'cloud':
        desired_cap = {
            'browser': 'Safari',
            'browser_version': '12.0',
            'os': 'OS X',
            'os_version': 'Mojave',
            'resolution': '1024x768',
            'name': 'Bstack-[Python] Sample Test'
        }

        wd = webdriver.Remote(command_executor='http://antonkuksenko2:U5MzCpsTLmSdKwgQ9MGj@hub.browserstack.com:80/wd'
                                               '/hub', desired_capabilities=desired_cap)

    else:
        print('Unsupported browser!')
        sys.exit(1)
    yield wd
    wd.quit()





