"""Test alert which appears for incorrectly login data"""
import time
import pytest


def test_alert(browser_action):
    """Test alert for Firefox"""
    print(type(browser_action))
    print(browser_action.login_page.alertmessage())
    # x = browser_action(alertmessage)
    # for i in x:
    #     print(i)
    # assert text == 'No match for Username and/or Password.'
# else:
#     @pytest.mark.usefixtures("submit")
#     def test_alert(self, driver):
#         """Test alert for Chrome"""
#         alert = driver.find_element_by_css_selector("div.alert.alert-danger.alert-dismissible")
#         print(alert.text)
#         assert 'No match for Username and/or Password.' in alert.text
#         driver.find_element_by_class_name("close").click()
#         time.sleep(3)
