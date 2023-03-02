from pages.base_page import BasePage
from pages.locators import FourthStepPageLocators


class FourthStepPage(BasePage):

    def select_all(self):
        checkboxes = [self.is_element_present(*loc) for loc in FourthStepPageLocators.checkboxes]
        for checkbox in checkboxes:
            checkbox.click()

    def validate(self):
        validate_button = self.is_element_present(*FourthStepPageLocators.VALIDATE_BUTTON)
        validate_button.click()
