import pytest
from selenium import webdriver
from selenium.webdriver.firefox.firefox_binary import FirefoxBinary

HUB = "http://192.168.56.1:4444/wd/hub"


@pytest.fixture
def chrome_browser():
    wd = webdriver.Remote(HUB, desired_capabilities={"browserName": "chrome", "version": '75'})
    yield wd
    wd.quit()


@pytest.fixture
def firefox_browser():
    binary = FirefoxBinary('C:/Program Files/Firefox Nightly/firefox.exe')
    wd = webdriver.Remote(HUB, desired_capabilities={"browserName": "firefox", "version": '66'})
    yield wd
    wd.quit()
