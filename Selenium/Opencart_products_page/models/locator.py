"""Locators for opencart login page"""
from selenium.webdriver.common.by import By


class AdminPageLocators(object):
    """Admin page locators"""
    CATALOG = (By.XPATH, '//*[@id="menu-catalog"]/a')
    CATALOG2 = (By.CSS_SELECTOR, '#menu-catalog > a')
    CATALOG3 = (By.LINK_TEXT, 'Catalog')
    PRODUCTS = (By.XPATH, '//*[@id="collapse1"]/li[2]')
    PRODUCTS2 = (By.CSS_SELECTOR, '#collapse1 > li.active')
    PRODUCTS3 = (By.XPATH, '//*[@id="collapse1"]/li[2]/a')
    PRODUCTS4 = (By.CSS_SELECTOR, '#collapse1 > li.active > a')
    PRODUCTS5 = (By.LINK_TEXT, 'Products')
    ADDNEW = (By.CLASS_NAME, "a.btn.btn-primary")
    ADDNEW2 = (By.XPATH, '//*[@id="content"]/div[1]/div/div/a')
    ADDNEW3 = (By.PARTIAL_LINK_TEXT, "add")
    DELETE = (By.CSS_SELECTOR, "#content > div.page-header > div > div > button.btn.btn-danger")
    MATCHPRODUCT = (By.XPATH, "//td[text()='Edited Product']/preceding-sibling::td[@class='text-center']/input["
                              "@type='checkbox']")
    EDIT = (By.XPATH, "//td[text()='New Product']/following-sibling::td[@class='text-right']/a["
                      "@data-original-title='Edit']")
    PRODUCTSLIST = (By.XPATH, '//*[@id="form-product"]/div/table/tbody')
    # PRODUCTELEMENTS = (PRODUCTSLIST.By.TAG_NAME, "tr")
    # PRODUCT_NAME = (By.TAG_NAME, "td")


class ProductPageLocators(object):
    PRODUCTNAME = (By.XPATH, '//*[@id="input-name1"]')
    PRODUCTNAME2 = (By.NAME, "category_description[1][name]")
    PRODUCTNAME3 = (By.CSS_SELECTOR, '#input-name1')
    METATAG = (By.XPATH, '//*[@id="input-meta-title1"]')
    DATATAB = (By.XPATH, '//*[@id="form-product"]/ul/li[2]/a')
    MODELNAME = (By.XPATH, '//*[@id="input-model"]')
    SAVEBUTTON = (By.XPATH, '//*[@id="content"]/div[1]/div/div/button/i')


class BaseLocators(object):
    """Base locator (submit button)"""
    PRIMARY_BUTTON = (By.TAG_NAME, "button")
    SUBMIT_BUTTON = (By.XPATH, "//*[@type='submit']")


class LoginPageLocators(object):
    """Login page locators (Username, Password, Alert, Forgot password, Close alert button)"""
    USERNAME = (By.ID, "input-username")
    USERNAME2 = (By.NAME, "username")
    USERNAME3 = (By.CSS_SELECTOR, "#input-username")
    USERNAME4 = (By.XPATH, "//*[@placeholder='Username']")
    PASSWORD = (By.ID, "input-password")
    ERROR = (By.CLASS_NAME, "alert.alert-danger.alert-dismissible")
    FORGOT = (By.LINK_TEXT, "Forgotten Password")
    ALERT = (By.CSS_SELECTOR, "div.alert.alert-danger.alert-dismissible")
    ALERTICON = (By.CSS_SELECTOR, "i.fa.fa-exclamation-circle")
    CLOSEALERT = (By.CLASS_NAME, 'close')
