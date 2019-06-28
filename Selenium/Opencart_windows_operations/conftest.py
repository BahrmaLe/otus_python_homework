"""Fixtures to testing Opencart login page"""
import os
import sys
import pytest
from selenium import webdriver as WD

from Selenium.Opencart_windows_operations.models.page_objects.page_objects import LoginPage, \
    ProductPage, NewProduct, ProductManager

dirname = os.path.dirname(__file__)
image = os.path.join(dirname, '1.JPG')


def pytest_addoption(parser):
    """Setting base URL Openacart and parametrize command line options for select
    browsers and set username or password """
    parser.addoption("--address", action="store", default="http://http://demo23.opencart.pro/",
                     help="Opencart web address")
    parser.addoption("--browser", action="store", default="firefox", help="Browser name")
    parser.addoption("--username", action="store", default="demo", help="User Name")
    parser.addoption("--password", action="store", default="demo", help="User Password")
    parser.addoption("--iwait", action="store", default="30000", help="Implicitly wait parameter")
    parser.addoption("--pltimeout", action="store", default="1000", help="Page load timeout")
    parser.addoption("--productname", action="store", default="New Product", help="Product Name")
    parser.addoption("--keywords", action="store",
                     default="New Meta Tag Keyword",
                     help="Meta Tag Keyword")
    parser.addoption("--modelname", action="store", default="New model", help="Model Name")


@pytest.fixture(scope="session", autouse=True)
def driver(request):
    """Launching webdriver"""
    browser_name = request.config.getoption("--browser")
    print(browser_name)
    if browser_name == 'firefox':
        capabilities = WD.DesiredCapabilities.FIREFOX.copy()
        capabilities['timeouts'] = {'implicit': 300000, 'pageLoad': 300000, 'script': 30000}
        capabilities['loggingPrefs'] = {'browser': 'ALL', 'client': 'ALL', 'driver': 'ALL',
                                        'performance': 'ALL', 'server': 'ALL'}
        capabilities['unexpectedAlertBehaviour'] = 'dismiss'
        profile = WD.FirefoxProfile()
        profile.set_preference('app.update.auto', False)
        profile.set_preference('app.update.enabled', False)
        profile.accept_untrusted_certs = True
        wd = WD.Firefox(firefox_profile=profile, capabilities=capabilities)
        wd.maximize_window()
    elif browser_name == 'chrome':
        capabilities = WD.DesiredCapabilities.CHROME.copy()
        capabilities['acceptSslCerts'] = True
        capabilities['acceptInsecureCerts'] = True
        capabilities['unexpectedAlertBehaviour'] = 'dismiss'
        wd = WD.Chrome(desired_capabilities=capabilities)
        wd.fullscreen_window()
    else:
        print('Unsupported browser!')
        sys.exit(1)
    wd.implicitly_wait((request.config.getoption("--iwait")))
    wd.set_page_load_timeout((request.config.getoption("--pltimeout")))
    implicitly_wait = request.config.getoption("--iwait")
    page_load_timeout = request.config.getoption("--pltimeout")
    print(implicitly_wait)
    print(page_load_timeout)
    yield wd
    wd.quit()


@pytest.fixture(scope="function")
def open_opencart_admin_url(driver, request):
    """Get base URL and attend admin link"""
    url = 'admin/'
    return driver.get("".join([request.config.getoption("--address"), url]))


@pytest.fixture(scope="function")
def login_form_operator(driver, open_opencart_admin_url):
    """Use class from page objects module for managing elements on the page"""
    return LoginPage(driver)


@pytest.fixture(scope="function")
def set_login_data(login_form_operator, request, driver):
    """Open admin login page and login in"""
    login_form_operator.login(request.config.getoption("--username"), request.config.getoption("--password"))


@pytest.fixture(scope="function")
def new_product_operator(driver, open_opencart_admin_url):
    """Use class from  page objects module for managing elements on the page"""
    return NewProduct(driver)


@pytest.fixture(scope="function")
def product_manager(driver, open_opencart_admin_url):
    """Use class from  page objects module for managing elements on the page"""
    return ProductManager(driver)


@pytest.fixture(scope='function')
def add_product_with_image(driver, set_login_data, new_product_operator, product_manager, request):
    """Adding new product"""
    product_manager.add_new_product_with_images(request.config.getoption("--productname"),
                                                request.config.getoption("--modelname"), image)
    # driver.back()
    # driver.back()
    # driver.refresh()


@pytest.fixture(scope="function")
def products_page_operator(driver, open_opencart_admin_url):
    """Use class from  page objects module for managing elements on the page"""
    return ProductPage(driver)


@pytest.fixture(scope='function')
def products_list(driver, open_opencart_admin_url, login_form_operator, products_page_operator):
    """Return products list with names"""
    return products_page.all_products_list()



