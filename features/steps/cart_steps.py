from nose.tools import assert_equal, assert_true
from selenium.webdriver.common.by import By

use_step_matcher("parse")

@step('I navigate to Cart page')
def navigate_to_cart_page(context):
    assert_equal(context.cart_page.get_header(), "Your Cart")

@step('"{product}" product is available on Cart page')
def check_product_on_cart_page(context, product):
    assert_equal(str(context.cart_page.find_item_name()), str(product))

@step('I checkout on Cart page')
def checkout_on_cart_page(context):
    context.cart_page.checkout()
    