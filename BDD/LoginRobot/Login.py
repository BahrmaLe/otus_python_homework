from robot.api.deco import keyword
import sys

# from BDD.LoginRobot.LoginAdmin import LoginAdmin
# from BDD.LoginRobot.LoginUser import LoginUser
from BDD.LoginRobot.LoginAdmin import LoginAdmin
from BDD.LoginRobot.LoginUser import LoginUser
# sys.path.remove('')
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

