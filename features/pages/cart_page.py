from selenium.webdriver.common.by import By
from browser import Browser

class CartPageLocator(object):

    HEADER = (By.CLASS_NAME, "subheader")
    INVENTORY_NAME = (By.CLASS_NAME, "inventory_item_name")
    CHECKOUT_BUTTON = (By.CLASS_NAME, "btn_action")

class CartPage(Browser):

    def get_header(self):
        return super().get_element(*CartPageLocator.HEADER).text

    def find_item_name(self):
        return super().get_element(*CartPageLocator.INVENTORY_NAME).text

    def checkout(self):
        return super().click_element(*CartPageLocator.CHECKOUT_BUTTON)
