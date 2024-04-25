import allure
from allure_commons.types import AttachmentType
from selenium import webdriver
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager
import pytest


def get_data():
    return [
        ("learner1@python.com", "Smile@python1"),
        ("learner2@python.com", "Smile@python2"),
        ("learner3@python.com", "Smile@python3")
    ]


def setup_function():
    global driver
    print("Launching webdriver...")
    # driver = webdriver.Chrome()
    driver = webdriver.Edge()
    print("Open Facebook Page")
    allure.attach(driver.get_screenshot_as_png(), name="Facebook Page", attachment_type=AttachmentType.PNG)
    driver.get("https://facebook.com")
    print("Maximizing page size...")
    driver.maximize_window()


def teardown_function():
    driver.quit()


@pytest.mark.parametrize("username, password", get_data())
def test_login(username, password):
    driver.find_element(By.ID, "email").send_keys(username)
    driver.find_element(By.ID, "pass").send_keys(password)

    print("Open Facebook Page")
    print(username, "-------", password)
    allure.attach(driver.get_screenshot_as_png(), name="Facebook Page", attachment_type=AttachmentType.PNG)
    driver.get("https://facebook.com")
    print("Maximizing page size...")


