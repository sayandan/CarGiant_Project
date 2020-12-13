from selenium.webdriver.common.by import By

from Utilities.BasePage import BasePage


class MyGarage(BasePage):
    """By Locators"""
    MY_GARAGE_LINK = (By.LINK_TEXT, 'My Garage')
    PAGE_NUMBER_BUTTONS = (By.XPATH, "//li[@role='presentation']")
    CAR_DETAIL_TEXT = (By.CSS_SELECTOR, 'div#slick-slide00 h5')
    REMOVE_BUTTON = (By.CSS_SELECTOR, 'div#slick-slide00 div p a')
    NEXT_BUTTON = (By.CSS_SELECTOR, 'span.watch-next')

    """Constructor"""
    def __init__(self, driver):
        super().__init__(driver)

    """Action methods"""
    def

