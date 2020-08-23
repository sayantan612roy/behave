from behave import *
from selenium import webdriver
import pytest


@when('I open the practice URL')
def test_go_to_practice_url(context):
    context.driver.get("http://automationpractice.com/index.php")


@then('Verify the logo is present')
def test_for_the_logo(context):
    logo_check = context.driver.find_element_by_xpath("//img[@class='logo img-responsive']").is_displayed()
    assert logo_check is True, "Test Passed"

# Command for allure reports
# behave -f allure_behave.formatter:AllureFormatter -o reports/ features/test_logo.feature
# Convert to html report allure serve report/
# To enable allure conversion install node js package npm install -g allure-commandline --save-dev
