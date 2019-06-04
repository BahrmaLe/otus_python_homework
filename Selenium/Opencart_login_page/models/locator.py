"""Locators for opencart login page"""
from selenium.webdriver.common.by import By


class BaseLocators(object):
    """Base locator (submit button)"""
    PRIMARY_BUTTON = (By.CLASS_NAME, "btn.btn-primary")
    SUBMIT_BUTTON = (By.XPATH, "//*[@type='submit']")


class LoginPageLocators(object):
    """Login page locators (Username, Password, Alert, Forgot password, Close alert button)"""
    USERNAME = (By.ID, "input-username")
    USERNAME2 = (By.NAME, "username")
    USERNAME3 = (By.CSS_SELECTOR, "#input-username")
    USERNAME4 = (By.XPATH, "//*[@placeholder='Username']")
    PASSWORD = (By.ID, "input-password")
    ERROR = (By.CLASS_NAME, "alert.alert-danger.alert-dismissible")
    FORGOT = (By.LINK_TEXT, "Forgotten Password")
    ALERT = (By.CSS_SELECTOR, "div.alert.alert-danger.alert-dismissible")
    ALERTICON = (By.CSS_SELECTOR, "i.fa.fa-exclamation-circle")
    CLOSEALERT = (By.CLASS_NAME, 'close')
