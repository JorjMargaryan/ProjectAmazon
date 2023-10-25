from tests_.baseTestWithLogin import BaseTestWithLogin
from pages_.navigationBar_.navigationBar import NavigationBar
from pages_.navigationBar_.accountAndListsDropdown import AccountListsDropdown
from pages_.accountPage import AccountPage
from pages_.profilesPage import ProfilesPage


class ChangeProfileNameTest(BaseTestWithLogin):
    def test_changing_user_name(self):
        self.navigationBarObj = NavigationBar(self.driver)
        self.navigationBarObj.hover_over_account_lists_dropdown()

        self.accountListsDropdownObj = AccountListsDropdown(self.driver)
        self.accountListsDropdownObj.click_account_button()

        self.accountPageObj = AccountPage(self.driver)
        self.accountPageObj.click_your_profiles_button()

        self.profilesPageObj = ProfilesPage(self.driver)
        self.profilesPageObj.select_profile()
        self.profileNameBeforeChange = self.profilesPageObj.get_profile_name()
        self.profilesPageObj.click_edit_profile_name_button()

        import random_name_generator as rng
        self.randomName = rng.generate_one(rng.Descent.ENGLISH, sex=rng.Sex.MALE)
        self.profilesPageObj.fill_profile_name_field(self.randomName)
        while self.profileNameBeforeChange == self.randomName:
            self.randomName = rng.generate_one(rng.Descent.ENGLISH, sex=rng.Sex.MALE)
            self.profilesPageObj.fill_profile_name_field(self.randomName)
        self.profilesPageObj.click_save_changes_button()

        self.profilesPageObj.validate_profile_name_update_tooltip()
        self.profileNameAfterChange = self.profilesPageObj.get_profile_name()
        self.assertNotEqual(self.profileNameBeforeChange, self.profileNameAfterChange,
                            "AssertionError: The profile name has not been updated.")
