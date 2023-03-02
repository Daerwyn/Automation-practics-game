import pytest
from selenium import webdriver
from selenium.webdriver.chrome.options import Options as Chrome_options


@pytest.fixture()
def get_chrome_options():
    options = Chrome_options()
    options.add_argument('chrome')
    options.add_argument('--start-maximized')
    options.add_argument('--disable-notifications')
    return options


@pytest.fixture()
def browser(get_chrome_options):
    options = get_chrome_options
    browser = webdriver.Chrome(options=options)
    yield browser
    browser.quit()
