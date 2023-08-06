# test_parallel_execution.py

"""
First --> We have to install pytest-xdist...
Execution --> pytest -n 6 --> 6 represents thread count...
"""
import time

from selenium import webdriver


def test_login_omayo_one():
    driver = webdriver.Edge()
    driver.maximize_window()
    driver.get("https://omayo.blogspot.com")
    time.sleep(5)
    driver.close()


def test_login_omayo_two():
    driver = webdriver.Edge()
    driver.maximize_window()
    driver.get("https://omayo.blogspot.com")
    time.sleep(5)
    driver.close()


def test_login_omayo_three():
    driver = webdriver.Edge()
    driver.maximize_window()
    driver.get("https://omayo.blogspot.com")
    time.sleep(5)
    driver.close()
