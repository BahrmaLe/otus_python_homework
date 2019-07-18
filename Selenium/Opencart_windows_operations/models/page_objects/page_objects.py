"""Module for action with elements"""
import os

from Selenium.Opencart_windows_operations.models.locator import AdminPageLocators, LoginPageLocators, BaseLocators, \
    ProductPageLocators, ProductsPageLocators, StorePageLocators
from Selenium.Opencart_windows_operations.models.page import BasePage

PRODUCT_IMAGES_PATH = ("duck", "dog", "kitty")


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


class ProductsPage(BasePage):
    """Class for action with elements on products page"""

    def _expand_catalog_menu_(self):
        """Click Add(Plus) button"""
        self.driver.find_element(*AdminPageLocators.CATALOG_MENU).click()

    def _select_products_menu_(self):
        """Click on Product element"""
        product = self._wait_element_(*AdminPageLocators.PRODUCTS_MENU, delay=10)
        if product:
            product.click()
        return product is not None

    def _click_add_new_button_(self):
        """Click Add New button"""
        self.driver.find_element(*ProductsPageLocators.ADD_NEW_BUTTON).click()

    # def _select_upload_dropdown_(self):
    #     """Click on upload element"""
    #     upload = self._wait_element_(*AdminPageLocators.UPLOAD, delay=10)
    #     if upload:
    #         upload.click()
    #     return upload is not None

    def _accept_delete_alert_(self):
        """Click submit on Alert confirmation pop-up"""
        alert = self._wait_alert_()
        return alert is not None

    def _add_images_(self):
        """Adding three images"""
        image = self.driver.find_element(*ProductPageLocators.PRIMARY_IMAGE)
        self.unhide_input(image)
        image.send_keys("".join(["C:/Users/60064265/PycharmProjects/Homework/Selenium/Opencart_windows_operations/", PRODUCT_IMAGES_PATH[0], ".jpg"]))
        self.press_add_image()

        image = self.driver.find_element(*ProductPageLocators.IMAGE1)
        self.unhide_input(image)
        image.send_keys("".join(["C:/Users/60064265/PycharmProjects/Homework/Selenium/Opencart_windows_operations/", PRODUCT_IMAGES_PATH[1], ".jpg"]))
        self.press_add_image()

        image = self.driver.find_element(*ProductPageLocators.IMAGE2)
        self.unhide_input(image)
        image.send_keys("".join(["C:/Users/60064265/PycharmProjects/Homework/Selenium/Opencart_windows_operations/", PRODUCT_IMAGES_PATH[2], ".jpg"]))

    def _unhide_input_(self, element):
        """Making input to be visible"""
        self.driver.execute_script("arguments[0].removeAttribute('type')", element)

    def _press_add_image_(self):
        """Pressing add image button"""
        self.driver.find_element(*ProductPageLocators.ADD_IMAGE).click()


class ProductPage(BasePage):
    """class for action with elements"""

    def _fill_product_name_(self, product_name):
        """Set name of the product"""
        self.driver.find_element(*ProductPageLocators.PRODUCT_NAME).send_keys(product_name)

    def _fill_meta_tag_title_(self, meta_tag):
        """Set Meta Tag"""
        self.driver.find_element(*ProductPageLocators.META_TAG_TITLE).send_keys(meta_tag)

    def _select_data_tab_(self):
        """Click on DATA tab"""
        self.driver.find_element(*ProductPageLocators.DATA_TAB).click()

    def _fill_model_(self, model_name):
        """Set code of the model"""
        self.driver.find_element(*ProductPageLocators.MODEL).send_keys(model_name)

    def _select_images_tab_(self):
        """Click on IMAGES tab"""
        self.driver.find_element(*ProductPageLocators.IMAGE_TAB).click()

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

    def _upload_image_(self, image):
        """Select images and upload it"""
        upload = self._wait_element_(*ProductPageLocators.UPLOAD_BUTTON, delay=10)
        if upload:
            upload.send_keys(image)
        return upload is not None

    def _clear_filemanager_(self):
        """Select images and upload it"""
        filemanager = self._wait_element_(*ProductPageLocators.UPLOAD_BUTTON, delay=20)
        if filemanager:
            filemanager.clear()
        return filemanager is not None

    def _accept_image_upload_alert_(self):
        """Click submit on Alert confirmation pop-up"""
        alert = self._wait_alert_()
        return alert is not None

    def _close_modal_window_(self):
        """Close modal window"""
        close = self._wait_element_(*ProductPageLocators.MODAL_WINDOW_CLOSE_BUTTON, delay=20)
        if close:
            close.click()
        return close is not None

    # def _frame_switch_to_modal_window_(self):
    #     """Switch to filemanager frame"""
    #     self.driver.switch_to.frame(self.driver.find_element_by_link_text("Менеджер изображений"))

    def _click_save_button_(self):
        """Click on save button"""
        self.driver.find_element(*ProductPageLocators.SAVE_BUTTON).click()


# class DownloadPage(BasePage):
#     """Managing page for Files to downloading"""
#
#     def _fill_file_desc_ru_(self, rudesc):
#         """Fill the description for ru users"""
#         self.driver.find_element(*DownloadPageLocators.DOWNLOAD_DESCRIPTION_RU).send_keys(rudesc)
#
#     def _fill_file_desc_en_(self, endesc):
#         """Fill the description for en users"""
#         self.driver.find_element(*DownloadPageLocators.DOWNLOAD_DESCRIPTION_EN).send_keys(endesc)
#
#     def _fill_file_name_(self, filename):
#         """Fill the file name"""
#         self.driver.find_element(*DownloadPageLocators.FILE_NAME).send_keys(filename)
#
#     def _upload_file_(self, file):
#         """Upload file through file manager"""
#         upload = self._wait_element_(*DownloadPageLocators.UPLOAD_BUTTON, delay=10)
#         if upload:
#             upload.send_keys(file)
#         return upload is not None
#
#     def _fill_mask_(self, maskname):
#         """Fill the mask field"""
#         self.driver.find_element(*DownloadPageLocators.MASK).send_keys(maskname)
#
#     def _click_submit_(self):
#         """Save uploaded files"""
#         self.driver.find_element(*DownloadPageLocators.SUBMIT_BUTTON).click()


class StorePage(BasePage):

    def _click_on_search_(self):
        search = self._wait_element_(*StorePageLocators.SEARCH_FIELD, delay=10)
        if search:
            search.click()
        return search is not None

    def _fill_search_(self, product_name):
        search = self._wait_element_(*StorePageLocators.SEARCH_FIELD, delay=10)
        if search:
            search.send_keys(product_name)
        return search is not None

    def _click_search_(self):
        self.driver.find_element(*StorePageLocators.SEARCH_BUTTON).click()

    def _return_image_name_(self):
        image_name = self.driver.find_element(*StorePageLocators.IMAGE_NAME)
        if image_name:
            print(image_name.get_attribute("src"))
            image_name_string = str(image_name.get_attribute("src"))
            print(type(image_name_string))
            return image_name_string


class ProductManager(ProductsPage, ProductPage, StorePage):
    """Managing product operations"""

    def add_new_product(self, product_name, meta_tag, model_name):
        """Add new product to site"""
        self._expand_catalog_menu_()
        self._select_products_menu_()
        self._click_add_new_button_()
        self._fill_product_name_(product_name)
        self._fill_meta_tag_title_(meta_tag)
        self._select_data_tab_()
        self._fill_model_(model_name)
        self._click_save_button_()

    def add_new_product_with_image(self, product_name, meta_tag, model_name, image):
        """Add new product to site"""
        self._expand_catalog_menu_()
        self._select_products_menu_()
        self._click_add_new_button_()
        self._fill_product_name_(product_name)
        self._fill_meta_tag_title_(meta_tag)
        self._select_data_tab_()
        self._fill_model_(model_name)
        self._select_images_tab_()
        self._click_thumb_image_()
        self._click_image_button_()
        # self._clear_filemanager_()
        # self._click_upload_button_()
        self._upload_image_(image)
        self._accept_image_upload_alert_()
        self._close_modal_window_()
        self._click_save_button_()

    def add_three_images(self, product_name, meta_tag, model_name):
        self._expand_catalog_menu_()
        self._select_products_menu_()
        self._click_add_new_button_()
        self._fill_product_name_(product_name)
        self._fill_meta_tag_title_(meta_tag)
        self._select_data_tab_()
        self._fill_model_(model_name)
        self._select_images_tab_()
        self._add_images_()
        self._click_save_button_()

    def find_product_image(self, product_name):
        self._click_on_search_()
        self._fill_search_(product_name)
        self._click_search_()

    def get_image_link(self):
        return self._return_image_name_()





# class DownloadManager(DownloadPage):
#     """Managing files for downloading"""
#
#     def add_file(self, rudesc, endesc, filename, maskname, file):
#         """Upload file"""
#         self._click_add_dropdown_()
#         self._select_upload_dropdown_()
#         self._fill_file_desc_ru_(rudesc)
#         self._fill_file_desc_en_(endesc)
#         self._fill_file_name_(filename)
#         self._fill_mask_(maskname)
#         self._upload_file_(file)
#         self._click_submit_()
