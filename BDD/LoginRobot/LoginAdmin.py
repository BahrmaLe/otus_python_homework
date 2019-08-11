from selenium import webdriver


class LoginAdmin():

    def __init__(self):
        self.options = webdriver.ChromeOptions()
        self.driver = webdriver.Chrome(chrome_options=self.options)

    def open_login_admin_page(self):
        self.driver.get("http://demo23.opencart.pro/admin/")

    def input_admin_name(self):
        self.driver.find_element_by_id("input-username").send_keys("demo")

    def input_password(self):
        self.driver.find_element_by_id("input-password").send_keys("demo")

    def submit_admin_login(self):
        self.driver.find_element_by_xpath("//button[@type='submit']").click()

    def open_admin_panel(self):
        self.driver.find_element_by_id("button-menu").click()

    def quit_browser_admin(self):
        self.driver.quit()
