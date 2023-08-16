from nose.tools import assert_equal, assert_true
from selenium.webdriver.common.by import By

use_step_matcher("parse")

@step('I navigate to Overview page')
def navigate_to_overview_page(context):
    assert_equal(context.overview_page.get_header(), "Checkout: Overview")
    