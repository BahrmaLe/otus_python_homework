from pytest_bdd import scenarios, given, when, then, parsers
from selenium import webdriver
from selenium.webdriver.common.keys import Keys


# Constants

OPENCART_HOME = 'http://192.168.56.103/opencart'
OPENCART_CART = 'http://192.168.56.103/opencart/index.php?route=checkout/cart'


# Scenarios

scenarios('../features/web.feature')


# Given Steps

@given('the Opencart home page is displayed')
def opencart_home(driver):
    driver.get(OPENCART_HOME)


@given('the User cart page is displayed')
def opencart_home(driver):
    driver.get(OPENCART_CART)


# When Steps

@when(parsers.parse('the user searches for "{phrase}"'))
def search_product(driver, phrase):
    search_input = driver.find_element_by_xpath('//*[@id="search"]/input')
    search_input.send_keys(phrase + Keys.RETURN)


@when(parsers.parse('the user product page'))
def open_product(driver):
    driver.find_element_by_link_text('MacBook').click()


@when(parsers.parse('the user add product to cart'))
def add_product(driver):
    driver.find_element_by_xpath('//*[@id="button-cart"]').click()


@when(parsers.parse('the user remove product from cart'))
def remove_product(driver):
    driver.find_element_by_xpath('//*[@type="button"]').click()


@when(parsers.parse('the user click to home page'))
def open_home_page(driver):
    driver.find_element_by_link_text('Your Store').click()


# Then Steps

@then(parsers.parse('one of the results contains "{phrase}"'))
def results_have_product(driver, phrase):
    xpath = "//*[@id='search']/input/contains(text(), '%s')]" % phrase
    results = driver.find_elements_by_xpath(xpath)
    assert len(results) > 0


@then(parsers.parse('results are shown for "{phrase}"'))
def search_results(driver, phrase):
    # Check search result list
    # (A more comprehensive test would check results for matching phrases)
    # (Check the list before the search phrase for correct implicit waiting)
    links_div = driver.find_element_by_id('content')
    assert len(links_div.find_elements_by_xpath('//div')) > 0
    # Check search phrase
    search_input = driver.find_element_by_xpath('//*[@id="search"]/input')
    assert search_input.get_attribute('value') == phrase


@then(parsers.parse('Product page is opened'))
def product_page_opened(driver, product):
    xpath = "//*[@class='thumbnail']/contains(text(), '%s')]" % product
    results = driver.find_elements_by_xpath(xpath)
    assert "MacBook" in results


@then(parsers.parse('Product added to cart'))
def product_in_cart(driver, product):
    xpath = "//*[@class='text-left']/contains(text(), '%s')]" % product
    results = driver.find_elements_by_xpath(xpath)
    assert "MacBook" in results


@then(parsers.parse('Product removed from cart'))
def results_removed_product(driver, product):
    xpath = "//*[@id='error-not-found']"
    results = driver.find_elements_by_xpath(xpath)
    assert len(results) > 0


@then(parsers.parse('Home page is opened'))
def results_have_product(driver, phrase):
    xpath = "//*[@id='common-home']"
    results = driver.find_elements_by_xpath(xpath)
    assert results is not None

