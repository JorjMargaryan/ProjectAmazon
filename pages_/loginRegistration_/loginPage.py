from selenium import webdriver
from selenium.webdriver.common.by import By

from pages_.basePage import BasePage


class LoginPage(BasePage):
    def __init__(self, driver: webdriver.Chrome):
        super().__init__(driver)

        self.__loginFieldLocator = (By.ID, "ap_email")
        self.__continueButtonLocator = (By.ID, "continue")
        self.__passwordFieldLocator = (By.ID, "ap_password")
        self.__signInButtonLocator = (By.ID, "signInSubmit")
        self.__errorMessageTitleLocator = (By.XPATH, "//div[@id='auth-error-message-box']/div/h4")
        self.__errorMessageTextLocator = (By.CLASS_NAME, "a-list-item")
        self.__accountWelcomeTextLocator = (By.ID, "nav-link-accountList-nav-line-1")

    def fill_login_field(self, login):
        loginFieldElement = self._find_element(self.__loginFieldLocator)
        self._fill_field(loginFieldElement, login)

    def click_continue_button(self):
        continueButtonElement = self._find_element(self.__continueButtonLocator)
        self._click_to_element(continueButtonElement)

    def fill_password_field(self, password):
        passwordFieldElement = self._find_element(self.__passwordFieldLocator)
        self._fill_field(passwordFieldElement, password)

    def click_signin_button(self):
        signInButtonElement = self._find_element(self.__signInButtonLocator)
        self._click_to_element(signInButtonElement)

    def validate_incorrect_login_alert(self):
        from testData_ import data
        loginAlertTitleElement = self._find_element(self.__errorMessageTitleLocator)
        assert self._get_element_text(loginAlertTitleElement) == data.invalidLoginAlert["title"]
        loginAlertTextElement = self._find_element(self.__errorMessageTextLocator)
        assert self._get_element_text(loginAlertTextElement) == data.invalidLoginAlert["text"]

    def validate_incorrect_password_alert(self):
        from testData_ import data
        passwordAlertTitleElement = self._find_element(self.__errorMessageTitleLocator)
        assert self._get_element_text(passwordAlertTitleElement) == data.invalidPasswordAlert["title"]
        passwordAlertTextElement = self._find_element(self.__errorMessageTextLocator)
        assert self._get_element_text(passwordAlertTextElement) == data.invalidPasswordAlert["text"]

    def get_account_welcome_text(self):
        accountWelcomeTextElement = self._find_element(self.__accountWelcomeTextLocator)
        return self._get_element_text(accountWelcomeTextElement)

    def quick_log_in(self, username, password):
        self.fill_login_field(username)
        self.click_continue_button()
        self.fill_password_field(password)
        self.click_signin_button()
