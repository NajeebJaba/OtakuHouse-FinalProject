from infra.ui_infra.base_page import BasePage
from selenium.webdriver.common.by import By
import time


class SearchPage(BasePage):
    SEARCH_INPUT = (By.XPATH, "//input[@name='q']")
    SEARCH_BUTTON = (By.XPATH, "//button[contains(text(),'Search')]")
    # GO_BACK_LINK = (By.XPATH, "//a[contains(text(),'Go Back')]")
    LOGO = (By.XPATH, "//img[@alt='Otaku Shop']")
    PRODUCT_IMAGE_XPATH =  "//img[@class='card-img' and contains(@src, '/media/images/ichigo_shirt.jpg')]"
    # PRODUCT_IMAGE_XPATH = "//img[@src='/media/images/mikasajacket.jpg' and @alt='Attack On Titan - Mikasa Battle Long Sleeve']"

    def search_for_product(self, product_name):
        search_input = self.driver.find_element(*self.SEARCH_INPUT)
        search_input.send_keys(product_name)
        time.sleep(3)

    def click_search_button(self):
        search_button = self.driver.find_element(*self.SEARCH_BUTTON)
        search_button.click()
        time.sleep(3)

    def click_on_product(self):
        # If you want to use it within the method only, declare it here.
        product_image_xpath = "//img[@class='card-img' and contains(@src, '/media/images/ichigo_shirt.jpg')]"
        product_element = self.driver.find_element(By.XPATH, product_image_xpath)
        product_element.click()

    def go_back_to_home_page_click_logo(self):
        logo_click = self.driver.find_element(*self.LOGO)
        logo_click.click()
        time.sleep(2)
