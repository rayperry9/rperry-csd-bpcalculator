from behave import *
from selenium import webdriver
from selenium.webdriver.chrome.options import Options

chromeOptions = Options()
chromeOptions.headless = True


@given("launch chrome browser")
def launchBrowser(context):
    context.driver = webdriver.Chrome("chromedriver", options=chromeOptions)


@when("open blood pressure calculator")
def openApp(context):
    context.driver.get("https://rayperry-dev-bpcalculator.azurewebsites.net")


@then("verify the container for systolic value input exists")
def verifySysValue(context):
    status = context.driver.find_element_by_name("systolic_value").is_displayed()
    assert status is True

@then("verify the container for diastolic value input exists")
def verifyDiasValue(context):
    status = context.driver.find_element_by_name("diastolic_value").is_displayed()
    assert status is True


@then("close browser")
def closeBrowser(context):
    context.driver.close()
