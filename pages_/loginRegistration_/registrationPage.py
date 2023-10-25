from selenium import webdriver

from pages_.basePage import BasePage


class RegistrationPage(BasePage):
    def __init__(self, driver: webdriver.Chrome):
        super().__init__(driver)
        pass
