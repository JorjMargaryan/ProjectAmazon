import unittest
from selenium import webdriver

from pages_.captchVerificationHandler import CaptchaVerificationHandler
from pages_.navigationBar_.navigationBar import NavigationBar

from testData_.data import mainPageUrl


class BaseTestWithoutLogin(unittest.TestCase):
    """
        Base test class for setting up and tearing down the test environment.

        This class defines common setup and teardown methods for test cases.
        The `setUp` method initializes a Chrome WebDriver instance with common settings,
        and the `tearDown` method closes the WebDriver instance after each test case.

        Attributes:
            driver (webdriver.Chrome): The WebDriver instance for running tests.

        Usage:
            Subclasses of this base class can inherit these setup and teardown methods
            to configure the test environment for their specific test cases.
    """

    def setUp(self) -> None:
        self.driver = webdriver.Chrome()
        self.driver.delete_all_cookies()
        self.driver.implicitly_wait(10)
        self.driver.maximize_window()
        self.driver.get(mainPageUrl)

        # Captcha exception handler after navigation to main page
        self.captchaVerificationHandlerObj = CaptchaVerificationHandler(self.driver)
        self.captchaVerificationHandlerObj.captcha_handler_on_navigation_to_page_url()

        self.navigationBarObj = NavigationBar(self.driver)
        if not self.navigationBarObj.is_update_location_button_visible():
            self.driver.refresh()

    def tearDown(self) -> None:
        self.driver.close()
