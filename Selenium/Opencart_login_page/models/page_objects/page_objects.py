"""Module for action with elements"""
from Selenium.Opencart_login_page.models.page import BasePage
from Selenium.Opencart_login_page.models.locator import BaseLocators, LoginPageLocators


class LoginPage(BasePage):
    """class for action with elements"""
    def set_username(self, username):
        """Set username"""
        self.driver.find_element(*LoginPageLocators.USERNAME3).send_keys(username)

    def set_password(self, password):
        """Set password"""
        self.driver.find_element(*LoginPageLocators.PASSWORD).send_keys(password)

    def forgot_link(self):
        """Click on forgot password"""
        self.driver.find_element(*LoginPageLocators.FORGOT).click()

    def submit(self):
        """Click on Submit button"""
        self.driver.find_element(*BaseLocators.SUBMIT_BUTTON).click()

    def login(self):
        """Click on Submit button"""
        self.driver.find_element(*BaseLocators.PRIMARY_BUTTON).click()

    def clear_password(self):
        """Clear password"""
        self._clear_element_(self.driver.find_element(*LoginPageLocators.PASSWORD))

    def alert(self):
        """Find Alert"""
        self.driver.find_element(*LoginPageLocators.ALERT)

    def alert_close_button(self):
        """Close alert"""
        self.driver.find_element(*LoginPageLocators.CLOSEALERT).click()
