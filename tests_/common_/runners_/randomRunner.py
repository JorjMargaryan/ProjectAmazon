import unittest

from tests_.common_.suits_.testSuits import TestSuites
from common_.htmlRunner_.htmlRunner import HtmlRunner

if __name__ == "__main__":
    testSuites = TestSuites()
    suite = testSuites.get_random_suite()

    htmlRunner = HtmlRunner()
    runner = htmlRunner.get_html_runner("Random Suite","Random Suite description")
    runner.run(suite)

    # runner = unittest.TextTestRunner()
    # runner.run(suite)
