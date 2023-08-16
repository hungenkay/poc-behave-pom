from selenium.webdriver.common.by import By
from browser import Browser

class LoginPageLocator(object):

    USERNAME_FIELD = (By.ID, "user-name")
    PASSWORD_FIELD = (By.ID, "password")
    LOGIN_BUTTON = (By.CLASS_NAME, "btn_action")
    ERROR_MESSAGE = (By.XPATH, "//h3[@data-test='error']")


class LoginPage(Browser):

    def navigate(self):
        super().navigate("https://www.saucedemo.com")

    def get_page_title(self):
        return super().get_page_title()

    def login(self, uid, pwd):
        super().fill(uid, *LoginPageLocator.USERNAME_FIELD)
        super().fill(pwd, *LoginPageLocator.PASSWORD_FIELD)
        super().click_element(*LoginPageLocator.LOGIN_BUTTON)

    def find_error_message(self):
        return super().get_element(*LoginPageLocator.ERROR_MESSAGE).text
