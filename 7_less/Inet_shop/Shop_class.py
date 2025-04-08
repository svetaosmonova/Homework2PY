import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


@pytest.fixture(scope="module")
def driver():

    driver = webdriver.Chrome()
    driver.implicitly_wait(3)
    driver.maximize_window()
    yield driver
    driver.quit()

class LoginPage:
    def __init__(self, driver):
        self.driver = driver
        self.driver.get("https://www.saucedemo.com/")
        self.wait = WebDriverWait(driver, 5)

        self.username_input = (By.ID, "user-name")  # Локатор для поля ввода имени пользователя
        self.password_input = (By.ID, "password")   # Локатор для поля ввода пароля
        self.login_button = (By.CLASS_NAME, "btn_action")  # Локатор для кнопки входа

    def enter_username(self, username):
        WebDriverWait(self.driver, 10).until(EC.presence_of_element_located(self.username_input)).send_keys(username)

    def enter_password(self, password):
        WebDriverWait(self.driver, 10).until(EC.presence_of_element_located(self.password_input)).send_keys(password)

    def click_login_button(self):
        WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable(self.login_button)).click()

class MainPage:
    # Инициализирует элементы на странице
    def __init__(self, driver):
        self.driver = driver
        self.driver.get("https://www.saucedemo.com/")
        self.wait = WebDriverWait(driver, 5)

        self.add_to_cart_buttons = {
            "backpack": (By.XPATH,
                         "//div[contains(text(), 'Sauce Labs Backpack')]//ancestor::div[@class='inventory_item']//descendant::button"),
            "t-shirt": (By.XPATH,
                        "//div[contains(text(), 'Sauce Labs Bolt T-Shirt')]//ancestor::div[@class='inventory_item']//descendant::button"),
            "onesie": (By.XPATH,
                       "//div[contains(text(), 'Sauce Labs Onesie')]//ancestor::div[@class='inventory_item']//descendant::button")
        }
        self.cart_icon = (By.CLASS_NAME, "shopping_cart_link")

    # Добавляет товар в корзину
    def add_item_to_cart(self, item_name):
        locator = self.add_to_cart_buttons[item_name]
        WebDriverWait(self.driver, 20).until(EC.element_to_be_clickable(locator)).click()

    # Переходит в корзину
    def go_to_cart(self):
        WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable(self.cart_icon)).click()
class CartPage:
    def __init__(self, driver):
        self.driver = driver
        self.driver.get("https://www.saucedemo.com/")
        self.wait = WebDriverWait(driver, 5)

        self.checkout_button = (By.CLASS_NAME, "checkout_button")


    def click_checkout_button(self):
        self.wait.until(EC.element_to_be_clickable(self.checkout_button)).click()




class CheckoutPage:
    def __init__(self, driver):
        self.driver = driver
        self.driver.get("https://www.saucedemo.com/")
        self.wait = WebDriverWait(driver, 5)

        self.fields = {
            'first-name': "first-name",
            'last-name': "last-name",
            'postal_code': "postal-code",
             'continue_button': "#continue",
            'total_cost_label': "summary_total_label"
        }

    def open(self):
        self.driver.get(
            "https://bonigarcia.dev/selenium-webdriver-java/data-types.html"
        )

    def fill_form(self):
        for field, value in self.fields.items():
            self.wait.until(
                EC.presence_of_element_located((
                    By.NAME, field))).send_keys(value)

    def submit_form(self):
        self.wait.until(
            EC.element_to_be_clickable((
                By.CSS_SELECTOR, '[type="submit"]'))).click()

    def get_field_class(self, field_id):
        element = self.wait.until(
            EC.presence_of_element_located((
                By.ID, field_id))).get_attribute("class")
        return element

    def get_total_cost(self):
        total_cost_element = WebDriverWait(self.driver, 10).until(EC.presence_of_element_located(self.total_cost_label))
        return total_cost_element.text.split(":")[1].strip()