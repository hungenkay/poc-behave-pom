from nose.tools import assert_equal, assert_true
from selenium.webdriver.common.by import By

use_step_matcher("parse")

@step('I navigate to Product page')
def navigate_to_product_page(context):
    assert_equal(context.product_page.get_header(), "Products")

@step('I choose "{product}" product to add to cart')
def choose_product_to_add_to_card(context, product):
    context.product_page.buy_item(product)