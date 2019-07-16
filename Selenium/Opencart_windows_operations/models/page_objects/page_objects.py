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
        """Click on Product element"""
        product = self._wait_element_(*AdminPageLocators.PRODUCT, delay=10)
        if product:
            product.click()
        return product is not None

    def _accept_delete_alert_(self):
        """Click submit on Alert confirmation pop-up"""
        alert = self._wait_alert_()
        return alert is not None


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
        image_button = self._wait_element_(*ProductPageLocators.IMAGE_BUTTON, delay=10)
        if image_button:
            image_button.click()

    def _click_upload_button_(self):
        """Click on the Upload button"""
        self.driver.find_element(*ProductPageLocators.UPLOAD_BUTTON).click()

    def _close_modal_window_(self):
        """Close modal window"""
        close = self._wait_element_(*ProductPageLocators.CLOSE_MODAL_WINDOW, delay=20)
        if close:
            close.click()
        return close is not None

    def _frame_switch_to_modal_window_(self):
        """Switch to filemanager frame"""
        self.driver.switch_to.frame(self.driver.find_element_by_link_text("Менеджер изображений"))

    def _upload_image_(self, image):
        """Select images and upload it"""
        upload = self._wait_element_(*ProductPageLocators.UPLOAD_BUTTON, delay=20)
        if upload:
            upload.send_keys(image)
        return upload is not None

    def _click_save_button_(self):
        """Click on save button"""
        self.driver.find_element(*ProductPageLocators.SAVE_BUTTON).click()


class ProductManager(NewProduct, ProductPage):
    """Managing product operations"""

    def add_new_product(self, product_name, model_name):
        """Add new product to site"""
        self._click_add_dropdown_()
        self._select_product_dropdown_()
        self._fill_product_name_(product_name)
        self._select_data_tab_()
        self._fill_product_code_(model_name)
        self._click_save_button_()

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
        # self._frame_switch_to_modal_window_()
        self._upload_image_(image)
        self._close_modal_window_()
        self._click_save_button_()


