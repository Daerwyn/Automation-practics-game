from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec


class BasePage():

    def __init__(self, browser, url):
        self.browser = browser
        self.url = url
        self.wait = WebDriverWait(browser, 30, 0.3)

    def open(self):
        self.browser.get(self.url)

    def is_element_present(self, how, what):
        return self.wait.until(ec.visibility_of_element_located((how, what)))

    def is_element_clickable(self, how, what):
        return self.wait.until(ec.element_to_be_clickable((how, what)))
