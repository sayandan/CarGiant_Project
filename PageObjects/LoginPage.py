import time

from Utilities.BasePage import BasePage
from selenium.webdriver.common.by import By


class LoginPage(BasePage):
    """By-locators"""
    POPUP_CLOSE_BUTTON = (By.CSS_SELECTOR, 'a.CallToActionPopupBlock__CallToActionLink-sc-1u8k8qw-0')
    LOGIN_BUTTON = (By.CSS_SELECTOR, 'a.sign-in-for-mygarage')
    USERNAME_TEXTBOX = (By.CSS_SELECTOR, 'input#PartialLogin_Username')
    PASSWORD_TEXTBOX = (By.CSS_SELECTOR, 'input#PartialLogin_Password')
    SIGNIN_BUTTON = (By.CSS_SELECTOR, "input[value='Sign in']")
    VERIFY_LOGIN = (By.XPATH, "//h3[contains(text(), 'Welcome')]")

    """constructor"""
    def __init__(self, driver):
        super().__init__(driver)

    """action methods"""
    def login(self, username, password):
        self.do_click(self.POPUP_CLOSE_BUTTON)
        self.do_click(self.LOGIN_BUTTON)
        self.do_send_keys(self.USERNAME_TEXTBOX, username)
        self.do_send_keys(self.PASSWORD_TEXTBOX, password)
        # self.do_click(self.SIGNIN_BUTTON)
        self.js_click(self.SIGNIN_BUTTON)

    def page_title(self, title):
        return self.get_title(title)

    def welcome_msg(self):
        return self.get_element_text(self.VERIFY_LOGIN)


