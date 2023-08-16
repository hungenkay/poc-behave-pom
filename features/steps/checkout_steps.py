from nose.tools import assert_equal, assert_true
from selenium.webdriver.common.by import By

use_step_matcher("parse")

@step('I navigate to Checkout page')
def navigate_to_checkout_page(context):
    assert_equal(context.checkout_page.get_header(), "Checkout: Your Information")

@step('I enter "{firstName}" first name and "{lastName}" last name and "{postalCode}" postal code')
def enter_checkout_info(context, firstName, lastName, postalCode):
    context.checkout_page.fill_up_information(firstName, lastName, postalCode)

@step('I see "{error}" error message on Checkout page')
def check_error_message_on_checkout_page(context, error):
    assert_equal(context.checkout_page.find_error_message() , error)
    