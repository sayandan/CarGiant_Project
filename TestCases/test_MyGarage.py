import json
from PageObjects.LoginPage import LoginPage
from PageObjects.MyGarage import MyGarage
from Utilities.BaseTest import BaseTest
from Utilities.TestData import TestData


class TestMyGarage(BaseTest):

    def test_06_login(self):
        self.logger = self.get_logger()
        self.logger.info("***********Test_My Garage **********")
        self.logger.info("******* test_06_login    ******")
        self.login_page = LoginPage(self.driver)
        self.login_page.login(TestData.USERNAME, TestData.PASSWORD)
        self.logger.info("**********logged in***********")
        self.my_garage = MyGarage(self.driver)

    def test_07_compare_watch_list(self):
        expected_watch_list = []
        self.logger = self.get_logger()
        self.logger.info("***************test compare watch list************")
        self.logger.info("************test 07 compare ***********")
        self.my_garage = MyGarage(self.driver)
        actual_watch_list = self.my_garage.compare_watch_list()
        self.logger.info(actual_watch_list)

        with open('../Utilities/watchlist.txt', 'r') as file_handle:
            car_list = json.load(file_handle)

        for i in range(len(car_list)):
            if car_list[i][3] == 'Listed':
                if car_list[i][4] == 'NOT SOLD':
                    l = list(car_list[i][2].split(", "))  # convert string to list, delimiter ', '
                    expected_watch_list.append(l[2:])  # remove the first two element of the list
        print(expected_watch_list)
        self.logger.info(expected_watch_list)

        if actual_watch_list.sort() == expected_watch_list.sort():
            self.logger.info("*******expected watch list matches actual watch list*********")
            assert True
        else:
            self.driver.save_screenshot('../Reports/test_compare_list.png')
            self.logger.error("**********Comparing watch list failed********")
            assert False
