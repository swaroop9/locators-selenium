import pytest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager

import pytest

from selenium import webdriver

driver = None


# Cmd line options for browsers in conftest.py
def pytest_add_option(parser):
    parser.addoption("--browserName", action="store", default="chrome",
                     help="Option: Chrome or FireFox or IE")


@pytest.fixture(scope="class")
def set_up(request):
    global driver
    browser_name = request.config.getoption("--browserName")
    url = "https://the-internet.herokuapp.com/login"

    if browser_name == "chrome":
        service = Service(ChromeDriverManager().install())
        driver = webdriver.Chrome(service=service)
        # driver = webdriver.Chrome('./chromedriver') # deprecated
    elif browser_name == "firefox":
        print("In firefox")
        firefox_path = "/Users/pyaganti/Documents/Practice/Automation-Testing/selenium-python/browserExes/geckodriver"
        driver = webdriver.Chrome(executable_path=firefox_path)
    elif browser_name == "IE":
        print("needs to be implemented")
        ie_path = "/Users/pyaganti/Documents/Practice/Automation-Testing/selenium-python/browserExes/chromedriver"
        driver = webdriver.Chrome(executable_path=ie_path)
    else:
        print("Enter Proper option")

    driver.get(url)
    driver.maximize_window()

    # To pass driver obj to class
    request.cls.driver = driver

    yield

    driver.close()


@pytest.mark.hookwrapper
def pytest_runtest_makereport(item):
    """
        Extends the PyTest Plugin to take and embed screenshot in html report, whenever test fails.
        :param item:
        """
    pytest_html = item.config.pluginmanager.getplugin('html')
    outcome = yield
    report = outcome.get_result()
    extra = getattr(report, 'extra', [])

    if report.when == 'call' or report.when == "setup":
        xfail = hasattr(report, 'wasxfail')
        if (report.skipped and xfail) or (report.failed and not xfail):
            file_name = report.nodeid.replace("::", "_") + ".png"
            _capture_screenshot(file_name)
            if file_name:
                html = '<div><img src="%s" alt="screenshot" style="width:304px;height:228px;" ' \
                       'onclick="window.open(this.src)" align="right"/></div>' % file_name
                extra.append(pytest_html.extras.html(html))
        report.extra = extra


def _capture_screenshot(name):
    driver.get_screenshot_as_file(name)