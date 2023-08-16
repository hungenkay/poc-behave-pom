from selenium import webdriver

class Browser(object):

    driver = webdriver.Chrome()
    driver.implicitly_wait(30)
    driver.set_page_load_timeout(30)
    driver.maximize_window()

    def navigate(self, url):
        self.driver.get(url)

    def get_page_title(self):
        return self.driver.title

    def get_element(self, *locator):
        return self.driver.find_element(*locator)

    def get_element_by_text(self, text):
        return self.driver.find_element_by_link_text(text)

    def fill(self, text, *locator):
        self.driver.find_element(*locator).send_keys(text)
    
    def click_element(self, *locator):
        self.driver.find_element(*locator).click()

    def close(context):
        context.driver.close()
