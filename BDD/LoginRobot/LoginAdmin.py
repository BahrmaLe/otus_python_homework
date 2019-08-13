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

    def expand_catalog(self):
        self.driver.find_element_by_css_selector("#menu-catalog > a").click()

    def open_category(self):
        self.driver.find_element_by_css_selector("#menu-catalog > ul > li:nth-child(1) > a").click()

    def expand_design(self):
        self.driver.find_element_by_css_selector("#menu-design > a").click()

    def open_designer(self):
        self.driver.find_element_by_css_selector("#menu-design > ul > li:nth-child(2) > a").click()

    def expand_system(self):
        self.driver.find_element_by_css_selector("#menu-system > a > i").click()

    def open_settings_menu(self):
        self.driver.find_element_by_css_selector("#menu-system > ul > li:nth-child(1) > a").click()

    def expand_reports(self):
        self.driver.find_element_by_css_selector("#menu-report > a").click()

    def open_sells_menu(self):
        self.driver.find_element_by_css_selector("#menu-report > ul > li.open > a").click()

    def open_orders_menu(self):
        self.driver.find_element_by_css_selector("#menu-report > ul > li.open > ul > li:nth-child(1) > a").click()

    def reports_page_assert(self):
        assert "sale_order" in self.driver.current_url

    def settings_page_assert(self):
        assert "setting" in self.driver.current_url

    def admin_page_assert(self):
        assert "dashboard" in self.driver.current_url

    def design_page_assert(self):
        assert "design" in self.driver.current_url

    def category_page_assert(self):
        assert "category" in self.driver.current_url

    def quit_browser_admin(self):
        self.driver.quit()
