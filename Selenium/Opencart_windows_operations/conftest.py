# """Fixtures to testing Opencart login page"""
# import os
# import sys
# import pytest
# from selenium import webdriver as WD
#
# from Selenium.Opencart_windows_operations.models.page_objects.page_objects import LoginPage, \
#     ProductPage, ProductsPage, ProductManager, DownloadPage, DownloadManager, CustomMenuDesignPage, CustomMenuDesigner
#
# image = os.path.abspath('C:/Users/60064265/PycharmProjects/Homework/Selenium/Opencart_windows_operations/1.JPG')
#
#
# def pytest_addoption(parser):
#     """Setting base URL Openacart and parametrize command line options for select
#     browsers and set username or password """
#     parser.addoption("--address", action="store", default="http://192.168.56.103/opencart/",
#                      help="Opencart web address")
#     parser.addoption("--address2", action="store", default="http://demo23.opencart.pro/",
#                      help="Opencart web address")
#     parser.addoption("--browser", action="store", default="chrome", help="Browser name")
#     parser.addoption("--username", action="store", default="admin", help="User Name")
#     parser.addoption("--password", action="store", default="admin", help="User Password")
#     parser.addoption("--username2", action="store", default="demo", help="User Name")
#     parser.addoption("--password2", action="store", default="demo", help="User Password")
#     parser.addoption("--iwait", action="store", default="30000", help="Implicitly wait parameter")
#     parser.addoption("--pltimeout", action="store", default="1000", help="Page load timeout")
#     parser.addoption("--productname", action="store", default="New Product", help="Product Name")
#     parser.addoption("--keywords", action="store",
#                      default="New Meta Tag Keyword",
#                      help="Meta Tag Keyword")
#     parser.addoption("--modelname", action="store", default="New model", help="Model Name")
#     parser.addoption("--meta", action="store", default="New meta", help="Meta Tag Title")
#     parser.addoption("--dname", action="store", default="New File for Download", help="Download name")
#     parser.addoption("--filename", action="store", default="New File Name", help="File name")
#     parser.addoption("--maskname", action="store", default="New Mask", help="Mask Name")
#
#
# @pytest.fixture(scope="session", autouse=True)
# def driver(request):
#     """Launching webdriver"""
#     browser_name = request.config.getoption("--browser")
#     print(browser_name)
#     if browser_name == 'firefox':
#         capabilities = WD.DesiredCapabilities.FIREFOX.copy()
#         capabilities['timeouts'] = {'implicit': 300000, 'pageLoad': 300000, 'script': 30000}
#         capabilities['loggingPrefs'] = {'browser': 'ALL', 'client': 'ALL', 'driver': 'ALL',
#                                         'performance': 'ALL', 'server': 'ALL'}
#         capabilities['unexpectedAlertBehaviour'] = 'accept'
#         profile = WD.FirefoxProfile()
#         profile.set_preference('app.update.auto', False)
#         profile.set_preference('app.update.enabled', False)
#         profile.accept_untrusted_certs = True
#         wd = WD.Firefox(firefox_profile=profile, capabilities=capabilities)
#         wd.maximize_window()
#     elif browser_name == 'chrome':
#         capabilities = WD.DesiredCapabilities.CHROME.copy()
#         capabilities['acceptSslCerts'] = True
#         capabilities['acceptInsecureCerts'] = True
#         capabilities['unexpectedAlertBehaviour'] = 'dismiss'
#         wd = WD.Chrome(desired_capabilities=capabilities)
#         wd.fullscreen_window()
#     else:
#         print('Unsupported browser!')
#         sys.exit(1)
#     wd.implicitly_wait((request.config.getoption("--iwait")))
#     wd.set_page_load_timeout((request.config.getoption("--pltimeout")))
#     implicitly_wait = request.config.getoption("--iwait")
#     page_load_timeout = request.config.getoption("--pltimeout")
#     print(implicitly_wait)
#     print(page_load_timeout)
#     yield wd
#     wd.quit()
#
#
# @pytest.fixture(scope="function")
# def open_store_page(driver, request):
#     """Get base URL and attend admin link"""
#     return driver.get("".join([request.config.getoption("--address")]))
#
#
# @pytest.fixture(scope="function")
# def open_opencart_admin_url(driver, request):
#     """Get base URL and attend admin link"""
#     url = 'admin/'
#     return driver.get("".join([request.config.getoption("--address2"), url]))
#
#
# @pytest.fixture(scope="function")
# def login_form_operator(driver, open_opencart_admin_url):
#     """Use class from page objects module for managing elements on the page"""
#     return LoginPage(driver)
#
#
# @pytest.fixture(scope="function")
# def set_login_data(login_form_operator, request, driver):
#     """Open admin login page and login in"""
#     login_form_operator.login(request.config.getoption("--username2"), request.config.getoption("--password2"))
#
#
# @pytest.fixture(scope="function")
# def products_page_opening(driver, open_opencart_admin_url):
#     """Use class from  page objects module for managing elements on the page"""
#     return ProductsPage(driver)
#
#
# @pytest.fixture(scope="function")
# def downloads_page_opening(driver, open_opencart_admin_url):
#     """Use class from  page objects module for managing elements on the page"""
#     return DownloadPage(driver)
#
#
# @pytest.fixture()
# def custom_menu_page_opening(driver, open_opencart_admin_url):
#     """Use"""
#     return CustomMenuDesignPage(driver)
#
#
# @pytest.fixture(scope="function")
# def products_page_operator(driver, open_opencart_admin_url):
#     """Use class from  page objects module for managing elements on the page"""
#     return ProductPage(driver)
#
#
# @pytest.fixture(scope="function")
# def product_manager(driver, open_opencart_admin_url):
#     """Use class from  page objects module for managing elements on the page"""
#     return ProductManager(driver)
#
#
# @pytest.fixture(scope="function")
# def store_manager(driver, open_store_page):
#     """Use class from  page objects module for managing elements on the page"""
#     return ProductManager(driver)
#
#
# @pytest.fixture(scope="function")
# def downloads_manager(driver, open_opencart_admin_url):
#     """Use class from  page objects module for managing elements on the page"""
#     return DownloadManager(driver)
#
#
# @pytest.fixture()
# def custom_menu_designer(driver, open_opencart_admin_url):
#     """USe"""
#     return CustomMenuDesigner(driver)
#
# # @pytest.fixture(scope="function")
# # def add_new_product(driver, set_login_data, products_page_opening, product_manager, request):
# #     product_manager.add_new_product(request.config.getoption("--productname"),
# #                                     request.config.getoption("--modelname"))
#
#
# @pytest.fixture(scope='function')
# def add_product_with_image(driver, set_login_data, products_page_opening, product_manager, request):
#     """Adding new product"""
#     product_manager.add_new_product_with_image(request.config.getoption("--productname"),
#                                                request.config.getoption("--meta"),
#                                                request.config.getoption("--modelname"),
#                                                image)
#
#
# @pytest.fixture(scope='function')
# def find_product_image(driver, open_store_page, store_manager):
#     """Find image"""
#     store_manager.find_product_image("MacBook Pro")
#     src = store_manager.get_image_link()
#     print(type(src))
#     print(src)
#     return src
#
#
# @pytest.fixture(scope='function')
# def upload_file(driver, set_login_data, downloads_page_opening, downloads_manager, request):
#     """Upload file to Downloads page"""
#     downloads_manager.add_file(request.config.getoption("--dname"),
#                                request.config.getoption("--filename"),
#                                request.config.getoption("--maskname"),
#                                image)
#
#
# @pytest.fixture(scope='function')
# def check_uploaded_file(driver, set_login_data, downloads_page_opening, downloads_manager):
#     """Upload file to Downloads page"""
#     return downloads_manager.get_file_name()
#
#
# @pytest.fixture(scope='function')
# def drag_and_drop_custom(driver, set_login_data, custom_menu_page_opening, custom_menu_designer):
#     """Return products list with names"""
#     return custom_menu_designer.drag_and_drop_menu()
