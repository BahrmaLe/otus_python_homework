"""Module for action with elements"""
from Selenium.Opencart_products_page.models.page import BasePage
from Selenium.Opencart_products_page.models.locator import BaseLocators, LoginPageLocators, AdminPageLocators, \
    ProductPageLocators


class CatalogMenu(BasePage):
    def open_catalog(self):
        """Click on catalog menu"""
        self.driver.find_element(*AdminPageLocators.CATALOG3).click()

    def open_products(self):
        """Click on products menu"""
        self.driver.find_element(*AdminPageLocators.PRODUCTS5).click()


class ProductsPage(BasePage):
    def addnew(self):
        """Click on Add New button"""
        self.driver.find_element(*AdminPageLocators.ADDNEW3).click()

    def addnew2(self):
        """Click on Add New button"""
        self.driver.find_element(*AdminPageLocators.ADDNEW2).click()

    def matchproduct(self):
        self.driver.find_element(*AdminPageLocators.MATCHPRODUCT).click()

    def delete(self):
        """Click on Delete button"""
        self.driver.find_element(*AdminPageLocators.DELETE).click()

    def edit(self):
        """Click on Edit button"""
        self.driver.find_element(*AdminPageLocators.EDIT).click()


class ProductPage(BasePage):
    def productname(self, productname):
        self.driver.find_element(*ProductPageLocators.PRODUCTNAME).send_keys(productname)

    def metatag(self, keywords):
        self.driver.find_element(*ProductPageLocators.METATAG).send_keys(keywords)

    def datatab(self):
        self.driver.find_element(*ProductPageLocators.DATATAB).click()

    def modelname(self, modelname):
        self.driver.find_element(*ProductPageLocators.MODELNAME).send_keys(modelname)

    def savebutton(self):
        self.driver.find_element(*ProductPageLocators.SAVEBUTTON).click()

    def clear_productname(self):
        """Clear password"""
        self._clear_element_(self.driver.find_element(*ProductPageLocators.PRODUCTNAME))

    def clear_metatag(self):
        """Clear password"""
        self._clear_element_(self.driver.find_element(*ProductPageLocators.METATAG))

    def clear_modelname(self):
        """Clear password"""
        self._clear_element_(self.driver.find_element(*ProductPageLocators.MODELNAME))


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

    def alerttext(self):
        """Find alert text message"""
        text = self.driver.find_element(*LoginPageLocators.ALERT)
        return text.text

    def alerticon(self):
        """find icon"""
        self.driver.find_element(*LoginPageLocators.ALERTICON)

    def alert_close_button(self):
        """Close alert"""
        self.driver.find_element(*LoginPageLocators.CLOSEALERT).click()
