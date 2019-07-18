def test_upload_file(upload_file):
    pass


def test_uploaded_file(check_uploaded_file):
    print(type(check_uploaded_file))
    print(check_uploaded_file)
    assert '111' in check_uploaded_file
