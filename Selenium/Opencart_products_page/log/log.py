"""Logging"""
import logging
import datetime as dt

from selenium.webdriver.support.events import AbstractEventListener

logging.basicConfig(filename="test.log", level=logging.INFO)


def msg_with_date(msg):
    """Adding date"""
    return ":".join([str(dt.datetime.now()), msg])


class TestListener(AbstractEventListener):
    """Class for writing logs and taking screenshots"""
    def before_navigate_to(self, url, driver):
        print(driver.get_log('browser'))
        logging.info(msg_with_date("".join(["Before navigate to ", url])))

    def after_navigate_to(self, url, driver):
        print(driver.get_log('browser'))
        performance_log = driver.get_log("performance")
        time_to_load = performance_log[-1].get('timestamp') - performance_log[0].get("timestamp")
        logging.info(" ".join(["Page load", url, str(time_to_load), 'ms']))

    def on_exception(self, exception, driver):
        logging.error(exception)
        now = dt.datetime.now()
        filename = "".join(["screenshots/exception", now.strftime("%d-%m-%Y-%H-%M"), ".png"])
        driver.get_screenshot_as_file(filename)
