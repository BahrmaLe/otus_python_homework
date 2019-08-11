from robot.api.deco import keyword
from selenium import webdriver
import sys
sys.path.remove('')
sys.path.append('.')


class LoginAdmin:

    def __init__(self):
        self.options = webdriver.ChromeOptions()
        self.driver = webdriver.Chrome(chrome_options=self.options)

    @keyword(name="Open Browser To Login Page")
    def open_login_admin_page(self):
        self.driver.get("http://demo23.opencart.pro/admin/")

    @keyword(name="Input Username")
    def enter_admin_name(self):
        self.driver.find_element_by_id("input-username").send_keys("demo")

    @keyword(name="Input Password")
    def enter_admin_password(self):
        self.driver.find_element_by_id("input-password").send_keys("demo")

    @keyword(name="Submit Credentials")
    def submit_admin_login(self):
        self.driver.find_element_by_xpath("//*button[@type='submit']").click()

    @keyword(name="Welcome Page Should Be Open")
    def assert_admin_page(self):
        cur_url = self.driver.current_url()
        assert "dashboard" in cur_url

    def open_admin_panel(self):
        self.driver.find_element_by_id("button-menu").click()

    @keyword(name="Close Browser")
    def quit_browser_admin(self):
        self.driver.quit()


class Login(LoginAdmin):
    """
    Class combining admin and customer login test for OpenCart
    """

    @keyword(name="Login Admin")
    def login_admin(self):
        self.open_login_admin_page()
        self.enter_admin_name()
        self.enter_admin_password()
        self.submit_admin_login()
        self.open_admin_panel()
        self.quit_browser_admin()
