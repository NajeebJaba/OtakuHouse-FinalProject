

import sys
sys.path.append('C:/Users/ASUS/OneDrive/מסמכים/GitHub/OtakuHouse-FinalProject')
import unittest

"""to run all the tests i need to take the imports"""
# import test classes from their respective files.
from api_tests.test_api_profile_page import TestProfilePage as TestAPIProfilePage
from api_tests.test_api_review_product import TestReviewProduct as TestAPIReviewProduct
from ui_tests.test_profile_page import TestProfilePage as TestUIProfilePage
from ui_tests.test_review_product import TestProductPageToSeeReview as TestUIReviewProduct

"""function to run API test suite. """


# this function aggregates all API tests into a single suite for execution.
def test_run_api_suite():
    # testSuite object to collect tests.
    api_suite = unittest.TestSuite()
    # testLoader to find and load tests from the test cases.
    loader = unittest.TestLoader()
    """Add API test cases to the suite."""
    # The loadTestsFromTestCase method dynamically loads all test methods from a TestCase.
    api_suite.addTests(loader.loadTestsFromTestCase(TestAPIProfilePage))
    api_suite.addTests(loader.loadTestsFromTestCase(TestAPIReviewProduct))
    runner = unittest.TextTestRunner(verbosity=2)
    # run the test suite.
    runner.run(api_suite)


"""above code was to run API tests , now I will run UI tests """
# function to run UI test suite.
"""same notes for API , just now for UI"""


def test_run_ui_suite():
    ui_suite = unittest.TestSuite()
    loader = unittest.TestLoader()
    """" add UI test cases to the suite."""
    ui_suite.addTests(loader.loadTestsFromTestCase(TestUIProfilePage))
    ui_suite.addTests(loader.loadTestsFromTestCase(TestUIReviewProduct))
    runner = unittest.TextTestRunner(verbosity=2)
    runner.run(ui_suite)


""" main execution """
if __name__ == '__main__':
    # run API suite first.
    test_run_api_suite()
    # following the API tests, run the UI suite.
    test_run_ui_suite()
