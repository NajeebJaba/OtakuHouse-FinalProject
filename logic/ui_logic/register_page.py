from selenium.webdriver.common.by import By
from infra.ui_infra.base_page import BasePage
import time


class RegisterPage(BasePage):
    NAME_INPUT = (By.ID, 'name')
    EMAIL_INPUT = (By.ID, 'email')
    PASSWORD_INPUT = (By.ID, 'password')
    CONFIRM_PASSWORD_INPUT = (By.ID, 'passwordConfirm')
    REGISTER_BUTTON = (By.XPATH, "//button[@type='submit' and contains(@class, 'btn-primary')]")

    def fill_registration_form(self, name, email, password, confirm_password):
        self.driver.find_element(*self.NAME_INPUT).send_keys(name)
        self.driver.find_element(*self.EMAIL_INPUT).send_keys(email)
        self.driver.find_element(*self.PASSWORD_INPUT).send_keys(password)
        self.driver.find_element(*self.CONFIRM_PASSWORD_INPUT).send_keys(confirm_password)

    def submit_registration(self):
        self.driver.find_element(*self.REGISTER_BUTTON).click()
        time.sleep(3)
