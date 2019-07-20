"""Module for action with elements"""
from selenium.webdriver import ActionChains

from Selenium.Opencart_windows_operations.models.locator import AdminPageLocators, LoginPageLocators, BaseLocators, \
    ProductPageLocators, ProductsPageLocators, StorePageLocators, DownloadPageLocators, CustomMenuLocators
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
        """Click on Products element"""
        product = self._wait_element_(*AdminPageLocators.PRODUCTS_MENU, delay=10)
        if product:
            product.click()
        return product is not None

    def _select_downloads_menu_(self):
        """Click on Downloads menu"""
        download = self._wait_element_(*AdminPageLocators.DOWNLOADS_MENU, delay=10)
        if download:
            download.click()
        return download is not None

    def _open_design_custom_menu_(self):
        """OPen"""
        design_menu = self.driver.find_element(*AdminPageLocators.DESIGN_MENU)
        if design_menu:
            ActionChains(self.driver).move_to_element(design_menu).perform()
            custom_menu = self._wait_element_(*AdminPageLocators.CUSTOM_MENU, delay=10)
            if custom_menu:
                custom_menu.click()
            return custom_menu is not None

        """ def setUp(self):
        self.webdriver = webdriver.Ie()
        self.mouse = webdriver.ActionChains(self.webdriver)
        self.webdriver.get("http://foo")

    def test_webdriver(self):
        mouse = self.mouse
        wd = self.webdriver
        wd.implicitly_wait(10)
        element = wd.find_element_by_xpath("//div[@title='Create Page']")
        mouse.move_to_element(element).perform()"""

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
        self._unhide_input_(image)
        image.send_keys("".join(["C:/Users/60064265/PycharmProjects/Homework/Selenium/Opencart_windows_operations/", PRODUCT_IMAGES_PATH[0], ".jpg"]))
        self._press_add_image_()

        image = self.driver.find_element(*ProductPageLocators.IMAGE1)
        self._unhide_input_(image)
        image.send_keys("".join(["C:/Users/60064265/PycharmProjects/Homework/Selenium/Opencart_windows_operations/", PRODUCT_IMAGES_PATH[1], ".jpg"]))
        self._press_add_image_()

        image = self.driver.find_element(*ProductPageLocators.IMAGE2)
        self._unhide_input_(image)
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


class DownloadPage(BasePage):
    """Managing page for Files to downloading"""

    def _fill_download_name_(self, dname):
        """Fill the description for ru users"""
        self.driver.find_element(*DownloadPageLocators.DOWNLOAD_NAME).send_keys(dname)

    def _fill_file_name_(self, filename):
        """Fill the file name"""
        self.driver.find_element(*DownloadPageLocators.FILE_NAME).send_keys(filename)

    def _upload_file_(self, file):
        """Upload file through file manager"""
        upload = self._wait_element_(*DownloadPageLocators.UPLOAD_BUTTON, delay=10)
        if upload:
            upload.send_keys(file)
        return upload is not None

    def _fill_mask_(self, maskname):
        """Fill the mask field"""
        self.driver.find_element(*DownloadPageLocators.MASK).send_keys(maskname)

    def _return_file_name_(self):
        """Get File name"""
        file_name = self.driver.find_element(*DownloadPageLocators.FILE_NAME_TITLE)
        if file_name:
            print(file_name.text())
            file_name_string = str(file_name.text())
            print(type(file_name_string))
            return file_name_string

    def _get_files_list_(self):
        """Return current list of products"""
        files = self._wait_element_(*DownloadPageLocators.ALL_FILES, delay=10)
        if files:
            files_elements = files.find_elements_by_tag_name("tr")
            file_list = set()
            for element in files_elements:
                file_name = element.find_elements_by_tag_name("td")[1]
                file_list.add(file_name.text)
            print(file_list)
            return file_list


class StorePage(BasePage):
    """Store"""

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


class CustomMenuDesignPage(BasePage):
    """Design"""

    def _find_source_1_(self):
        """Find"""
        self.driver.find_element(*CustomMenuLocators.CUSTOM_MENU_ELEMENT1)

    def _find_source_2_(self):
        """Find"""
        self.driver.find_element(*CustomMenuLocators.CUSTOM_MENU_ELEMENT1)

    def _click_submit_button_(self):
        """Submit"""
        self.driver.find_element(*CustomMenuLocators.SUBMIT_BUTTON).click()


class CustomMenuDesigner(ProductsPage, CustomMenuDesignPage):
    """Class"""

    def drag_and_drop_menu(self):
        """Drug"""
        self._open_design_custom_menu_()
        source1 = self.driver.find_element(*CustomMenuLocators.CUSTOM_MENU_ELEMENT3)
        source2 = self.driver.find_element(*CustomMenuLocators.CUSTOM_MENU_ELEMENT4)
        ActionChains(self.driver).drag_and_drop(source1, source2).perform()
        self._click_submit_button_()


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
        """Get image src attribute (link)"""
        return self._return_image_name_()


class DownloadManager(ProductsPage, ProductPage, DownloadPage):
    """Managing files for downloading"""

    def add_file(self, dname, filename, maskname, file):
        """Upload file"""
        self._expand_catalog_menu_()
        self._select_downloads_menu_()
        self._click_add_new_button_()
        self._fill_download_name_(dname)
        self._fill_file_name_(filename)
        self._fill_mask_(maskname)
        self._upload_file_(file)
        self._accept_image_upload_alert_()
        self._click_save_button_()

    def get_file_name(self):
        """Get file name"""
        self._expand_catalog_menu_()
        self._select_downloads_menu_()
        return self._get_files_list_()

