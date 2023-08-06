# test_two.py
import allure
import pytest
from selenium.webdriver.common.by import By


@pytest.mark.usefixtures("setup_and_teardown", "log_on_failure")
class Test_Two:
    @allure.severity(allure.severity_level.BLOCKER)
    def test_two(self):
        self.driver.find_element(By.XPATH, "//option[@value='volvox']").click()
        assert False
