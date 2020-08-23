from behave import *
from selenium import webdriver


@given('I launch the chrome browser')
def launch_browser(context):
    context.driver = webdriver.Chrome(executable_path="C:\PHANTOMS_PROJECT\drivers\chromedriver.exe")


@when('I open the orange HRM Homepage')
def open_home_page(context):
    context.driver.get("https://opensource-demo.orangehrmlive.com/")


@when('Enter the username "{username}" and password "{password}"')
def enter_login_details(context, username, password):
    context.driver.find_element_by_id("txtUsername").send_keys(username)
    context.driver.find_element_by_id("txtPassword").send_keys(password)


@when('Click on login Button')
def click_login_button(context):
    context.driver.find_element_by_id("btnLogin").click()


@then('User must be successfully logged in to the dashboard page')
def check_log_in(context):
    try:
        actual_text = context.driver.find_element_by_xpath("//h1[contains(text(),'Dashboard')]").text
    except Exception:
        context.driver.close()
        assert False, "Test Failed Cannot find Dashboard"
    if actual_text == "Dashboard":
        context.driver.close()
        assert True, "Test Passed. Login Successful"
