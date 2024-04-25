from behave import *
from selenium import webdriver
from selenium.webdriver.edge.webdriver import WebDriver

use_step_matcher("re")


@given("I navigate to google.com")
def step_impl(context):
    """
    :type context: behave.runner.Context
    """
    print(u'STEP: Given I navigate to google.com')


@when("I validate the page title")
def step_impl(context):
    global driver
    print("Launching webdriver...")
    # driver = webdriver.Chrome()
    driver = webdriver.Edge()
    print("Open Facebook Page")
    driver.get("https://facebook.com")
    print("Maximizing page size...")
    driver.maximize_window()
    title = context.driver.title
