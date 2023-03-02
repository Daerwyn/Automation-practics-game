import os
import autoit

from pages.base_page import BasePage
from pages.locators import SecondStepPageLocators


class SecondStepPage(BasePage):

    def upload_image(self):
        upload_button = self.is_element_present(*SecondStepPageLocators.UPLOAD_BUTTON)
        current_dir = os.path.abspath(os.path.dirname(__file__))
        file_path = os.path.join(current_dir, 'avatar.png')
        upload_button.click()
        autoit.win_wait_active("[CLASS:#32770]", 3)
        autoit.control_set_text("[CLASS:#32770]", "Edit1", file_path)
        autoit.control_click("[CLASS:#32770]", "Button1")

    def select_checkboxes(self):
        unselect_all = self.is_element_present(*SecondStepPageLocators.UNSELECT_CHECKBOX)
        cinnamon_checkbox = self.is_element_present(*SecondStepPageLocators.CINNAMON_CHECKBOX)
        mullets_checkbox = self.is_element_present(*SecondStepPageLocators.MULLETS_CHECKBOX)
        windows_checkbox = self.is_element_present(*SecondStepPageLocators.WINDOWS_CHECKBOX)
        unselect_all.click()
        cinnamon_checkbox.click()
        mullets_checkbox.click()
        windows_checkbox.click()

    def go_to_next_step(self):
        button_next = self.is_element_present(*SecondStepPageLocators.NEXT_BUTTON)
        button_next.click()
