import unittest

from selenium.webdriver.common.by import By

from infra.ui_infra.browser_wrapper import BrowserWrapper
# from jira_report import JiraReport
from logic.ui_logic.search_product import SearchPage
from infra.ui_infra.config_handler import ConfigHandler


class TestSearchProduct(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.config_handler = ConfigHandler()
        cls.config = cls.config_handler.config
        cls.browser_wrapper = BrowserWrapper()
        cls.driver = cls.browser_wrapper.initialize_driver()

    def test_search_existing_product(self):
        search_page = SearchPage(self.driver)
        search_page.search_for_product(self.config["search_product"])
        search_page.click_search_button()
        search_page.go_back_to_home_page_click_logo()


    def test_search_nonexistent_product(self):
        search_page = SearchPage(self.driver)
        search_page.search_for_product(self.config["search_product_didnt_exist"])
        search_page.click_search_button()
        search_page.go_back_to_home_page_click_logo()



    # @classmethod
    # def tearDownClass(cls, self=None):
    #     cls.driver.quit()
    #
    #     #jira code
    #     if hasattr(self, '_outcome') and self._outcome.errors:
    #         try:
    #             # Assertion passed, report bug to Jira
    #             jira_report = JiraReport()
    #             issue_summary = "Test Assertion Failure"
    #             issue_description = "Test failed due to assertion failure in test_search_not_exist"
    #             jira_report.create_issue(issue_summary, issue_description)
    #             print("Issue Created")
    #         except Exception as e:
    #             print("Failed to report bug to Jira:", str(e))

if __name__ == "__main__":
    unittest.main()
