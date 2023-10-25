from selenium import webdriver
from selenium.webdriver.common.by import By

from pages_.basePage import BasePage


class SearchResultPage(BasePage):
    def __init__(self, driver: webdriver.Chrome):
        super().__init__(driver)

        self.firstProductLocator = (By.XPATH, "(//a[@class='a-link-normal s-no-outline'])[1]")

    def open_first_product(self):
        firstProductElement = self._find_element(self.firstProductLocator)
        self._click_to_element(firstProductElement)
