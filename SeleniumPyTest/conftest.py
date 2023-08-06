# conftest.py
import allure
import pytest
import time
from allure_commons.types import AttachmentType

from selenium import webdriver


@pytest.yield_fixture
def log_on_failure(request):
    yield
    item = request.node
    if item.rep_call.failed:
        allure.attach(driver.get_screenshot_as_png(), name="test_one_screenshot",
                      attachment_type=AttachmentType.PNG)


@pytest.hookimpl(hookwrapper=True, tryfirst=True)
def pytest_runtest_makereport(item):
    outcome = yield
    rep = outcome.get_result()
    setattr(item, "rep_" + rep.when, rep)
    return rep


@pytest.fixture(scope="class", params=["edge"])
def setup_and_teardown(request):
    global driver

    if request.param == "chrome":
        driver = webdriver.Chrome()
    elif request.param == "edge":
        driver = webdriver.Edge()
    elif request.param == "firefox":
        driver = webdriver.Firefox()
    driver.maximize_window()
    driver.get("https://omayo.blogspot.com")
    driver.implicitly_wait(10)
    request.cls.driver = driver
    yield
    time.sleep(3)
    driver.quit()
