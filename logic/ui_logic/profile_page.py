from selenium.webdriver.common.by import By
from infra.ui_infra.base_page import BasePage
import time

class ProfilePage(BasePage):
    PROFILE_BUTTON = (By.XPATH, '//a[@href="#/profile"]')
    UPDATE_NAME_INPUT = (By.ID, 'name')
    EMAIL_INPUT = (By.ID, 'email')
    PASSWORD_INPUT = (By.ID, 'password')
    CONFIRM_PASSWORD_INPUT = (By.ID, 'passwordConfirm')
    UPDATE_BUTTON = (By.XPATH, "//button[@type='submit' and contains(@class, 'btn-primary')]")

    def update_profile(self, name, email, password, confirm_password):
        self.driver.find_element(*self.UPDATE_NAME_INPUT).clear()
        self.driver.find_element(*self.UPDATE_NAME_INPUT).send_keys(name)
        self.driver.find_element(*self.EMAIL_INPUT).clear()
        self.driver.find_element(*self.EMAIL_INPUT).send_keys(email)
        self.driver.find_element(*self.PASSWORD_INPUT).clear()
        self.driver.find_element(*self.PASSWORD_INPUT).send_keys(password)
        self.driver.find_element(*self.CONFIRM_PASSWORD_INPUT).clear()
        self.driver.find_element(*self.CONFIRM_PASSWORD_INPUT).send_keys(confirm_password)
        self.driver.find_element(*self.UPDATE_BUTTON).click()
        time.sleep(3)

    def submit_update(self):
        self.driver.find_element(*self.UPDATE_BUTTON).click()
        time.sleep(3)
