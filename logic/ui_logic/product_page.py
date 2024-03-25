from selenium.webdriver.common.by import By
from infra.ui_infra.base_page import BasePage
from selenium.webdriver.support.ui import Select
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time


class ProductPage(BasePage):
    QUANTITY_SELECT = (By.XPATH, "//select[@class='form-control']")#there is an error in the xpath. can't click on it
    RATING_SELECT = (By.XPATH, "//select[@id='rating']")
    COMMENT_TEXTAREA = (By.XPATH, "//textarea[@id='comment']")
    # SUBMIT_REVIEW_BUTTON = (By.XPATH, "//button[@type='submit']")
    # GO_BACK_LINK = (By.XPATH, "//a[contains(text(),'Go Back')]")
    SUBMIT_REVIEW_BUTTON = (By.XPATH, "//button[@type='submit' and contains(@class, 'btn-primary')]")
    # GO_BACK_LINK = (By.XPATH, "//a[@href='#/' and contains(@class, 'btn-light')]")
    GO_BACK_LINK = (By.XPATH, "//a[contains(@class, 'btn-light') and contains(text(), 'Go Back')]")

    def update_quantity(self, quantity):
        quantity_select_element = self.driver.find_element(*self.QUANTITY_SELECT)
        select = Select(quantity_select_element)
        select.select_by_value(str(quantity))
        time.sleep(3)

    def select_review_rate(self, value):
        rating_select = WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable(self.RATING_SELECT))
        self.driver.execute_script("arguments[0].scrollIntoView(true);", rating_select)
        try:
            rating_select.click()
        except Exception as e:
            print(f"Click using traditional method failed: {e}. Attempting click via JavaScript.")
            self.driver.execute_script("arguments[0].click();", rating_select)

        # Select the rating option
        rating_option = f"//select[@id='rating']/option[@value='{value}']"
        WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable((By.XPATH, rating_option))).click()
        print("Rating selected.")
        time.sleep(4)

    def add_review_comment(self, comment):
        comment_textarea = self.driver.find_element(*self.COMMENT_TEXTAREA)
        comment_textarea.send_keys(comment)
        time.sleep(3)

    def submit_review(self):
        submit_button = WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable(self.SUBMIT_REVIEW_BUTTON))
        self.driver.execute_script("arguments[0].scrollIntoView(true);", submit_button)
        submit_button.click()
        time.sleep(3)

    def go_back(self):
        WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located(self.GO_BACK_LINK))
        go_back_link = self.driver.find_element(*self.GO_BACK_LINK)
        self.driver.execute_script("arguments[0].scrollIntoView(true);", go_back_link)
        self.driver.execute_script("arguments[0].click();", go_back_link)
        time.sleep(3)

