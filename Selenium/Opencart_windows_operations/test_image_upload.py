
def test_image_name(add_product_with_image, find_product_image):
    print(type(find_product_image))
    print(find_product_image)
    assert 'macbook_pro' in find_product_image


