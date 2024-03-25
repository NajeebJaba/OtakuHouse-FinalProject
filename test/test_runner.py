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



import unittest

def run_api_tests():
    loader = unittest.TestLoader()
    suite = loader.discover(start_dir='api_tests', pattern='test_api_profile_page.py')
    runner = unittest.TextTestRunner()
    print("\nRunning API tests...")
    runner.run(suite)

def run_ui_tests():
    loader = unittest.TestLoader()
    suite = loader.discover(start_dir='ui_tests', pattern='test_profile_page.py')
    runner = unittest.TextTestRunner()
    print("\nRunning UI tests...")
    runner.run(suite)

if __name__ == "__main__":
    run_api_tests()
    run_ui_tests()









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
