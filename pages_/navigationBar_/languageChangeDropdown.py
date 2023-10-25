from selenium import webdriver

from pages_.basePage import BasePage


class LanguageChangeDropdown(BasePage):
    def __init__(self, driver: webdriver.Chrome):
        super().__init__(driver)
        pass
