from selenium import webdriver
from browser import Browser
from pages.login_page import LoginPage
from pages.product_page import ProductPage
from pages.cart_page import CartPage
from pages.checkout_page import CheckoutPage
from pages.overview_page import OverviewPage

def before_all(context):
    context.browser = Browser()
    context.login_page = LoginPage()
    context.product_page = ProductPage()
    context.cart_page = CartPage()
    context.checkout_page = CheckoutPage()
    context.overview_page = OverviewPage()

def after_all(context):
    context.browser.close()
