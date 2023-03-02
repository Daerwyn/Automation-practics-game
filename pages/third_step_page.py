from pages.base_page import BasePage
from pages.locators import ThirdStepPageLocators
from selenium.webdriver import ActionChains


class ThirdStepPage(BasePage):

    def enter_first_name(self):
        first_name_input = self.is_element_present(*ThirdStepPageLocators.FIRST_NAME_INPUT)
        first_name_input.clear()
        first_name_input.send_keys('Tom')

    def enter_surname(self):
        surname_input = self.is_element_present(*ThirdStepPageLocators.SURNAME_IPNUT)
        surname_input.clear()
        surname_input.send_keys('Riddle')

    def enter_street(self):
        street_input = self.is_element_present(*ThirdStepPageLocators.STREET_INPUT)
        street_input.clear()
        street_input.send_keys('Kurchatova')

    def enter_city(self):
        city_input = self.is_element_present(*ThirdStepPageLocators.CITY_INPUT)
        city_input.clear()
        city_input.send_keys('London')

    def enter_zip(self):
        zip_input = self.is_element_present(*ThirdStepPageLocators.ZIP_INPUT)
        zip_input.clear()
        zip_input.send_keys('715-04')

    def choose_title(self):
        title_dropdown = self.is_element_present(*ThirdStepPageLocators.TITLE_DROPDOWN)
        title_dropdown.click()
        title_mr = self.is_element_present(*ThirdStepPageLocators.TITLE_MR)
        title_mr.click()

    def choose_country(self):
        country_dropdown = self.is_element_present(*ThirdStepPageLocators.COUNTRY_DROPDOWN)
        country_dropdown.click()
        flag = self.is_element_present(*ThirdStepPageLocators.FLAG)
        flag.click()

    def choose_birthdate(self):
        day_dropdown = self.is_element_present(*ThirdStepPageLocators.DAY_DROPDOWN)
        day_dropdown.click()
        day = self.is_element_present(*ThirdStepPageLocators.DAY_25)
        day.click()
        month_dropdown = self.is_element_present(*ThirdStepPageLocators.MONTH_DROPDOWN)
        month_dropdown.click()
        month = self.is_element_present(*ThirdStepPageLocators.MONTH_JULY)
        month.click()
        year_dropdown = self.is_element_present(*ThirdStepPageLocators.YEAR_DROPDOWN)
        year_dropdown.click()
        year = self.is_element_present(*ThirdStepPageLocators.YEAR_1997)
        year.click()

    def number_and_box(self):
        number = self.is_element_present(*ThirdStepPageLocators.NUMBER_UP)
        number.click()
        number.click()
        box = self.is_element_present(*ThirdStepPageLocators.BOX_UP)
        box.click()
        box.click()
        box.click()

    def choose_gender(self):
        gender_male = self.is_element_present(*ThirdStepPageLocators.GENDER_MALE)
        gender_male.click()

    def slider_move(self):
        slider = self.is_element_present(*ThirdStepPageLocators.SLIDER)
        distance = slider.size["width"] * 0.85
        action_chains = ActionChains(self.browser)
        action_chains.drag_and_drop_by_offset(slider, distance, 0).perform()

    def go_to_next_step(self):
        button_next = self.is_element_present(*ThirdStepPageLocators.NEXT_BUTTON)
        button_next.click()
