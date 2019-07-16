"""Locators for opencart login page"""
from selenium.webdriver.common.by import By


class AdminPageLocators(object):
    """Admin page locators"""
    DROPDOWN = (By.XPATH, '//a[@class="dropdown-toggle"]')
    PRODUCT = (By.LINK_TEXT, 'Товар')


class ProductPageLocators(object):
    """Locators for product item"""
    PRODUCT_NAME = (By.XPATH, '//*[@id="input-name1"]')
    DATA_TAB = (By.XPATH, '//*[@href="#tab-data"]')
    PRODUCT_CODE = (By.XPATH, '//*[@id="input-model"]')
    IMAGES_TAB = (By.XPATH, '//*[@href="#tab-image"]')
    THUMB_IMAGE = (By.ID, 'thumb-image')
    IMAGE_BUTTON = (By.ID, 'button-image')
    UPLOAD_BUTTON = (By.ID, 'button-upload')
    CLOSE_MODAL_WINDOW = (By.CSS_SELECTOR, '#filemanager > div:nth-child(1) > div:nth-child(1) > button:nth-child(1)')
    SAVE_BUTTON = (By.XPATH, '//*[@id="content"]/div[1]/div/div/button/i')
    FILE_MANAGER = (By.ID, 'filemanager')


class BaseLocators(object):
    """Base locator (submit button)"""
    PRIMARY_BUTTON = (By.TAG_NAME, "button")
    SUBMIT_BUTTON = (By.XPATH, "//*[@type='submit']")


class LoginPageLocators(object):
    """Login page locators (Username, Password, Alert, Forgot password, Close alert button)"""
    USERNAME = (By.ID, "input-username")
    PASSWORD = (By.ID, "input-password")

