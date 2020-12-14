import time
from selenium.webdriver.common.by import By
from Utilities.BasePage import BasePage

car_flag = []

class FindCar(BasePage):

    """By locators"""
    FIND_CAR_BUTTON =(By.XPATH, "//ul[@class='menu__top']/li[1]")
    MAKE_DROPDOWN = (By.XPATH, "//a[contains(text(), 'Make')]")
    MAKE_LISTS = (By.XPATH, "//select[@data-source='MakeOptions']/parent::div[@tabindex='0']/div[1]/div[1]/a")
    MODEL_DROPDOWN = (By.XPATH, "//a[contains(text(), 'Model')]")
    MODEL_LISTS = (By.XPATH, "//select[@data-source='ModelOptions']/parent::div[@tabindex='1']/div[1]/div[1]/a")
    SEARCH_BUTTON = (By.XPATH, "//button[@type='submit']")

    VERIFY_RESULTS = (By.XPATH, "//div[@class='row']/h1")
    CAR_DETAIL_TEXT = (By.XPATH, "//div[@class='vehicle-tile__detail']/p")

    """constructor"""
    def __init__(self, driver):
        super().__init__(driver)

    def search_car(self, make, model):
        self.do_click(self.FIND_CAR_BUTTON)
        self.do_click(self.MAKE_DROPDOWN)
        time.sleep(2)
        make_lists = self.get_elements(self.MAKE_LISTS)
        for make_list in make_lists:
            if make in make_list.text:
                print('\n' + make_list.text)
                make_list.click()
                break
        self.do_click(self.MODEL_DROPDOWN)
        time.sleep(2)
        model_lists = self.get_elements(self.MODEL_LISTS)
        for model_list in model_lists:
            if model in model_list.text:
                print(model_list.text)
                model_list.click()
                break
        self.do_click(self.SEARCH_BUTTON)

    def verify_search_header(self):
        return self.get_element_text(self.VERIFY_RESULTS)

    def add_to_watchlist(self, car_detail):
        cars = self.get_elements(self.CAR_DETAIL_TEXT)
        global car_flag
        car_flag = [car_detail, 'Not Listed', 'SOLD TODAY']
        for car in cars:
            if car_detail == car.text:
                print(car.text + ' ' + car.find_element_by_xpath("ancestor::article/div/a").text)
                time.sleep(2)
                if car.find_element_by_xpath("ancestor::article/div/a").text == 'SOLD TODAY':
                    print('Element not clickable')
                    car_flag[1] = 'Listed'
                    car_flag[2] = 'SOLD TODAY'
                    print(car_flag)

                watch_list = car.find_element_by_xpath("ancestor::article/div/div[@class='vehicle-tile__actions']/a[text()='Add to watchlist']")
                if watch_list.is_displayed():
                    print('Element clickable')
                    car_flag[1] = 'Listed'
                    car_flag[2] = 'NOT SOLD'
                    print(car_flag)
                    self.driver.execute_script("arguments[0].click();", watch_list)  # Javascript click
                break
        return car_flag












