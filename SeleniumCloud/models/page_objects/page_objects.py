"""Module for action with elements"""
from Selenium.Opencart_products_page.log.log import TestListener
from Selenium.Opencart_products_page.models.page import BasePage
from Selenium.Opencart_products_page.models.locator import BaseLocators, LoginPageLocators, \
    AdminPageLocators, ProductPageLocators


class CatalogMenu(BasePage):
    """class for action with elements"""

    def _expand_catalog_menu_item(self):
        """Click on catalog menu item"""
        self.driver.find_element(*AdminPageLocators.CATALOG3).click()

    def _open_products_menu_item(self):
        """Click on products menu item"""
        products = self._wait_element_(*AdminPageLocators.PRODUCTS5, delay=10)
        if products:
            products.click()
        return products is not None

    def open_products_page(self):
        """Open product managements page"""
        self._expand_catalog_menu_item()
        self._open_products_menu_item()


class ProductsPage(BasePage):
    """Class for action with elements on products page"""

    def _click_add_new_button_(self):
        """Click on Add New button"""
        self.driver.find_element(*AdminPageLocators.ADDNEW3).click()

    def _click_add_new_button2_(self):
        """Click on Add New button"""
        self.driver.find_element(*AdminPageLocators.ADDNEW2).click()

    def _match_product_(self):
        """Click for flag checkbox forward the product"""
        self.driver.find_element(*AdminPageLocators.MATCHPRODUCT).click()

    def _click_delete_button_(self):
        """Click on Delete button"""
        self.driver.find_element(*AdminPageLocators.DELETE).click()

    def _accept_delete_alert_(self):
        """Click submit on Alert confirmation pop-up"""
        alert = self._wait_alert_()
        return alert is not None

    def _click_edit_button_(self):
        """Click on Edit button"""
        self.driver.find_element(*AdminPageLocators.EDIT).click()

    def _get_product_list_(self):
        """Return current list of products"""
        products = self._wait_element_(*AdminPageLocators.ALLPRODUCTS, delay=10)
        if products:
            products_elements = products.find_elements_by_tag_name("tr")
            product_list = set()
            for element in products_elements:
                product_name = element.find_elements_by_tag_name("td")[2]
                product_list.add(product_name.text)
            print(product_list)
            return product_list

    def delete_product(self):
        """Delete selected product"""
        self._match_product_()
        self._click_delete_button_()
        self._accept_delete_alert_()

    def all_products_list(self):
        """Show list of all products on the site"""
        return self._get_product_list_()


class ProductPage(BasePage):
    """class for action with elements"""

    def _set_product_name_(self, productname):
        """Fill the product name field"""
        self.driver.find_element(*ProductPageLocators.PRODUCTNAME).send_keys(productname)

    def _set_meta_tag_(self, keywords):
        """Fill the metatag field"""
        self.driver.find_element(*ProductPageLocators.METATAG).send_keys(keywords)

    def _click_data_tab_(self):
        """Go o Data tab"""
        self.driver.find_element(*ProductPageLocators.DATATAB).click()

    def _set_model_name_(self, modelname):
        """Fill the model field"""
        self.driver.find_element(*ProductPageLocators.MODELNAME).send_keys(modelname)

    def _click_save_button_(self):
        """Click on save button"""
        self.driver.find_element(*ProductPageLocators.SAVEBUTTON).click()

    def _clear_product_name_(self):
        """Clear password"""
        self._clear_element_(self.driver.find_element(*ProductPageLocators.PRODUCTNAME))

    def _clear_meta_tag_(self):
        """Clear metatag"""
        self._clear_element_(self.driver.find_element(*ProductPageLocators.METATAG))

    def _clear_model_name_(self):
        """Clear model name"""
        self._clear_element_(self.driver.find_element(*ProductPageLocators.MODELNAME))


class LoginPage(BasePage):
    """class for action with elements"""

    def _set_username_(self, username):
        """Set username"""
        self.driver.find_element(*LoginPageLocators.USERNAME3).send_keys(username)

    def _set_password_(self, password):
        """Set password"""
        self.driver.find_element(*LoginPageLocators.PASSWORD).send_keys(password)

    def _forgot_link_(self):
        """Click on forgot password"""
        self.driver.find_element(*LoginPageLocators.FORGOT).click()

    def _click_submit_button_(self):
        """Click on Submit button"""
        self.driver.find_element(*BaseLocators.SUBMIT_BUTTON).click()

    def _login_button_(self):
        """Click on Submit button"""
        self.driver.find_element(*BaseLocators.PRIMARY_BUTTON).click()

    def _clear_password_(self):
        """Clear password"""
        self._clear_element_(self.driver.find_element(*LoginPageLocators.PASSWORD))

    def _incorrectly_login_alert_(self):
        """Find Alert"""
        self.driver.find_element(*LoginPageLocators.ALERT)

    def _incorrectly_login_alert_message_(self):
        """Find alert text message"""
        text = self.driver.find_element(*LoginPageLocators.ALERT)
        return text.text

    def _incorrectly_login_alert_icon_(self):
        """find icon"""
        self.driver.find_element(*LoginPageLocators.ALERTICON)

    def _incorrectly_login_alert_close_button_(self):
        """Close alert"""
        self.driver.find_element(*LoginPageLocators.CLOSEALERT).click()

    def login(self, username, password):
        """Open admin page and login in"""
        self._set_username_(username)
        self._set_password_(password)
        self._click_submit_button_()


class ProductManager(ProductsPage, ProductPage, TestListener):
    """Managing product operations"""

    def add_new_product(self, productname, keywords, modelname):
        """Add new product to site"""
        self._click_add_new_button2_()
        self._set_product_name_(productname)
        self._set_meta_tag_(keywords)
        self._click_data_tab_()
        self._set_model_name_(modelname)
        self._click_save_button_()

    def edit_product(self, productname, keywords, modelname):
        """Edit created product"""
        self._click_edit_button_()
        self._clear_product_name_()
        self._set_product_name_(productname)
        self._clear_meta_tag_()
        self._set_meta_tag_(keywords)
        self._click_data_tab_()
        self._clear_model_name_()
        self._set_model_name_(modelname)
        self._click_save_button_()
