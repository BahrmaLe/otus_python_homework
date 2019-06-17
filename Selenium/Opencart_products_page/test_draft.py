# def test_products(driver, add_product, login_action, open_products_page):
#     products = driver.find_element_by_xpath('//*[@id="form-product"]/div/table/tbody')
#     products_elements = products.find_elements_by_tag_name("tr")
#     product_list = set()
#     for element in products_elements:
#         product_name = element.find_elements_by_tag_name("td")[2]
#         product_list.add(product_name.text)
#     print(product_list)
#     assert "New Product" in product_list


# def test_products(driver, add_product, open_login_page, login_action, catalog_menu):
#     catalog_menu.open_catalog()
#     catalog_menu.open_products()
#     products = driver.find_element_by_xpath('//*[@id="form-product"]/div/table/tbody')
#     products_elements = products.find_elements_by_tag_name("tr")
#     product_list = set()
#     for element in products_elements:
#         product_name = element.find_elements_by_tag_name("td")[2]
#         product_list.add(product_name.text)
#     print(product_list)
#     assert "New Product" in product_list


def test_delete_product(driver, open_login_page, login_action, catalog_menu, products_page):
    catalog_menu.open_catalog()
    catalog_menu.open_products()
    products_page.matchproduct()
    driver.implicitly_wait(3)
    products_page.delete()
    driver.implicitly_wait(3)
    alert = driver.switch_to.alert
    print(alert.text)
    alert.accept()
    products = driver.find_element_by_xpath('//*[@id="form-product"]/div/table/tbody')
    products_elements = products.find_elements_by_tag_name("tr")
    product_list = set()
    for element in products_elements:
        product_name = element.find_elements_by_tag_name("td")[2]
        product_list.add(product_name.text)
    print(product_list)
    assert "New Product" not in product_list





