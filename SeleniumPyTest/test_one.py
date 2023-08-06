# test_one.py
import allure
import pytest
from selenium.webdriver.common.by import By


@pytest.mark.usefixtures("setup_and_teardown", "log_on_failure")
class Test_One:
    @allure.severity(allure.severity_level.BLOCKER)
    def test_one(self):
        self.driver.find_element(By.XPATH, "//option[@value='volvox']").click()
