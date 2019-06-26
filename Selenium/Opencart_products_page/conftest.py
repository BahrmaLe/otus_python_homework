"""Fixtures to testing Opencart login page"""
import sys
import pytest
from selenium import webdriver
from Selenium.Opencart_products_page.models.page_objects.page_objects import LoginPage, \
    CatalogMenu, ProductsPage, ProductPage, ProductManager


def pytest_addoption(parser):
    """Setting base URL Openacart and parametrize command line options for select
    browsers and set username or password """
    parser.addoption("--address", action="store", default="http://192.168.56.103/",
                     help="Opencart web address")
    parser.addoption("--browser", action="store", default="firefox", help="Browser name")
    parser.addoption("--username", action="store", default="admin", help="User Name")
    parser.addoption("--password", action="store", default="admin", help="User Password")
    parser.addoption("--iwait", action="store", default="30000", help="Implicitly wait parameter")
    parser.addoption("--pltimeout", action="store", default="1000", help="Page load timeout")
    parser.addoption("--productname", action="store", default="New Product", help="Product Name")
    parser.addoption("--keywords", action="store",
                     default="New Meta Tag Keyword",
                     help="Meta Tag Keyword")
    parser.addoption("--modelname", action="store", default="New model", help="Model Name")


@pytest.fixture(scope="function")
def open_login_page(driver, request):
    """Get base URL and attend admin link"""
    url = 'opencart/admin/'
    return driver.get("".join([request.config.getoption("--address"), url]))


@pytest.fixture(scope="function")
def login_page(driver, open_login_page):
    """Use class from  page objects module for managing elements on the page"""
    return LoginPage(driver)


@pytest.fixture(scope="function")
def login_action(login_page, request, driver):
    """Open admin login page and login in"""
    login_page.login(request.config.getoption("--username"), request.config.getoption("--password"))


@pytest.fixture(scope="function")
def catalog_menu(driver, open_login_page):
    """Use class from  page objects module for managing elements on the page"""
    return CatalogMenu(driver)


@pytest.fixture(scope="function")
def product_manager(driver, open_login_page):
    """Use class from  page objects module for managing elements on the page"""
    return ProductManager(driver)


@pytest.fixture(scope="function")
def products_page(driver, open_login_page):
    """Use class from  page objects module for managing elements on the page"""
    return ProductsPage(driver)


@pytest.fixture(scope="function")
def product_card(driver, open_login_page):
    """Use class from  page objects module for managing elements on the page"""
    return ProductPage(driver)


@pytest.fixture(scope='function')
def open_products_page(catalog_menu):
    """Open product managements page"""
    catalog_menu.open_products_page()


@pytest.fixture(scope='function')
def add_product(driver, login_action, open_products_page, product_manager, request):
    """Adding new product"""
    product_manager.add_new_product(request.config.getoption("--productname"),
                                    request.config.getoption("--keywords"),
                                    request.config.getoption("--modelname"))
    driver.back()
    driver.back()
    driver.refresh()


@pytest.fixture(scope='function')
def edit_product(driver, login_action, open_products_page, product_manager, request):
    """Editing product"""
    product_manager.edit_product("".join([request.config.getoption("--productname"), " Edited"]),
                                 "".join([request.config.getoption("--keywords"), " Edited"]),
                                 "".join([request.config.getoption("--modelname"), " Edited"]))


@pytest.fixture(scope='function')
def delete_product(driver, login_action, open_products_page, products_page):
    """Matching and deleting product"""
    products_page.delete_product()
    driver.refresh()


@pytest.fixture(scope='function')
def products_list(driver, login_action, open_products_page, products_page):
    """Return products list with names"""
    return products_page.all_products_list()


@pytest.fixture(scope="session", autouse=True)
def driver(request):
    """Launching webdriver"""
    browser_name = request.config.getoption("--browser")
    print(browser_name)
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
