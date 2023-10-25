from selenium import webdriver
from selenium.webdriver.common.by import By

from pages_.basePage import BasePage


class AccountPage(BasePage):
    def __init__(self, driver: webdriver.Chrome):
        super().__init__(driver)

        self.yourOrdersButtonLocator = (By.XPATH, "(//a[@class='ya-card__whole-card-link'])[1]")
        self.loginSecurityButtonLocator = (By.XPATH, "(//a[@class='ya-card__whole-card-link'])[2]")
        self.primeButtonLocator = (By.XPATH, "(//a[@class='ya-card__whole-card-link'])[3]")
        self.yourAddressesButtonLocator = (By.XPATH, "(//a[@class='ya-card__whole-card-link'])[4]")
        self.giftCardsButtonLocator = (By.XPATH, "(//a[@class='ya-card__whole-card-link'])[5]")
        self.yourPaymentsButtonLocator = (By.XPATH, "(//a[@class='ya-card__whole-card-link'])[6]")
        self.yourProfilesButtonLocator = (By.XPATH, "(//a[@class='ya-card__whole-card-link'])[7]")
        self.digitalServicesButtonLocator = (By.XPATH, "(//a[@class='ya-card__whole-card-link'])[8]")
        self.archivedOrdersButtonLocator = (By.XPATH, "(//a[@class='ya-card__whole-card-link'])[9]")
        self.yourListsButtonLocator = (By.XPATH, "(//a[@class='ya-card__whole-card-link'])[10]")
        self.customerServiceButtonLocator = (By.XPATH, "(//a[@class='ya-card__whole-card-link'])[11]")
        self.yourMessagesButtonLocator = (By.XPATH, "(//a[@class='ya-card__whole-card-link'])[12]")
        self.amazonBusinessButtonLocator = (By.XPATH, "(//a[@class='ya-card__whole-card-link'])[13]")


    def click_your_orders_button(self):
        yourOrdersButtonElement = self._find_element(self.yourOrdersButtonLocator)
        self._click_to_element(yourOrdersButtonElement)

    def click_login_security_button(self):
        loginSecurityButtonElement = self._find_element(self.loginSecurityButtonLocator)
        self._click_to_element(loginSecurityButtonElement)

    def click_prime_button(self):
        primeButtonElement = self._find_element(self.primeButtonLocator)
        self._click_to_element(primeButtonElement)

    def click_your_addresses_button(self):
        yourAddressesButtonElement = self._find_element(self.yourAddressesButtonLocator)
        self._click_to_element(yourAddressesButtonElement)

    def click_gift_cards_button(self):
        giftCardsButtonElement = self._find_element(self.giftCardsButtonLocator)
        self._click_to_element(giftCardsButtonElement)

    def click_your_payments_button(self):
        yourPaymentsButtonElement = self._find_element(self.yourPaymentsButtonLocator)
        self._click_to_element(yourPaymentsButtonElement)

    def click_your_profiles_button(self):
        yourProfilesButtonElement = self._find_element(self.yourProfilesButtonLocator)
        self._click_to_element(yourProfilesButtonElement)

    def click_digital_services_button(self):
        digitalServicesButtonElement = self._find_element(self.digitalServicesButtonLocator)
        self._click_to_element(digitalServicesButtonElement)

    def click_archived_orders_button(self):
        archivedOrdersButtonElement = self._find_element(self.archivedOrdersButtonLocator)
        self._click_to_element(archivedOrdersButtonElement)

    def click_your_lists_button(self):
        yourListsButtonElement = self._find_element(self.yourListsButtonLocator)
        self._click_to_element(yourListsButtonElement)

    def click_customer_service_button(self):
        customerServiceButtonElement = self._find_element(self.customerServiceButtonLocator)
        self._click_to_element(customerServiceButtonElement)

    def click_your_messages_button(self):
        yourMessagesButtonElement = self._find_element(self.yourMessagesButtonLocator)
        self._click_to_element(yourMessagesButtonElement)

    def click_amazon_business_button(self):
        amazonBusinessButtonElement = self._find_element(self.amazonBusinessButtonLocator)
        self._click_to_element(amazonBusinessButtonElement)
