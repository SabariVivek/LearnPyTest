import time

from selenium import webdriver


def abc():
    driver = webdriver.Chrome()
    driver.maximize_window()
    driver.get("https://omayo.blogspot.com")
    time.sleep(5)
    driver.close()


abc()
