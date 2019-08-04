"""SeleniumGrid Testing"""


def test_firefox(firefox_browser):
    """Testing on Virtual machine"""
    firefox_browser.get("https://habr.com/ru/")
    print(firefox_browser.title)
    assert firefox_browser.title == "Лучшие публикации за сутки / Хабр"


def test_chrome(chrome_browser):
    """Testing on local machine"""
    chrome_browser.get("https://habr.com/ru/")
    print(chrome_browser.title)
    assert chrome_browser.title == "Лучшие публикации за сутки / Хабр"

