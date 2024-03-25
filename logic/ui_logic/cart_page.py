from selenium.webdriver.common.by import By
from infra.ui_infra.base_page import BasePage
import time
from selenium.webdriver.support.ui import Select
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class CartPage(BasePage):
    # PRODUCT_IMAGE_XPATH = "//img[@class='card-img' and @src='/media/images/ichigo_shirt.jpg']"
    ADD_TO_CART_BUTTON = (By.XPATH, "//button[@type='button' and contains(@class, 'btn-primary') and text()='Add to Cart']")
    # ADD_TO_CART_BUTTON = (By.XPATH, "//button[text()='Add to Cart']")
    QUANTITY_SELECT = (By.XPATH, "//select[@class='form-control']")
    DELETE_ICON = (By.XPATH, "//i[@class='fas fa-trash']")

    def add_to_cart(self):
        WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable(self.ADD_TO_CART_BUTTON)).click()
        time.sleep(2)

    def update_quantity(self, quantity):
        select_element = self.driver.find_element(*self.QUANTITY_SELECT)
        select = Select(select_element)
        select.select_by_value(str(quantity))
        time.sleep(3)

    def delete_product(self):
        self.driver.find_element(*self.DELETE_ICON).click()
        time.sleep(3)
