from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class ShopPage:
    def __init__(self, driver):
        self.driver = driver
        self.url = "https://www.saucedemo.com/"

        self.username = (By.ID, "user-name")
        self.password = (By.ID, "password")
        self.login_button = (By.CSS_SELECTOR, ".btn_action")
        self.backpack = (By.ID, "add-to-cart-sauce-labs-backpack")
        self.tshirt = (By.ID, "add-to-cart-sauce-labs-bolt-t-shirt")
        self.onesie = (By.ID, "add-to-cart-sauce-labs-onesie")
        self.cart_button = (By.CSS_SELECTOR, ".shopping_cart_link")
        self.checkout_button = (By.CSS_SELECTOR, "#checkout")
        self.first_name = (By.ID, "first-name")
        self.last_name = (By.ID, "last-name")
        self.postal_code = (By.ID, "postal-code")
        self.continue_button = (By.CSS_SELECTOR, ".btn_primary.cart_button")
        self.total = (By.CSS_SELECTOR, ".summary_total_label")

    def open(self):
        self.driver.get(self.url)

    def login(self, username, password):
        self.driver.find_element(*self.username).send_keys(username)
        self.driver.find_element(*self.password).send_keys(password)
        self.driver.find_element(*self.login_button).click()

    def add_to_cart(self):
        self.driver.find_element(*self.backpack).click()
        self.driver.find_element(*self.tshirt).click()
        self.driver.find_element(*self.onesie).click()

    def checkout(self, first_name, last_name, postal_code):
        self.driver.find_element(*self.cart_button).click()
        self.driver.find_element(*self.checkout_button).click()
        self.driver.find_element(*self.first_name).send_keys(first_name)
        self.driver.find_element(*self.last_name).send_keys(last_name)
        self.driver.find_element(*self.postal_code).send_keys(postal_code)
        self.driver.find_element(*self.continue_button).click()

    def get_total(self):
        return self.driver.find_element(*self.total).text
