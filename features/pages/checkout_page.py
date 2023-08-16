from selenium.webdriver.common.by import By
from browser import Browser

class CheckoutPageLocator(object):

    HEADER = (By.CLASS_NAME, "subheader")
    FIRST_NAME_FIELD = (By.ID, "first-name")
    LAST_NAME_FIELD = (By.ID, "last-name")
    POSTAL_CODE_FIELD = (By.ID, "postal-code")
    CONTINUE_BUTTON = (By.CLASS_NAME, "btn_primary")
    ERROR_MESSAGE = (By.XPATH, "//h3[@data-test='error']")

class CheckoutPage(Browser):

    def get_header(self):
        return super().get_element(*CheckoutPageLocator.HEADER).text

    def find_error_message(self):
        return super().get_element(*CheckoutPageLocator.ERROR_MESSAGE).text

    def fill_up_information(self, first_name, last_name, postal_code):
        super().fill(first_name, *CheckoutPageLocator.FIRST_NAME_FIELD)
        super().fill(last_name, *CheckoutPageLocator.LAST_NAME_FIELD)
        super().fill(postal_code, *CheckoutPageLocator.POSTAL_CODE_FIELD)
        super().click_element(*CheckoutPageLocator.CONTINUE_BUTTON)
