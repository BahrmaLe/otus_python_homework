"""Test correctly login data"""
import time
import pytest


from Selenium.Opencart_login_page.conftest import browser
from Selenium.Opencart_login_page.models.page_objects.page_objects import LoginPage


@pytest.fixture(scope="session")
def open_login_page(driver, request):
    """Get base URL and attend admin link"""
    url = 'opencart/admin/'
    return driver.get("".join([request.config.getoption("--address"), url]))


@pytest.fixture(scope="module")
def login_page(driver):
    """Use class from  page objects module for managing elements on the page"""
    return LoginPage(driver)


@pytest.fixture(scope="function")
def login(login_page):
    """Set Username and Password and login"""
    login_page.set_username("admin")
    login_page.set_password("admin")
    login_page.login()
    time.sleep(5)


@pytest.fixture(scope="function")
def submit(login_page):
    """Set Username and Password by another element(locator)"""
    login_page.set_username("admin")
    login_page.set_password("admin")
    login_page.submit()
    time.sleep(5)


@pytest.mark.usefixtures("login_page")
@pytest.mark.usefixtures("open_login_page")
class TestLoginPage:
    """Class for checking asserts"""
    if browser == 'firefox':
        @pytest.mark.usefixtures("login")
        def test_login(self, driver):
            """Test alert for Firefox"""
            print(driver.current_url)
            assert "dashboard" in driver.current_url
    else:
        @pytest.mark.usefixtures("submit")
        def test_submit(self, driver):
            """Test alert for Chrome"""
            print(driver.current_url)
            assert "dashboard" in driver.current_url
