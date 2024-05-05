import os
import time
import pytest
from selenium import webdriver
# import prefs as prefs
from webdriver_manager.firefox import GeckoDriverManager
from selenium.webdriver.firefox.service import Service
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.firefox.options import Options
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.select import Select
from selenium.webdriver import Keys

options = webdriver.FirefoxOptions()
service = Service(executable_path=GeckoDriverManager().install())
driver = webdriver.Firefox(service=service, options=options)
action = ActionChains(driver)
wait = WebDriverWait(driver, 15, poll_frequency=1)


def test_inputs():
    driver.get("https://www.qa-practice.com/elements/input/simple")

    # VARIABLES
    FIRST_INPUT_locator = ("xpath", '//input[@type = "text"]')
    FIRST_SWITCH_BUTTON = ("xpath", '//a[text() = "Email field"]')
    MAIL_INPUT_AREA = ('xpath', '//input[@id = "id_email"]')
    PASSWORD_FIELD_BUTTON = ("xpath", '//a[text() = "Password field"]')

    # ACTION
    FIRST_INPUT_act = driver.find_element(*FIRST_INPUT_locator)
    FIRST_INPUT_act.send_keys("mymail@gmail.com")

    driver.find_element(*FIRST_SWITCH_BUTTON).click()

    # handlers = driver.window_handles
    # driver.switch_to.window(handlers[1])

    # wait.until(EC.element_to_be_clickable(*MAIL_INPUT_AREA)).click()
    driver.find_element(*MAIL_INPUT_AREA).send_keys("mymailTOO@proton.com")
    driver.find_element(*PASSWORD_FIELD_BUTTON).click()
    driver.find_element("xpath", '//input[@id = "id_password"]').send_keys("myNewSecretPassword")
    print("INPUTS SUCCESS")