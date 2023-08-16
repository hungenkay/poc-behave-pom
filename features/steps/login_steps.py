from nose.tools import assert_equal, assert_true
from selenium.webdriver.common.by import By

use_step_matcher("parse")

@step('I navigate to Wizeline page')
def navigate_to_wizeline_page(context):
    context.login_page.navigate()
    assert_equal(context.login_page.get_page_title(), "Swag Labs")

@step('I login by using "{username}" username and "{password}" password')
def login_by_using_username_and_password(context, username, password):
    context.login_page.login(username, password)

@step('I can see this "{error}" error message')
def check_error_message_on_login_page(context, error):
    assert_equal(str(context.login_page.find_error_message()), str(error))