from selenium.webdriver.common.by import By
from browser import Browser

class ProductPageLocator(object):

    HEADER = (By.CLASS_NAME, "product_label")
    SHOPPING_CART_BUTTON = (By.CLASS_NAME, "shopping_cart_link")

class ProductPage(Browser):

    def get_header(self):
        return super().get_element(*ProductPageLocator.HEADER).text

    def buy_item(self, item_name):
        item = super().get_element_by_text(item_name)
        add_to_cart_button = item.find_element_by_xpath("parent::*/parent::*//button")
        add_to_cart_button.click()
        super().click_element(*ProductPageLocator.SHOPPING_CART_BUTTON)
