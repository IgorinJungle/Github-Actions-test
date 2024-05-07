import os
import time

# import prefs as prefs
import pytest
import allure
from selenium import webdriver
from selenium.webdriver import Keys
from webdriver_manager.firefox import GeckoDriverManager
from selenium.webdriver.firefox.options import Options
from selenium.webdriver.firefox.service import Service
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.select import Select

options = webdriver.FirefoxOptions()
# options.add_argument("--headless")
# options.add_argument("--disable-cache")


service = Service(executable_path=GeckoDriverManager().install())
driver = webdriver.Firefox(service=service, options=options)
action = ActionChains(driver)
wait = WebDriverWait(driver, 15, poll_frequency=1)


@allure.feature("LOG IN")
def test_login():
    driver.get("https://www.saucedemo.com/")
    with allure.step("Filling Login"):
        driver.find_element('xpath', '//input[@id = "user-name"]').send_keys("standard_user")
        driver.find_element('xpath', '//input[@id = "password"]').send_keys("secret_sauce")
    with allure.step("Entering system"):
        driver.find_element("xpath", '//input[@id = "login-button"]').click()


