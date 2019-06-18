def test_products(add_product, driver, open_login_page, login_action, open_products_page):
    products = driver.find_element_by_xpath('//*[@id="form-product"]/div/table/tbody')
    products_elements = products.find_elements_by_tag_name("tr")
    product_list = set()
    for element in products_elements:
        product_name = element.find_elements_by_tag_name("td")[2]
        product_list.add(product_name.text)
    print(product_list)
    assert "New Product" in product_list


def test_edit_product(driver, open_login_page, login_action, open_products_page, products_page, product_card):
    products_page.edit()
    product_card.clear_productname()
    product_card.productname('Edited Product')
    product_card.clear_metatag()
    product_card.metatag('Edited Meta Tag Keyword')
    product_card.datatab()
    product_card.clear_modelname()
    product_card.modelname('Edited model')
    product_card.savebutton()
    products = driver.find_element_by_xpath('//*[@id="form-product"]/div/table/tbody')
    products_elements = products.find_elements_by_tag_name("tr")
    product_list = set()
    for element in products_elements:
        product_name = element.find_elements_by_tag_name("td")[2]
        product_list.add(product_name.text)
    print(product_list)
    assert "Edited Product" in product_list


def test_delete_product(driver, open_login_page, login_action, open_products_page, products_page):
    products_page.matchproduct()
    products_page.delete()
    alert = driver.switch_to.alert
    print(alert.text)
    alert.accept()
    driver.refresh()
    products = driver.find_element_by_xpath('//*[@id="form-product"]/div/table/tbody')
    products_elements = products.find_elements_by_tag_name("tr")
    product_list = set()
    for element in products_elements:
        product_name = element.find_elements_by_tag_name("td")[2]
        product_list.add(product_name.text)
    print(product_list)
    assert "Edited Product" not in product_list
