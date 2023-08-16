from selenium.webdriver.common.by import By
from browser import Browser

class OverviewPageLocator(object):

    HEADER = (By.CLASS_NAME, "subheader")

class OverviewPage(Browser):

    def get_header(self):
        return super().get_element(*OverviewPageLocator.HEADER).text
