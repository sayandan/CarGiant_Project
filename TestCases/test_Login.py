from PageObjects.LoginPage import LoginPage
from Utilities.BaseTest import BaseTest
from Utilities.TestData import TestData


class TestLogin(BaseTest):

    def test_001_homepage_title(self):
        self.logger = self.get_logger()
        self.logger.info("***************TTest_001_Login************")
        self.logger.info("************verifying home page title")
        actual_title = self.driver.title

        if actual_title == TestData.PAGE_TITLE:
            assert True
            self.logger.info("*************home page title verity success**")
        else:
            self.driver.save_screenshot('../Reports/test_homePageTitle.png')
            self.logger.error("*****home page title test failed")
            assert False

    def test_002_login(self):
        self.logger = self.get_logger()
        self.logger.info("******login test***********")
        self.login_page = LoginPage(self.driver)
        self.login_page.login(TestData.USERNAME, TestData.PASSWORD)

        actual_title = self.login_page.page_title(TestData.LOGIN_TITLE)

        if actual_title == TestData.LOGIN_TITLE:
            self.logger.info("**********Veritying login title password ****")
            assert True
        else:
            self.logger.error("********login test failed **********")
            self.driver.save_screenshot('../Reports/test_login.png')
            assert False

    def test_003_login_page_message(self):
        self.login_page = LoginPage(self.driver)
        self.logger = self.get_logger()
        self.logger.info("**********verifying loginpage welcome message*****")
        actual_title = self.login_page.welcome_msg()

        if TestData.LOGIN_VERIFY_TEXT in actual_title:
            self.logger.info("**********login page welcome message test passed***")
            assert True
        else:
            self.logger.error("*********login page welcome message verify failed")
            self.driver.save_screenshot('../Reports/login_page_message.png')
            assert False



