def test_restart_opencart_mysql_service(restart_mysql):
    assert "active (running)" in restart_mysql
    print(restart_mysql)


def test_restart_opencart_apache_service(restart_apache):
    assert "active (running)" in restart_apache
    print(restart_apache)


def test_opencart_is_active(request_opencart):
    print(request_opencart.status_code)
    assert request_opencart.status_code == 200
