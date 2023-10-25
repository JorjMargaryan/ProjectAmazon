from selenium import webdriver
from selenium.webdriver.common.by import By

from pages_.basePage import BasePage


class ProfilesPage(BasePage):
    def __init__(self, driver: webdriver.Chrome):
        super().__init__(driver)

        self.__profileSelectionLocator = (By.ID, "profile-pick-actor-button-0")
        self.__editProfileNameButtonLocator = (By.ID, "name-edit-modal-link")
        self.__profileNameInputFieldLocator = (By.ID, "profile-name-text-input")
        self.__saveChangesButtonLocator = (By.ID, "profile-name-edit-submit-button")
        self.__closeXButtonLocator = (By.CLASS_NAME, " a-button-close")
        self.__editMobileNumberButtonLocator = (By.ID, "mobile-number-edit-link")
        self.__editPinButtonLocator = (By.ID, "edit-pin-link")
        self.__shoppingButtonLocator = (By.ID, "profile-program-id-test-link")
        self.__profileNameLocator = (By.ID, "profile-name")
        self.__profileNameUpdateTooltipLocator = (By.XPATH, "//div[@class='a-changeover-inner']/strong")

    def select_profile(self):
        profileSelectionElement = self._find_element(self.__profileSelectionLocator)
        self._click_to_element(profileSelectionElement)

    def click_edit_profile_name_button(self):
        editProfileNameButtonElement = self._find_element(self.__editProfileNameButtonLocator)
        self._click_to_element(editProfileNameButtonElement)

    def fill_profile_name_field(self, name):
        profileNameInputFieldElement = self._find_element(self.__profileNameInputFieldLocator)
        self._fill_field(profileNameInputFieldElement, name)

    def get_profile_name(self):
        profileNameElement = self._find_element(self.__profileNameLocator)
        return self._get_element_text(profileNameElement)

    def validate_profile_name_update_tooltip(self):
        from testData_ import data
        profileNameUpdateTooltipElement = self._find_element(self.__profileNameUpdateTooltipLocator)
        assert self._get_element_text(profileNameUpdateTooltipElement) == data.profileNameUpdateTooltipText

    def click_save_changes_button(self):
        saveChangesButtonElement = self._find_element(self.__saveChangesButtonLocator)
        self._click_to_element(saveChangesButtonElement)

    def click_close_x_button(self):
        closeXButtonElement = self._find_element(self.__closeXButtonLocator)
        self._click_to_element(closeXButtonElement)

    def click_edit_mobile_number_button(self):
        editMobileNumberButtonElement = self._find_element(self.__editMobileNumberButtonLocator)
        self._click_to_element(editMobileNumberButtonElement)

    def click_edit_pin_button(self):
        editPinButtonElement = self._find_element(self.__editPinButtonLocator)
        self._click_to_element(editPinButtonElement)

    def click_shopping_button(self):
        shoppingButtonElement = self._find_element(self.__shoppingButtonLocator)
        self._click_to_element(shoppingButtonElement)
