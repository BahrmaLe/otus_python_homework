"""Test forgotten password link"""
import time
import pytest
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
    """Click on Forgotten link"""
    login_page.forgot_link()
    time.sleep(5)


@pytest.mark.usefixtures("login_page")
@pytest.mark.usefixtures("open_login_page")
class TestLoginPage:
    """Class for checking asserts"""
    @pytest.mark.usefixtures("login")
    def test_forgotten_password(self, driver):
        """Test redirection to forgot password page"""
        print(driver.current_url)
        assert "forgotten" in driver.current_url
