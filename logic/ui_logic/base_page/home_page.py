from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from infra.ui_infra.base_page import BasePage
import time


class HomePage(BasePage):
    LOGIN_BUTTON = (By.XPATH, '//a[@data-rb-event-key="#/login"]')
    PRODUCT_1_XPATH = "//strong[text()='Dragon Ball SUper - Vegito Figure (Super Saiyan God Super Saiyan)']"
    PRODUCT_2_XPATH = "//strong[text()='Fullmetal Alchemist - Group Vs. Pride Mug']"
    DROPDOWN_ARROW = (By.ID, 'username')
    PROFILE_BUTTON = (By.XPATH, "//a[@href='#/profile']")

    def click_on_sign_in_link(self):
        login_button = self.driver.find_element(*self.LOGIN_BUTTON)
        login_button.click()

    def open_user_dropdown(self):
        WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable(self.DROPDOWN_ARROW)
        ).click()
        time.sleep(2)
    def click_profile_button(self):
        self.open_user_dropdown()
        WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable(self.PROFILE_BUTTON)
        ).click()

    def click_product_1(self):
        product_one_element = self.driver.find_element(By.XPATH, self.PRODUCT_1_XPATH)
        self.driver.execute_script("arguments[0].scrollIntoView(true);", product_one_element)
        time.sleep(3)
        product_one_element.click()

    def click_product_2(self):
        product_2_element = self.driver.find_element(By.XPATH, self.PRODUCT_2_XPATH)
        self.driver.execute_script("arguments[0].scrollIntoView(true);", product_2_element)
        time.sleep(3)  # giving time for any lazy-loaded elements
        product_2_element.click()

    def navigate_to_home(self):
        home_button = self.driver.find_element(By.XPATH, '//a[@data-rb-event-key="#/login"]')
        home_button.click()
        time.sleep(3)

