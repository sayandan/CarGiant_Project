import pytest
from selenium.common.exceptions import NoSuchElementException

from PageObjects.FindCar import FindCar
from PageObjects.LoginPage import LoginPage
from Utilities.BaseTest import BaseTest
from Utilities.TestData import TestData


class TestFindCar(BaseTest):
    car_flag_all = []

    def test_004_login(self):
        self.logger = self.get_logger()
        self.logger.info("***********Test_002_FindCar**********")
        self.logger.info("******* test_004_login    ******")
        self.login_page = LoginPage(self.driver)
        self.login_page.login(TestData.USERNAME, TestData.PASSWORD)
        self.logger.info("**********logged in***********")

    def test_005_find_car(self, get_data):
        self.logger = self.get_logger()
        self.find_car = FindCar(self.driver)
        try:
            self.find_car.search_car(get_data["Make"], get_data["Model"])
            self.logger.info("searching for car " + get_data["Make"] + ' ' + get_data["Model"])
        except NoSuchElementException:
            self.logger.exception("*********the car is no longer listed****")

        self.logger.info("********testing result title header*****")
        result_header = self.find_car.verify_search_header()
        if result_header == TestData.RESULTS_HEADER:
            self.logger.info("***********verify result header success****")
            assert True
        else:
            self.logger.error("**********result page verify failed********")
            self.driver.save_screenshot('../Reports/test_find_car.png')
            assert False

        self.logger.info("***********getting car details***********")
        try:
            self.car_flag = self.find_car.add_to_watchlist(get_data["Detail"])
            self.car_flag.insert(0, get_data["Make"])
            self.car_flag.insert(1, get_data["Model"])
            self.logger.info("*****looking for :" + str(self.car_flag))
        except NoSuchElementException:
            self.logger.error(get_data["Make"] + ' ' + get_data["Make"] + ' ' + get_data["Detail"])
            self.logger.error("************not available to add to the watch list*******")
            self.car_flag = [get_data["Make"], get_data["Make"], get_data["Detail"], 'Listed', 'Not Clickable']

        self.car_flag_all.append(self.car_flag)
        self.logger.info(str(self.car_flag_all))

    def test_006_my_car(self):
        print(str(self.car_flag_all))

    @pytest.fixture(params=(
            {"Make":  "Honda", "Model":  "Civic", "Detail": "4 Dr Hatch, Auto, Petrol, White, 2016 (16), 46,018 miles"},
            {"Make":  "Audi", "Model":  "Q2", "Detail": "SUV, Manual, Petrol, White, 2017 (67), 29,744 miles"},
            {"Make": "Ford", "Model": "Focus", "Detail": "5 Dr Hatch, Manual, Diesel, Blue, 2015 (65), 59,427 miles"},
            {"Make": "Ford", "Model": "Focus", "Detail": "Estate, Manual, Diesel, Grey, 2016 (16), 62,594 miles"},
            {"Make":  "BMW", "Model":  "All 7-series", "Detail": "Saloon, Auto, Diesel, Grey, 2016 (66), 20,834 miles"}
    ))
    def get_data(self, request):
        return request.param
