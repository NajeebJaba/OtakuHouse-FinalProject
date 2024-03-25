from selenium.webdriver.common.by import By
from infra.ui_infra.base_page import BasePage


class LoginPage(BasePage):
    EMAIL = (By.ID, 'email')#(By.XPATH, "//input[@id='email']")
    PASSWORD = (By.ID, 'password')#(By.XPATH, "//input[@id='password']")
    SIGNIN_BUTTON = (By.CLASS_NAME, 'btn-primary')#(By.XPATH, "//button[@type='submit' and contains(@class, 'btn-primary')]")
    REGISTER_BUTTON = (By.XPATH, "//a[@href='#/register?redirect=/']")

    EMAIL_TWO = (By.ID, 'email')
    PASSWORD_TWO = (By.ID, 'password')

    def enter_username(self, username):
        email_field = self.driver.find_element(*self.EMAIL)
        email_field.send_keys(username)

    def enter_password_and_login(self, password):
        password_field = self.driver.find_element(*self.PASSWORD)
        password_field.send_keys(password)
        signin_button = self.driver.find_element(*self.SIGNIN_BUTTON)
        signin_button.click()

    def click_register(self):
        register_button = self.driver.find_element(*self.REGISTER_BUTTON)
        register_button.click()




