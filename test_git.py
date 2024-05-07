import os
import allure
import time
import pytest
from selenium import webdriver
# import prefs as prefs
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.select import Select
from selenium.webdriver import Keys

options = webdriver.ChromeOptions()
options.add_argument("--headless")
options.add_argument('start-maximized')
service = Service(executable_path=ChromeDriverManager().install())
driver = webdriver.Chrome(service=service, options=options)
action = ActionChains(driver)
wait = WebDriverWait(driver, 15, poll_frequency=1)


def test_inputs():
    options = Options()
    options.add_argument("--headless")
    options.add_argument('start-maximized')
    driver.get("https://www.qa-practice.com/elements/input/simple")

    # VARIABLES
    FIRST_INPUT_locator = ("xpath", '//input[@type = "text"]')

    # ACTION
    FIRST_INPUT_act = driver.find_element(*FIRST_INPUT_locator)
    FIRST_INPUT_act.send_keys("mymaertertretrtertertretil@gmail.com")
    print("INPUTS SUCCESS")


def test_buttons():
    options = Options()
    options.add_argument("--headless")
    options.add_argument('start-maximized')
    driver.get("https://www.qa-practice.com/elements/input/simple")

    # VARIABLES
    FIRST_INPUT_locator = ("xpath", '//input[@type = "text"]')

    # ACTION
    FIRST_INPUT_act = driver.find_element(*FIRST_INPUT_locator)
    FIRST_INPUT_act.send_keys("NEmyMAIL@protonmail.ru")
    print("INPUTS SUCCESS")