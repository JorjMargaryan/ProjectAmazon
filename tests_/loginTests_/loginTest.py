from selenium import webdriver
import unittest
from selenium.webdriver.support.events import EventFiringWebDriver

from common_.utilities_.customListener import CustomListener
from pages_.loginRegistration_.loginPage import LoginPage
from pages_.captchVerificationHandler import CaptchaVerificationHandler
from testData_ import data


class LoginTest(unittest.TestCase):
    def setUp(self) -> None:
        self.simpleDriver = webdriver.Chrome()
        self.driver = EventFiringWebDriver(self.simpleDriver, CustomListener())
        self.driver.delete_all_cookies()
        self.driver.implicitly_wait(10)
        self.driver.maximize_window()
        self.driver.get(data.signInUrl)
        self.captchaVerificationHandlerObj = CaptchaVerificationHandler(self.driver)

        # Captcha exception handler after navigation to login page
        self.captchaVerificationHandlerObj.captcha_handler_on_navigation_to_page_url()

    def test_positive_login(self):
        self.loginPageObj = LoginPage(self.driver)
        self.loginPageObj.fill_login_field(data.loginDataValid["username"])
        self.loginPageObj.click_continue_button()
        self.loginPageObj.fill_password_field(data.loginDataValid["password"])
        self.loginPageObj.click_signin_button()

        # Captcha exception handler after fill password field
        self.captchaVerificationHandlerObj.captcha_handler_after_login()

        self.accountWelcomeText = self.loginPageObj.get_account_welcome_text()
        self.assertNotEqual(self.accountWelcomeText, "Hello, sign in", "User has not been authorized")

    def test_negative_login_invalid_login(self):
        self.loginPageObj = LoginPage(self.driver)
        self.loginPageObj.fill_login_field(data.loginDataInvalidLogin["username"])
        self.loginPageObj.click_continue_button()
        self.loginPageObj.validate_incorrect_login_alert()

    def test_negative_login_invalid_password(self):
        self.loginPageObj = LoginPage(self.driver)
        self.loginPageObj.fill_login_field(data.loginDataValid["username"])
        self.loginPageObj.click_continue_button()
        self.loginPageObj.fill_password_field(data.loginDataInvalidPassword["password"])
        self.loginPageObj.click_signin_button()

        # Captcha exception handler after fill password field
        self.captchaVerificationHandlerObj.captcha_handler_after_login()
        self.loginPageObj.validate_incorrect_password_alert()

    def tearDown(self) -> None:
        self.driver.close()


if __name__ == "__main__":
    unittest.main()