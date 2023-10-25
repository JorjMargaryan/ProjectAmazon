from selenium import webdriver
from selenium.webdriver.common.by import By

from pages_.basePage import BasePage


class ProductDetailsPage(BasePage):
    def __init__(self, driver: webdriver.Chrome):
        super().__init__(driver)

        self.__addToCartButtonLocator = (By.ID, "add-to-cart-button")
        self.__addToCartConfirmationMessageLocator = (By.XPATH, "//div[@id='NATC_SMART_WAGON_CONF_MSG_SUCCESS']/span")
        self.__addToCartConfirmationCheckboxLocator = (By.XPATH, "//div[@id='NATC_SMART_WAGON_CONF_MSG_SUCCESS']/div/div/i")

    def click_add_to_cart_button(self):
        addToCartButtonElement = self._find_element(self.__addToCartButtonLocator)
        self._click_to_element(addToCartButtonElement)

    def validate_add_to_cart_confirmation_message(self):
        from testData_.data import addToCartConfirmationMessage
        confirmationMessageElement = self._find_element(self.__addToCartConfirmationMessageLocator)
        assert self._get_element_text(confirmationMessageElement) == addToCartConfirmationMessage

    def check_add_to_cart_confirmation_checkbox_icon_existence(self):
        assert self._element_should_be_visible(self.__addToCartConfirmationCheckboxLocator)
