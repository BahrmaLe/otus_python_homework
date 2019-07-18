"""Locators for opencart login page"""
from selenium.webdriver.common.by import By


class StorePageLocators(object):
    SEARCH_FIELD = (By.CSS_SELECTOR, '.form-control')
    SEARCH_BUTTON = (By.XPATH, '//*[@class="btn btn-default btn-lg"]')
    IMAGE_NAME = (By.XPATH, '//*[@class="img-responsive"]')


class AdminPageLocators(object):
    """Admin page locators"""
    # DROPDOWN = (By.XPATH, '//a[@class="dropdown-toggle"]')
    # PRODUCT = (By.LINK_TEXT, 'Товар')
    # UPLOAD = (By.LINK_TEXT, 'Загрузку')
    CATALOG_MENU = (By.XPATH, '//*[@id="menu-catalog"]')
    PRODUCTS_MENU = (By.LINK_TEXT, 'Products')


class ProductsPageLocators(object):
    """Products page locators"""
    ADD_NEW_BUTTON = (By.XPATH, '//*[@class="btn btn-primary"]')


class ProductPageLocators(object):
    """Locators for product item"""
    PRODUCT_NAME = (By.XPATH, '//*[@id="input-name1"]')
    META_TAG_TITLE = (By.XPATH, '//*[@id="input-meta-title1"]')
    DATA_TAB = (By.XPATH, '//*[@href="#tab-data"]')
    MODEL = (By.XPATH, '//*[@id="input-model"]')
    # PRODUCT_CODE = (By.XPATH, '//*[@id="input-model"]')
    IMAGE_TAB = (By.XPATH, '//*[@href="#tab-image"]')
    THUMB_IMAGE = (By.ID, 'thumb-image')
    IMAGE_BUTTON = (By.ID, 'button-image')
    UPLOAD_BUTTON = (By.CSS_SELECTOR, '#button-upload')
    PRIMARY_IMAGE = (By.ID, "input-image")
    IMAGE1 = (By.ID, "input-image0")
    IMAGE2 = (By.ID, "input-image1")
    ADD_IMAGE = (By.CSS_SELECTOR, "[data-original-title=\"Add Image\"]")
    MODAL_WINDOW_CLOSE_BUTTON = (By.CSS_SELECTOR, '#filemanager > div:nth-child(1) > div:nth-child(1) > button:nth-child(1)')
    # MODAL_WINDOW_CLOSE_BUTTON = (By.CSS_SELECTOR, '#filemanager > div:nth-child(1) > div:nth-child(1) > button:nth-child(1)')
    SAVE_BUTTON = (By.XPATH, '//*[@class="btn btn-primary"]')
    # FILE_MANAGER = (By.ID, 'filemanager')


# class DownloadPageLocators(object):
#     """Download page locators"""
#     DOWNLOAD_DESCRIPTION_RU =
#     DOWNLOAD_DESCRIPTION_EN =
#     FILE_NAME =
#     MASK =
#     UPLOAD_BUTTON =
#     SUBMIT_BUTTON =


class BaseLocators(object):
    """Base locator (submit button)"""
    PRIMARY_BUTTON = (By.TAG_NAME, "button")
    SUBMIT_BUTTON = (By.XPATH, "//*[@type='submit']")


class LoginPageLocators(object):
    """Login page locators (Username, Password, Alert, Forgot password, Close alert button)"""
    USERNAME = (By.ID, "input-username")
    PASSWORD = (By.ID, "input-password")

