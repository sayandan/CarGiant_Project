import time
from selenium.webdriver.common.by import By
from Utilities.BasePage import BasePage
from Utilities.TestData import TestData


class MyGarage(BasePage):
    """By Locators"""
    MY_GARAGE_LINK = (By.LINK_TEXT, 'My Garage')
    PAGE_NUMBER_BUTTONS = (By.XPATH, "//li[@role='presentation']")
    FIRST_PAGE_BUTTON = (By.XPATH, "//button[@id='slick-slide-control00' and @aria-selected='true']")
    #CAR_DETAIL_TEXT = (By.CSS_SELECTOR, 'div#slick-slide00 h5')
    CAR_DETAIL_TEXT =(By.CSS_SELECTOR, 'div.slick-current h5')
    REMOVE_BUTTON = (By.CSS_SELECTOR, 'div#slick-slide00 div p a')
    REMOVE_ALL_BUTTON = (By.LINK_TEXT, 'Remove from watchlist')
    NEXT_BUTTON = (By.CSS_SELECTOR, 'span.watch-next')

    """Constructor"""
    def __init__(self, driver):
        super().__init__(driver)

    """Action methods"""
    def compare_watch_list(self):
        actual_watch_list = []

        # while self.is_visible(self.FIRST_PAGE_BUTTON):  # move to first page
        #     self.js_click(self.NEXT_BUTTON)

        no_of_pages = len(self.get_elements(self.PAGE_NUMBER_BUTTONS))
        print('\n')
        for i in range(no_of_pages):
            # by_element = (By.CSS_SELECTOR, 'div#slick-slide0' + str(i) + ' h5')
            print(self.get_element_text(self.CAR_DETAIL_TEXT))
            # watch_list.append(self.get_element_text(by_element))
            actual_watch_list.append(list(self.get_element_text(self.CAR_DETAIL_TEXT).split(", ")))
            self.js_click(self.NEXT_BUTTON)
            time.sleep(2)
        print(actual_watch_list)
        return actual_watch_list

    def delete_all_watch_list(self):
        self.do_click(self.MY_GARAGE_LINK)
        while self.is_visible(self.REMOVE_ALL_BUTTON):
            self.js_click(self.REMOVE_ALL_BUTTON)
            print('\n' + 'Deleting watch list....')
            time.sleep(2)



