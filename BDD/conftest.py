import pytest


def pytest_addoption(parser):
    """Setting base URL Openacart and parametrize command line options for select
    browsers and set username or password """
    parser.addoption("--address", action="store", default="http://192.168.56.103/opencart/",
                     help="Opencart web address")


@pytest.fixture(scope="session", autouse=True)
def driver(request):
    """Launching webdriver"""
    browser_name = request.config.getoption("--browser")
    print(browser_name)
    if browser_name == 'firefox':
        capabilities = WD.DesiredCapabilities.FIREFOX.copy()
        capabilities['timeouts'] = {'implicit': 300000, 'pageLoad': 300000, 'script': 30000}
        capabilities['loggingPrefs'] = {'browser': 'ALL', 'client': 'ALL', 'driver': 'ALL',
                                        'performance': 'ALL', 'server': 'ALL'}
        capabilities['unexpectedAlertBehaviour'] = 'accept'
        profile = WD.FirefoxProfile()
        profile.set_preference('app.update.auto', False)
        profile.set_preference('app.update.enabled', False)
        profile.accept_untrusted_certs = True
        wd = WD.Firefox(firefox_profile=profile, capabilities=capabilities)
        wd.maximize_window()
    elif browser_name == 'chrome':
        capabilities = WD.DesiredCapabilities.CHROME.copy()
        capabilities['acceptSslCerts'] = True
        capabilities['acceptInsecureCerts'] = True
        capabilities['unexpectedAlertBehaviour'] = 'dismiss'
        wd = WD.Chrome(desired_capabilities=capabilities)
        wd.fullscreen_window()
    else:
        print('Unsupported browser!')
        sys.exit(1)
    wd.implicitly_wait((request.config.getoption("--iwait")))
    wd.set_page_load_timeout((request.config.getoption("--pltimeout")))
    implicitly_wait = request.config.getoption("--iwait")
    page_load_timeout = request.config.getoption("--pltimeout")
    print(implicitly_wait)
    print(page_load_timeout)
    yield wd
    wd.quit()