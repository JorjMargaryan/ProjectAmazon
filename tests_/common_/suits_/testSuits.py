import unittest
from tests_.loginTests_.loginTest import LoginTest
from tests_.accountRelatedTests_.changeProfileNameTest import ChangeProfileNameTest

class TestSuites():
    def get_smoke_suite(self):
        pass

    def get_regression_suite(self):
        pass

    def get_performance_suite(self):
        pass

    def get_random_suite(self):
        suite = unittest.TestSuite()
        suite.addTest(LoginTest('test_positive_login'))
        # suite.addTest(LoginTest('test_negative_login_invalid_login'))
        # suite.addTest(LoginTest('test_negative_login_invalid_password'))
        # suite.addTest(ChangeProfileNameTest('test_changing_user_name'))
        return suite

    def get_functional_suite(self):
        pass

    def get_integration_suite(self):
        pass

    def get_end_to_end_suite(self):
        pass

    def get_security_suite(self):
        pass

    def get_usability_suite(self):
        pass

    def get_compatibility_suite(self):
        pass

    def get_installation_suite(self):
        pass

    def get_localization_suite(self):
        pass

    def get_ad_hoc_suite(self):
        pass

    def get_sanity_suite(self):
        pass

    def get_acceptance_suite(self):
        pass

    def get_alpha_and_beta_suite(self):
        pass

