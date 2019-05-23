def test_open_home_page(driver, request):
    url = 'opencart/'
    return driver.get("".join([request.config.getoption("--address"), url]))
    element = driver.find_elements_by_xpath("//base[contains(@href, 'http://192.168.56.103/opencart/]")
    assert element == 'http://192.168.56.103/opencart/'
    assert driver.find_element_by_class_name('col-sm-4').text == 'Your Store'


