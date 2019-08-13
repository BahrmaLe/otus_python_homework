from robot.api.deco import keyword
import sys

from BDD.LoginRobot.LoginAdmin import LoginAdmin
from BDD.LoginRobot.LoginUser import LoginUser
sys.path.append('Homework/BDD')


class Login(LoginAdmin, LoginUser):
    """
    Class combining admin and customer login test for OpenCart
    """

    @keyword(name="Login Admin")
    def login_admin(self):
        self.open_login_admin_page()
        self.input_admin_name()
        self.input_password()
        self.submit_admin_login()
        self.open_admin_panel()
        self.quit_browser_admin()

    @keyword(name="Login User")
    def login_user(self):
        self.open_login_user_page()
        # self.select_login()
        self.input_email()
        self.input_user_password()
        self.submit_user_login()
        self.open_user_home()
        self.quit_browser_user()

    @keyword(name="Admin page is opened")
    def open_admin(self):
        self.admin_page_assert()

    @keyword(name="Open Category")
    def login_admin(self):
        self.open_login_admin_page()
        self.input_admin_name()
        self.input_password()
        self.submit_admin_login()
        self.expand_catalog()
        self.open_category()
        self.quit_browser_admin()

    @keyword(name="Category Page is opened")
    def category_assert(self):
        self.category_page_assert()

    @keyword(name="Open Menu Designer")
    def login_admin(self):
        self.open_login_admin_page()
        self.input_admin_name()
        self.input_password()
        self.submit_admin_login()
        self.expand_design()
        self.open_designer()
        self.quit_browser_admin()

    @keyword(name="Menu Designer is opened")
    def design_assert(self):
        self.design_page_assert()

    @keyword(name="Open Settings")
    def login_admin(self):
        self.open_login_admin_page()
        self.input_admin_name()
        self.input_password()
        self.submit_admin_login()
        self.expand_system()
        self.open_settings_menu()
        self.quit_browser_admin()

    @keyword(name="Settings is opened")
    def settings_assert(self):
        self.settings_page_assert()

    @keyword(name="Open orders")
    def login_admin(self):
        self.open_login_admin_page()
        self.input_admin_name()
        self.input_password()
        self.submit_admin_login()
        self.expand_reports()
        self.open_sells_menu()
        self.open_orders_menu()
        self.quit_browser_admin()

    @keyword(name="Orders is opened")
    def reports_assert(self):
        self.reports_page_assert()

