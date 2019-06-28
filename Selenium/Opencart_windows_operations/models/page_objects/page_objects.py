"""Module for action with elements"""
from Selenium.Opencart_windows_operations.models.locator import AdminPageLocators, LoginPageLocators, BaseLocators, \
    ProductPageLocators
from Selenium.Opencart_windows_operations.models.page import BasePage


class LoginPage(BasePage):
    """class for action with elements"""

    def _set_username_(self, username):
        """Set username"""
        self.driver.find_element(*LoginPageLocators.USERNAME).send_keys(username)

    def _set_password_(self, password):
        """Set password"""
        self.driver.find_element(*LoginPageLocators.PASSWORD).send_keys(password)

    def _click_submit_button_(self):
        """Click on Submit button"""
        self.driver.find_element(*BaseLocators.SUBMIT_BUTTON).click()

    def _login_button_(self):
        """Click on Submit button"""
        self.driver.find_element(*BaseLocators.PRIMARY_BUTTON).click()

    def _clear_password_(self):
        """Clear password"""
        self._clear_element_(self.driver.find_element(*LoginPageLocators.PASSWORD))

    def login(self, username, password):
        """Open admin page and login in"""
        self._set_username_(username)
        self._set_password_(password)
        self._click_submit_button_()


# class CatalogMenu(BasePage):
#     """class for action with elements"""
#
#     def _expand_catalog_menu_item(self):
#         """Click on catalog menu item"""
#         self.driver.find_element(*AdminPageLocators.CATALOG3).click()
#
#     def _open_products_menu_item(self):
#         """Click on products menu item"""
#         products = self._wait_element_(*AdminPageLocators.PRODUCTS5, delay=10)
#         if products:
#             products.click()
#         return products is not None
#
#     def open_products_page(self):
#         """Open product managements page"""
#         self._expand_catalog_menu_item()
#         self._open_products_menu_item()


class NewProduct(BasePage):
    """Class for action with elements on products page"""

    def _click_add_dropdown_(self):
        self.driver.find_element(*AdminPageLocators.DROPDOWN).click()

    def _select_product_dropdown_(self):
        self.driver.find_element(AdminPageLocators.PRODUCT).click()

    def _accept_delete_alert_(self):
        """Click submit on Alert confirmation pop-up"""
        alert = self._wait_alert_()
        return alert is not None

    # def _click_add_new_button_(self):
    #     """Click on Add New button"""
    #     self.driver.find_element(*AdminPageLocators.ADDNEW3).click()
    #
    # def _click_add_new_button2_(self):
    #     """Click on Add New button"""
    #     self.driver.find_element(*AdminPageLocators.ADDNEW2).click()
    #
    # def _match_product_(self):
    #     """Click for flag checkbox forward the product"""
    #     self.driver.find_element(*AdminPageLocators.MATCHPRODUCT).click()
    #
    # def _click_delete_button_(self):
    #     """Click on Delete button"""
    #     self.driver.find_element(*AdminPageLocators.DELETE).click()
    # def _click_edit_button_(self):
    #     """Click on Edit button"""
    #     self.driver.find_element(*AdminPageLocators.EDIT).click()

    # def _get_product_list_(self):
    #     """Return current list of products"""
    #     products = self._wait_element_(*AdminPageLocators.ALLPRODUCTS, delay=10)
    #     if products:
    #         products_elements = products.find_elements_by_tag_name("tr")
    #         product_list = set()
    #         for element in products_elements:
    #             product_name = element.find_elements_by_tag_name("td")[2]
    #             product_list.add(product_name.text)
    #         print(product_list)
    #         return product_list
    # def delete_product(self):
    #     """Delete selected product"""
    #     self._match_product_()
    #     self._click_delete_button_()
    #     self._accept_delete_alert_()
    #
    # def all_products_list(self):
    #     """Show list of all products on the site"""
    #     return self._get_product_list_()


class ProductPage(BasePage):
    """class for action with elements"""

    def _fill_product_name_(self, product_name):
        """Set name of the product"""
        self.driver.find_element(*ProductPageLocators.PRODUCT_NAME).send_keys(product_name)

    def _select_data_tab_(self):
        """Click on DATA tab"""
        self.driver.find_element(*ProductPageLocators.DATA_TAB).click()

    def _fill_product_code_(self, model_name):
        """Set code of the model"""
        self.driver.find_element(*ProductPageLocators.PRODUCT_CODE).send_keys(model_name)

    def _select_images_tab_(self):
        """Click on IMAGES tab"""
        self.driver.find_element(*ProductPageLocators.IMAGES_TAB).click()

    def _click_thumb_image_(self):
        """CLick on thumb image icon"""
        self.driver.find_element(*ProductPageLocators.THUMB_IMAGE).click()

    def _click_image_button_(self):
        """Click on Edit Image icon/button"""
        self.driver.find_element(*ProductPageLocators.IMAGE_BUTTON).click()

    def _click_upload_button_(self):
        """Click on the Upload button"""
        self.driver.find_element(*ProductPageLocators.UPLOAD_BUTTON).click()

    def _upload_image_(self, image):
        """Select images and upload it"""
        self.driver.find_element(*ProductPageLocators.UPLOAD_BUTTON).send_keys(image)

    def _click_save_button_(self):
        """Click on save button"""
        self.driver.find_element(*ProductPageLocators.SAVE_BUTTON).click()


    # def _set_product_name_(self, productname):
    #     """Fill the product name field"""
    #     self.driver.find_element(*ProductPageLocators.PRODUCTNAME).send_keys(productname)
    #
    # def _set_meta_tag_(self, keywords):
    #     """Fill the metatag field"""
    #     self.driver.find_element(*ProductPageLocators.METATAG).send_keys(keywords)
    #
    # def _click_data_tab_(self):
    #     """Go o Data tab"""
    #     self.driver.find_element(*ProductPageLocators.DATATAB).click()
    #
    # def _set_model_name_(self, modelname):
    #     """Fill the model field"""
    #     self.driver.find_element(*ProductPageLocators.MODELNAME).send_keys(modelname)
    #
    #
    # def _clear_product_name_(self):
    #     """Clear password"""
    #     self._clear_element_(self.driver.find_element(*ProductPageLocators.PRODUCTNAME))
    #
    # def _clear_meta_tag_(self):
    #     """Clear metatag"""
    #     self._clear_element_(self.driver.find_element(*ProductPageLocators.METATAG))
    #
    # def _clear_model_name_(self):
    #     """Clear model name"""
    #     self._clear_element_(self.driver.find_element(*ProductPageLocators.MODELNAME))


class ProductManager(NewProduct, ProductPage):
    """Managing product operations"""

    def add_new_product_with_images(self, product_name, model_name, image):
        """Add new product to site"""
        self._click_add_dropdown_()
        self._select_product_dropdown_()
        self._fill_product_name_(product_name)
        self._select_data_tab_()
        self._fill_product_code_(model_name)
        self._select_images_tab_()
        self._click_thumb_image_()
        self._click_image_button_()
        self._upload_image_(image)
        self._click_save_button_()


