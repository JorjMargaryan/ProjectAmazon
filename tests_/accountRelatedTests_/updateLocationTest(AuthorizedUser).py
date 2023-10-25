from tests_.baseTestWithLogin import BaseTestWithLogin
from pages_.navigationBar_.updateLocationPopup import UpdateLocationPopup
from pages_.navigationBar_.navigationBar import NavigationBar
from testData_.data import zipCodeData


class UpdateLocationTest(BaseTestWithLogin):
    def test_update_location_by_valid_zip_code(self):
        self.navigationBarObj = NavigationBar(self.driver)
        self.navigationBarObj.click_update_location_button()

        self.updateLocationPopupObj = UpdateLocationPopup(self.driver)
        if self.updateLocationPopupObj.check_the_change_button_existence():
            self.updateLocationPopupObj.click_change_button()
            self.updateLocationPopupObj.fill_zip_code_field(zipCodeData["validZipCode"])
            self.updateLocationPopupObj.click_apply_button()
            self.updateLocationPopupObj.click_done_button()
        else:
            self.updateLocationPopupObj.fill_zip_code_field(zipCodeData["validZipCode"])
            self.updateLocationPopupObj.click_apply_button()
            self.updateLocationPopupObj.click_continue_button()

            self.deliveryCountryName = self.updateLocationPopupObj.get_delivery_country_name()
            self.assertIn(str(zipCodeData["validZipCode"]), self.deliveryCountryName,
                          "AssertionError: The given valid zip code has not been updated")

    def test_update_location_by_country_selection(self):
        self.navigationBarObj.click_update_location_button()
        self.updateLocationPopupObj.open_country_dropdown()
        self.updateLocationPopupObj.select_country_from_dropdown()
        self.countryDropdownPlaceholder = self.updateLocationPopupObj.get_country_dropdown_placeholder_text()
        self.updateLocationPopupObj.click_done_button()

        self.deliveryCountryName = self.updateLocationPopupObj.get_delivery_country_name()
        self.assertEqual(self.countryDropdownPlaceholder, self.deliveryCountryName,
                         "AssertionError: The delivery country has not been updated.")

    def test_negative_update_location_by_invalid_zip_code(self):
        self.navigationBarObj.click_update_location_button()
        if self.updateLocationPopupObj.check_the_change_button_existence():
            self.updateLocationPopupObj.click_change_button()
            self.updateLocationPopupObj.fill_zip_code_field(zipCodeData["invalidZipCode"])
            self.updateLocationPopupObj.click_apply_button()
        else:
            self.updateLocationPopupObj.fill_zip_code_field(zipCodeData["invalidZipCode"])
            self.updateLocationPopupObj.click_apply_button()

        self.invalidZipCodeAlertText = self.updateLocationPopupObj.get_invalid_zip_code_validation_alert_text()
        self.assertEqual(self.invalidZipCodeAlertText, "Please enter a valid US zip code",
                         "AssertionError: Validation message for invalid zip code was not displayed")
