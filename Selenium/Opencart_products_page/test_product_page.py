from selenium.webdriver.common.by import By


def test_categories(driver, request):
    url = 'opencart/admin/'
    driver.get("".join([request.config.getoption("--address"), url]))
    driver.find_element(By.ID, "input-username").send_keys("admin")
    driver.find_element(By.ID, "input-password").send_keys("admin")
    driver.find_element(By.CLASS_NAME, "btn.btn-primary").click()
    driver.find_element_by_class_name("close").click()
    els = driver.find_elements_by_class_name("parent.collapsed")
    for el in els:
        if el.text == "Catalog":
            catalog = el
            break
    catalog.click()
    catalog_elements = driver.find_elements_by_tag_name("li")
    for catalog_element in catalog_elements:
        if catalog_element.text == "Categories":
            catalog_element.click()
            break
    fluids = driver.find_elements_by_class_name("container-fluid")
    for fl in fluids:
        if "Categories" in fl.text:
            action_fluid = fl
            break
    action_fluid.find_element_by_class_name("btn.btn-primary").click()
    driver.find_element_by_name("category_description[1][name]").send_keys("Test Category")
    driver.find_element_by_name("category_description[1][meta_title]").send_keys("Test Category")
    driver.find_element_by_class_name("fa.fa-save").click()
    notification = driver.find_element_by_class_name("alert.alert-success.alert-dismissible")
    notification_text = notification.text.rstrip("\n×'")
    assert notification
    assert notification_text == "Success: You have modified categories!"
