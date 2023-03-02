from pages.base_page import BasePage
from pages.locators import MainPageLocators


class MainPage(BasePage):

    def start_game(self):
        start_game_button = self.is_element_present(*MainPageLocators.START_BUTTON)
        start_game_button.click()

