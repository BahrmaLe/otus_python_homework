"""Fixtures to testing Opencart login page"""
import sys
import pytest
from selenium import webdriver
from Selenium.Opencart_products_page.models.page_objects.page_objects import LoginPage, CatalogMenu, ProductsPage, \
    ProductPage


def pytest_addoption(parser):
    """Setting base URL Openacart and parametrize command line options for select browsers and set username or
    password """
    parser.addoption("--address", action="store", default="http://192.168.56.103/",
                     help="Opencart web address")
    parser.addoption("--browser", action="store", default="firefox", help="Browser name")
    parser.addoption("--username", action="store", default="admin", help="User Name")
    parser.addoption("--password", action="store", default="admin", help="User Name")


@pytest.fixture(scope="function")
def open_login_page(driver, request):
    """Get base URL and attend admin link"""
    url = 'opencart/admin/'
    return driver.get("".join([request.config.getoption("--address"), url]))


@pytest.fixture(scope="function")
def login_page(open_login_page, driver):
    """Use class from  page objects module for managing elements on the page"""
    return LoginPage(driver)


@pytest.fixture(scope="function")
def login_action(login_page, request, driver):
    """Set username/password by command line parameters and do login"""
    login_page.set_username(request.config.getoption("--username"))
    login_page.set_password(request.config.getoption("--password"))
    login_page.submit()


@pytest.fixture(scope="function")
def catalog_menu(open_login_page, driver):
    """Use class from  page objects module for managing elements on the page"""
    return CatalogMenu(driver)


@pytest.fixture(scope='function')
def delete_product(products_page):
    products_page.matchproduct()
    products_page.delete()


@pytest.fixture(scope="function")
def products_page(open_login_page, driver):
    """Use class from  page objects module for managing elements on the page"""
    return ProductsPage(driver)


@pytest.fixture(scope="function")
def product_card(open_login_page, driver):
    """Use class from  page objects module for managing elements on the page"""
    return ProductPage(driver)


@pytest.fixture(scope='function')
def open_products_page(catalog_menu):
    catalog_menu.open_catalog()
    catalog_menu.open_products()


@pytest.fixture(scope='function')
def add_product(driver, login_action, open_products_page, products_page, product_card):
    products_page.addnew2()
    product_card.productname('New Product')
    product_card.metatag('New Meta Tag Keyword')
    product_card.datatab()
    product_card.modelname('New model')
    product_card.savebutton()
    driver.back()
    driver.back()
    driver.refresh()


# @pytest.fixture(scope="function", autouse=True)
# def products_path(request, driver, login_action, login_page, catalog_menu):
#     """Use this func for moving to products page"""
#     browser_name = request.config.getoption("--browser")
#     print(browser_name)
#     if browser_name == "firefox":
#         login_page.login()
#         driver.implicitly_wait(1)
#     elif browser_name == "chrome":
#         login_page.submit()
#         driver.implicitly_wait(1)


# @pytest.fixture(scope="function", autouse=True)
# def open_product_page(driver, login_action, login_page, catalog_menu):
#     """Use this func for moving to products page"""
#     catalog_menu.open_catalog()
#     catalog_menu.open_products()
#
#
# @pytest.fixture(scope="function", autouse=True)
# def add_new_product(request, driver, login_page, login_action, product_page):
#     """Use this func for moving to products page"""
#     browser_name = request.config.getoption("--browser")
#     print(browser_name)
#     if browser_name == 'firefox':
#         products_page.addnew()
#         driver.implicitly_wait(3)
#         product_page.productname('New Product')
#         product_page.metatag('New Meta Tag Keyword')
#         product_page.datatab()
#         product_page.modelname('New model')
#         product_page.savebutton()
#         driver.implicitly_wait(3)
#     elif browser_name == "chrome":
#         products_page.addnew2()
#         driver.implicitly_wait(3)
#         product_page.productname('New Product')
#         product_page.metatag('New Meta Tag Keyword')
#         product_page.datatab()
#         product_page.modelname('New model')
#         product_page.savebutton()
#         driver.implicitly_wait(3)


# @pytest.fixture(scope="function")
# def fill_product_page(request, driver, login_action, login_page, catalog_menu, products_page, product_page):
#     browser_name = request.config.getoption("--browser")
#     print(browser_name)
#     login_page.login()
#     driver.implicitly_wait(1)
#     catalog_menu.open_catalog()
#     catalog_menu.open_products()
#     products_page.addnew()
#     product_page.productname('New Product')
#     product_page.metatag('New Meta Tag Keyword')
#     product_page.datatab()
#     product_page.modelname('New model')
#     product_page.savebutton()
#     driver.implicitly_wait(3)
#     yield driver.current_url


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
