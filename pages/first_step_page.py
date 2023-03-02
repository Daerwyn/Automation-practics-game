from pages.base_page import BasePage
from pages.locators import FirstStepPageLocators


class FirstStepPage(BasePage):

    def enter_password(self):
        password_box = self.is_element_present(*FirstStepPageLocators.PASSWORD_INPUT)
        password_box.clear()
        password_box.send_keys("Password10203040")

    def enter_email(self):
        email_box = self.is_element_present(*FirstStepPageLocators.EMAIL_INPUT)
        email_box.clear()
        email_box.send_keys("mailname")

    def enter_domain(self):
        domain_box = self.is_element_present(*FirstStepPageLocators.DOMAIN_INPUT)
        domain_box.clear()
        domain_box.send_keys("zaporoze")

    def select_domain(self):
        domain = self.is_element_present(*FirstStepPageLocators.DROPDOWN)
        domain.click()
        domain_1 = self.is_element_present(*FirstStepPageLocators.DROPDOWN_2)
        domain_1.click()

    def accept_terms_checkbox(self):
        terms_checkbox = self.is_element_present(*FirstStepPageLocators.CHECKBOX)
        terms_checkbox.click()

    def go_to_next_step(self):
        button_next = self.is_element_present(*FirstStepPageLocators.NEXT_BUTTON)
        button_next.click()
