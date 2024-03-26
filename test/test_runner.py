# import unittest
#
# def run_api_tests():
#     loader = unittest.TestLoader()
#     suite = loader.discover(start_dir='api_tests', pattern='test_api_search_product.py')
#     runner = unittest.TextTestRunner()
#     print("\nRunning API tests...")
#     runner.run(suite)
#
# def run_ui_tests():
#     loader = unittest.TestLoader()
#     suite = loader.discover(start_dir='ui_tests', pattern='test_search_product.py')
#     runner = unittest.TextTestRunner()
#     print("\nRunning UI tests...")
#     runner.run(suite)
#
# if __name__ == "__main__":
#     run_api_tests()
#     run_ui_tests()


# import unittest
#
# def run_api_tests():
#     loader = unittest.TestLoader()
#     suite = loader.discover(start_dir='api_tests', pattern='test_api_profile_page.py')
#     runner = unittest.TextTestRunner()
#     print("\nRunning API tests...")
#     runner.run(suite)
#
# def run_ui_tests():
#     loader = unittest.TestLoader()
#     suite = loader.discover(start_dir='ui_tests', pattern='test_profile_page.py')
#     runner = unittest.TextTestRunner()
#     print("\nRunning UI tests...")
#     runner.run(suite)
#
# if __name__ == "__main__":
#     run_api_tests()
#     run_ui_tests()


#
# import argparse
# import unittest
#
#
# def run_api_tests(test_name):
#     loader = unittest.TestLoader()
#     if test_name == 'search':
#         suite = loader.discover(start_dir='api_tests', pattern='test_api_search_product.py')
#     elif test_name == 'profile':
#         suite = loader.discover(start_dir='api_tests', pattern='test_api_profile_page.py')
#     else:
#         print(f"No API test suite found for {test_name}")
#         return
#     runner = unittest.TextTestRunner()
#     print(f"\nRunning API tests for {test_name}...")
#     runner.run(suite)
#
#
# def run_ui_tests(test_name):
#     loader = unittest.TestLoader()
#     if test_name == 'search':
#         suite = loader.discover(start_dir='ui_tests', pattern='test_search_product.py')
#     elif test_name == 'profile':
#         suite = loader.discover(start_dir='ui_tests', pattern='test_profile_page.py')
#     else:
#         print(f"No UI test suite found for {test_name}")
#         return
#     runner = unittest.TextTestRunner()
#     print(f"\nRunning UI tests for {test_name}...")
#     runner.run(suite)
#
#
# if __name__ == "__main__":
#     parser = argparse.ArgumentParser(description='Run specific tests for API and UI.')
#     parser.add_argument('--test', type=str, help='Name of the test to run (e.g., search, profile)', required=True)
#
#     args = parser.parse_args()
#     test_name = args.test.lower()
#
#     run_api_tests(test_name)
#     run_ui_tests(test_name)


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
