"""serial"""
# import unittest
# from infra.ui_infra.browser_wrapper import BrowserWrapper
# from logic.ui_logic.base_page.home_page import HomePage
# from logic.ui_logic.login_page import LoginPage
# from infra.ui_infra.config_handler import ConfigHandler
# import time
#
#
# class TestProfilePage(unittest.TestCase):
#     @classmethod
#     def setUpClass(cls):
#         cls.config = ConfigHandler().config
#         cls.browser_wrapper = BrowserWrapper()
#         cls.driver = cls.browser_wrapper.initialize_driver()
#         cls.home_page = HomePage(cls.driver)
#         cls.login_page = LoginPage(cls.driver)
#
#     def setUp(self):
#         self.driver.get(self.config['url'])
#         time.sleep(2)
#
#     def test_navigate_to_profile_page(self):
#         # click on login button
#         self.home_page.click_on_sign_in_link()
#         time.sleep(2)
#
#         """login page"""
#         # enter username and password then click signin
#         self.login_page.enter_username(self.config["email"])
#         self.login_page.enter_password_and_login(self.config["password"])
#         time.sleep(3)
#
#         # from home page click on the dropdown and then click on profile button
#         self.home_page.click_profile_button()
#
#         # in profile page, wait for 15 seconds and don't do anything
#         time.sleep(10)
#
#     @classmethod
#     def tearDownClass(cls):
#         cls.driver.quit()
#
#
# if __name__ == "__main__":
#     unittest.main()



"""paralle"""

import unittest
from infra.ui_infra.browser_wrapper import BrowserWrapper
from logic.ui_logic.base_page.home_page import HomePage
from logic.ui_logic.login_page import LoginPage
from infra.ui_infra.config_handler import ConfigHandler
import concurrent.futures
import time


class TestProfilePage(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.config = ConfigHandler().config

    def run_profile_page_test_on_browser(self, browser_name):
        print(f"Running profile page test on {browser_name}")
        browser_wrapper = BrowserWrapper(browser_name=browser_name)
        driver = browser_wrapper.initialize_driver()

        try:
            home_page = HomePage(driver)
            login_page = LoginPage(driver)

            driver.get(self.config['url'])
            time.sleep(2)

            """Login page"""
            home_page.click_on_sign_in_link()
            time.sleep(2)
            login_page.enter_username(self.config["email"])
            login_page.enter_password_and_login(self.config["password"])
            time.sleep(3)

            """Profile page navigation"""
            home_page.click_profile_button()
            time.sleep(10)

        finally:
            driver.quit()

    def test_parallel_profile_page_navigation(self):
        with concurrent.futures.ThreadPoolExecutor() as executor:
            futures = {executor.submit(self.run_profile_page_test_on_browser, browser): browser for browser in
                       self.config["browser_types"]}
            for future in concurrent.futures.as_completed(futures):
                browser = futures[future]
                try:
                    future.result()
                except Exception as exc:
                    print(f'{browser} generated an exception: {exc}')
                else:
                    print(f'Profile page navigation test completed on {browser}')


if __name__ == "__main__":
    unittest.main()
