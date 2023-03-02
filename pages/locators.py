from selenium.webdriver.common.by import By


class MainPageLocators():
    START_BUTTON = (By.CSS_SELECTOR, "a.start__link")


class FirstStepPageLocators():
    PASSWORD_INPUT = (By.CSS_SELECTOR, "input.input.input--blue.input--gray[placeholder='Choose Password']")
    EMAIL_INPUT = (By.CSS_SELECTOR, "input.input.input--blue.input--gray[placeholder='Your email']")
    DOMAIN_INPUT = (By.CSS_SELECTOR, "input.input.input--blue.input--gray[placeholder='Domain']")
    DROPDOWN = (By.CSS_SELECTOR, "div.dropdown__header")
    DROPDOWN_2 = (By.XPATH, " //div[normalize-space()='.org']")
    CHECKBOX = (By.CSS_SELECTOR, "span.checkbox__box")
    NEXT_BUTTON = (By.XPATH, "//a[normalize-space()='Next']")


class SecondStepPageLocators():
    UPLOAD_BUTTON = (By.CSS_SELECTOR, "a.avatar-and-interests__upload-button")
    UNSELECT_CHECKBOX = (By.XPATH, "(//span[@class='icon icon-check checkbox__check'])[21]")
    CINNAMON_CHECKBOX = (By.XPATH, "(//span[@class='icon icon-check checkbox__check'])[20]")
    MULLETS_CHECKBOX = (By.XPATH, "(//span[@class='icon icon-check checkbox__check'])[19]")
    WINDOWS_CHECKBOX = (By.XPATH, "(//span[@class='icon icon-check checkbox__check'])[17]")
    NEXT_BUTTON = (By.XPATH, "//button[normalize-space()='Next']")


class ThirdStepPageLocators():
    FIRST_NAME_INPUT = (By.XPATH, "(//input[@placeholder='Placeholder...'])[1]")
    SURNAME_IPNUT = (By.XPATH, "(//input[@placeholder='Placeholder...'])[4]")
    STREET_INPUT = (By.XPATH, "(//input[@placeholder='Placeholder...'])[5]")
    ZIP_INPUT = (By.XPATH, "(//input[@placeholder='Placeholder...'])[2]")
    CITY_INPUT = (By.XPATH, "(//input[@placeholder='Placeholder...'])[3]")
    TITLE_DROPDOWN = (By.XPATH, "//div[contains(text(),'Choose a title')]")
    TITLE_MR = (By.XPATH, "//div[normalize-space()='Mr']")
    NUMBER_UP = (By.XPATH, "(//button)[9]")
    COUNTRY_DROPDOWN = (By.XPATH, "(//div[@class='dropdown__field'])[2]")
    FLAG = (By.XPATH, "//div[@class='flag flag-ax country-dropdown__flag-item']")
    BOX_UP = (By.XPATH, "(//button)[7]")
    DAY_DROPDOWN = (By.XPATH, "//div[contains(text(),'Day')]")
    DAY_25 = (By.XPATH, "//div[normalize-space()='25']")
    MONTH_DROPDOWN = (By.XPATH, "//div[contains(text(),'Month')]")
    MONTH_JULY = (By.XPATH, "//div[normalize-space()='July']")
    YEAR_DROPDOWN = (By.XPATH, "//div[contains(text(),'Year')]")
    YEAR_1997 = (By.XPATH, "(//div[@class='dropdown__list-item'])[146]")
    SLIDER = (By.XPATH, "//div[@class='slider__handle']")
    GENDER_MALE = (By.XPATH, "//div[@class='toggle-button toggle-button--left selected']")
    NEXT_BUTTON = (By.XPATH, "//button[@class='button button--stroked button--white']")


class FourthStepPageLocators():
    checkboxes = [(By.XPATH, f"(//span)[{i}]") for i in range(2, 48, 3)]
    VALIDATE_BUTTON = (By.XPATH, "//button[@class='button button--solid button--blue']")
