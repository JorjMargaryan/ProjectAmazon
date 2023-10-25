from selenium import webdriver
from selenium.webdriver.common.by import By

from pages_.basePage import BasePage
from common_.utilities_ import customLogger
from testData_.data import captchaElementTextSignIn, captchaElementTextPassword


class CaptchaVerificationHandler(BasePage):
    def __init__(self, driver: webdriver.Chrome):
        super().__init__(driver)

        self.__captchaLoginPageSectionLocator = (By.XPATH, "(//h4)[1]")
        self.__passwordFieldFirstCaptchaLocator = (By.CLASS_NAME, "a-size-large")
        self.__passwordFieldSecondCaptchaLocator = (By.XPATH, "//div[@id='image-captcha-section']/div/h4")

    def captcha_handler_on_navigation_to_page_url(self):
        if self._is_element_visible(self.__captchaLoginPageSectionLocator):
            captchaCheckElement = self._find_element(self.__captchaLoginPageSectionLocator)
            if self._get_element_text(captchaCheckElement) == captchaElementTextSignIn:
                customLogger.logger("ERROR", "Test failed due to captcha verification")
                exit(10)

    def captcha_handler_after_login(self):
        if self._is_element_visible(self.__passwordFieldFirstCaptchaLocator):
            passwordFieldCaptchaElement = self._find_element(self.__passwordFieldFirstCaptchaLocator)
            if self._get_element_text(passwordFieldCaptchaElement) == captchaElementTextPassword["firstCaptchaText"]:
                customLogger.logger("ERROR", "Test failed due to captcha verification")
                exit(10)
        elif self._is_element_visible(self.__passwordFieldSecondCaptchaLocator):
            passwordFieldCaptchaElement = self._find_element(self.__passwordFieldSecondCaptchaLocator)
            if self._get_element_text(passwordFieldCaptchaElement) == captchaElementTextPassword["secondCaptchaText"]:
                customLogger.logger("ERROR", "Test failed due to captcha verification")
                exit(10)
