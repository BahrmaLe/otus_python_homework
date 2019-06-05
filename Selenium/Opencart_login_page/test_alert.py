def test_alert_message(alert_message):
    """Use this for check message in different cases:Incorrectly username/password, only username, only password by
    parameters """
    print(alert_message)
    assert 'No match for Username and/or Password.' in alert_message
