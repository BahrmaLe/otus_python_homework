"""Logging"""
import os
import datetime as dt
import sqlite3

from selenium.webdriver.support.events import AbstractEventListener

table_name = 'log'
# db_path = "C:/Users/60064265/PycharmProjects/Homework/Selenium/Opencart_products_page/db/logs.db"


def msg_with_date(msg):
    """Adding date"""
    return ":".join([str(dt.datetime.now()), msg])


class TestListenerDB(AbstractEventListener):
    """Class for writing logs to DB"""

    def __init__(self):
        """Initialize block"""
        db_path = "/".join([os.path.dirname(os.path.abspath(__file__)), "logs/logs.db"])
        print(db_path)
        self.conn = sqlite3.connect(db_path)

    def __exit__(self, exc_type, exc_val, exc_tb):
        """Closing DB session"""
        self.conn.close()

    def create_table(self):
        self.conn.execute("CREATE TABLE IF NOT EXISTS log(log, level)")
        self.conn.commit()

    def write(self, log, level="INFO"):
        """Inserting data to table log"""
        self.conn.execute("INSERT INTO log VALUES(\"{0}\", \"{1}\")".format(log, level))
        self.conn.commit()

    def before_navigate_to(self, url, driver):
        """Get url before navigating and insert to table"""
        self.write(msg_with_date("".join(["Before navigate to ", url])))

    def after_navigate_to(self, url, driver):
        """Get url after navigating and insert to table"""
        self.write(msg_with_date("".join(["After navigate to ", url])))

    def on_exception(self, exception, driver):
        """Get Exception log and insert to table"""
        self.write(exception)
