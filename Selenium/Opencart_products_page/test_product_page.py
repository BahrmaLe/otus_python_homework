def test_products(add_product, driver, open_login_page,
                  login_action, open_products_page, products_list):
    """Test that New product is added"""
    assert "New Product" in products_list


def test_edit_product(driver, open_login_page, login_action,
                      open_products_page, edit_product, products_list):
    """Test that New product is edited"""
    assert "Edited Product" in products_list


def test_delete_product(driver, open_login_page, login_action,
                        open_products_page, delete_product, products_list):
    """Test that product is deleted"""
    assert "Edited Product" not in products_list
