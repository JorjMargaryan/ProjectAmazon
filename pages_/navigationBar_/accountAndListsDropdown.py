from selenium import webdriver
from selenium.webdriver.common.by import By

from pages_.basePage import BasePage


class AccountListsDropdown(BasePage):
    def __init__(self, driver: webdriver.Chrome):
        super().__init__(driver)

        self.manageProfilesButtonLocator = (By.CLASS_NAME, "sc-fvEvSO jCeFih")

        # "Your Lists" area buttons
        self.createListButtonLocator = (By.LINK_TEXT, "Create a List")
        self.findListOrRegistryButtonLocator = (By.LINK_TEXT, "Find a List or Registry")

        # "Your Account" area buttons
        self.accountButtonLocator = (By.LINK_TEXT, "Account")
        self.ordersButtonLocator = (By.ID, "nav_prefetch_yourorders")
        self.recommendationsButtonLocator = (By.LINK_TEXT, "Recommendations")
        self.keepShoppingForButtonLocator = (By.LINK_TEXT, "Keep Shopping For")
        self.browsingHistoryButtonLocator = (By.LINK_TEXT, "Browsing History")
        self.watchlistButtonLocator = (By.LINK_TEXT, "Watchlist")
        self.videoPurchasesRentalsButtonLocator = (By.LINK_TEXT, "Video Purchases & Rentals")
        self.kindleUnlimitedButtonLocator = (By.LINK_TEXT, "Kindle Unlimited")
        self.contentDevicesButtonLocator = (By.LINK_TEXT, "Content & Devices")
        self.subscribeSaveItemsButtonLocator = (By.LINK_TEXT, "Subscribe & Save Items")
        self.membershipsSubscriptionsButtonLocator = (By.LINK_TEXT, "Memberships & Subscriptions")
        self.primeMembershipButtonLocator = (By.LINK_TEXT, "Prime Membership")
        self.amazonCreditCardsButtonLocator = (By.LINK_TEXT, "Amazon Credit Cards")
        self.musicLibraryButtonLocator = (By.LINK_TEXT, "Music Library")
        self.startSellingAccountButtonLocator = (By.LINK_TEXT, "Start a Selling Account")
        self.registerForFreeBusinessAccountButtonLocator = (By.LINK_TEXT, "Register for a free Business Account")
        self.customerServiceButtonLocator = (By.LINK_TEXT, "Customer Service")
        self.switchAccountsButtonLocator = (By.ID, "nav-item-switch-account")
        self.signOutButtonLocator = (By.ID, "nav-item-signout")

    def click_manage_profiles_button(self):
        manageProfilesButtonElement = self._find_element(self.manageProfilesButtonLocator)
        self._click_to_element(manageProfilesButtonElement)

    # "Your Lists" area buttons
    def click_create_list_button(self):
        createListButtonElement = self._find_element(self.createListButtonLocator)
        self._click_to_element(createListButtonElement)

    def click_find_list_or_registry_button(self):
        findListOrRegistryButtonElement = self._find_element(self.findListOrRegistryButtonLocator)
        self._click_to_element(findListOrRegistryButtonElement)

    # "Your Account" area buttons
    def click_account_button(self):
        accountButtonElement = self._find_element(self.accountButtonLocator)
        self._click_to_element(accountButtonElement)

    def click_orders_button(self):
        ordersButtonElement = self._find_element(self.ordersButtonLocator)
        self._click_to_element(ordersButtonElement)

    def click_recommendations_button(self):
        recommendationsButtonElement = self._find_element(self.recommendationsButtonLocator)
        self._click_to_element(recommendationsButtonElement)

    def click_keep_shopping_for_button(self):
        keepShoppingForButtonElement = self._find_element(self.keepShoppingForButtonLocator)
        self._click_to_element(keepShoppingForButtonElement)

    def click_browsing_history_button(self):
        browsingHistoryButtonElement = self._find_element(self.browsingHistoryButtonLocator)
        self._click_to_element(browsingHistoryButtonElement)

    def click_watchlist_button(self):
        watchlistButtonElement = self._find_element(self.watchlistButtonLocator)
        self._click_to_element(watchlistButtonElement)

    def click_video_purchases_rentals_button(self):
        videoPurchasesRentalsButtonElement = self._find_element(self.videoPurchasesRentalsButtonLocator)
        self._click_to_element(videoPurchasesRentalsButtonElement)

    def click_kindle_unlimited_button(self):
        kindleUnlimitedButtonElement = self._find_element(self.kindleUnlimitedButtonLocator)
        self._click_to_element(kindleUnlimitedButtonElement)

    def click_content_devices_button(self):
        contentDevicesButtonElement = self._find_element(self.contentDevicesButtonLocator)
        self._click_to_element(contentDevicesButtonElement)

    def click_subscribe_save_items_button(self):
        subscribeSaveItemsButtonElement = self._find_element(self.subscribeSaveItemsButtonLocator)
        self._click_to_element(subscribeSaveItemsButtonElement)

    def click_memberships_subscriptions_button(self):
        membershipsSubscriptionsButtonElement = self._find_element(self.membershipsSubscriptionsButtonLocator)
        self._click_to_element(membershipsSubscriptionsButtonElement)

    def click_prime_membership_button(self):
        primeMembershipButtonElement = self._find_element(self.primeMembershipButtonLocator)
        self._click_to_element(primeMembershipButtonElement)

    def click_amazon_credit_cards_button(self):
        amazonCreditCardsButtonElement = self._find_element(self.amazonCreditCardsButtonLocator)
        self._click_to_element(amazonCreditCardsButtonElement)

    def click_music_library_button(self):
        musicLibraryButtonElement = self._find_element(self.musicLibraryButtonLocator)
        self._click_to_element(musicLibraryButtonElement)

    def click_start_selling_account_button(self):
        startSellingAccountButtonElement = self._find_element(self.startSellingAccountButtonLocator)
        self._click_to_element(startSellingAccountButtonElement)

    def click_register_for_free_business_account_button(self):
        registerForFreeBusinessAccountButtonElement = self._find_element(self.registerForFreeBusinessAccountButtonLocator)
        self._click_to_element(registerForFreeBusinessAccountButtonElement)

    def click_customer_service_button(self):
        customerServiceButtonElement = self._find_element(self.customerServiceButtonLocator)
        self._click_to_element(customerServiceButtonElement)

    def click_sign_out_button(self):
        signOutButtonElement = self._find_element(self.signOutButtonLocator)
        self._click_to_element(signOutButtonElement)
