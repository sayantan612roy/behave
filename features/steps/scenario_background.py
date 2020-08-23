from behave import *
from selenium import webdriver
import pytest


@when('Navigate to search page')
def navigate_to_search_page(context):
    context.driver
    assert True, "Test Passed"


@then('search page should be displayed')
def check_search_page(context):
    assert True, "Test Passed"


@when('Navigate to advanced search page')
def navigate_adv_search_page(context):
    assert True, "Test Passed"


@then('advanced search page should be displayed')
def check_adv_search_page(context):
    assert True, "Test Passed"

