"""Fixtures to testing Opencart login page"""
import sys
import pytest
from selenium import webdriver
from Selenium.Opencart_products_page.models.page_objects.page_objects import LoginPage, \
    CatalogMenu, ProductsPage, ProductPage


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
    """Set username/password by command line parameters and do login"""
    login_page.set_username(request.config.getoption("--username"))
    login_page.set_password(request.config.getoption("--password"))
    login_page.submit()


@pytest.fixture(scope="function")
def catalog_menu(driver, open_login_page):
    """Use class from  page objects module for managing elements on the page"""
    return CatalogMenu(driver)


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
    """Use locators for opening catalog menu - products"""
    catalog_menu.open_catalog()
    catalog_menu.open_products()


@pytest.fixture(scope='function')
def add_product(driver, login_action, open_products_page, products_page, product_card):
    """Adding new product"""
    products_page.addnew2()
    product_card.productname('New Product')
    product_card.metatag('New Meta Tag Keyword')
    product_card.datatab()
    product_card.modelname('New model')
    product_card.savebutton()
    driver.back()
    driver.back()
    driver.refresh()


@pytest.fixture(scope='function')
def edit_product(driver, login_action, open_products_page, products_page, product_card):
    """Editing product"""
    products_page.edit()
    product_card.clear_productname()
    product_card.productname('Edited Product')
    product_card.clear_metatag()
    product_card.metatag('Edited Meta Tag Keyword')
    product_card.datatab()
    product_card.clear_modelname()
    product_card.modelname('Edited model')
    product_card.savebutton()


@pytest.mark.usefixtures("login_action", "open_products_page")
@pytest.fixture(scope='function')
def delete_product(driver, products_page):
    """Matching and deleting product"""
    products_page.matchproduct()
    products_page.delete()
    products_page.alert()
    driver.refresh()


@pytest.fixture(scope='function')
def products_list(driver, open_login_page, login_action, open_products_page, products_page):
    """Return products list with names"""
    return products_page.products_list()


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
