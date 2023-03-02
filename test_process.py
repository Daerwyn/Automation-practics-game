import time

from pages.main_page import MainPage
from pages.first_step_page import FirstStepPage
from pages.second_stage_page import SecondStepPage
from pages.third_step_page import ThirdStepPage
from pages.fourth_step_page import FourthStepPage


def test_game_start(browser):
    link = "https://userinyerface.com"
    page = MainPage(browser, link)
    page.open()
    page.start_game()
    first = FirstStepPage(browser, browser.current_url)
    first.enter_password()
    first.enter_email()
    first.enter_domain()
    first.select_domain()
    first.accept_terms_checkbox()
    first.go_to_next_step()
    second = SecondStepPage(browser, browser.current_url)
    second.upload_image()
    second.select_checkboxes()
    second.go_to_next_step()
    third = ThirdStepPage(browser, browser.current_url)
    third.enter_first_name()
    third.enter_surname()
    third.enter_city()
    third.enter_street()
    third.enter_zip()
    third.choose_title()
    third.choose_country()
    third.number_and_box()
    third.choose_birthdate()
    third.choose_gender()
    third.slider_move()
    third.go_to_next_step()
    fourth = FourthStepPage(browser, browser.current_url)
    fourth.select_all()
    fourth.validate()
    time.sleep(15)
