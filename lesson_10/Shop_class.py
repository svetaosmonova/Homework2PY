from selenium.webdriver.common.by import By
from time import sleep


class ShopPage:
    """
    Класс для взаимодействия с страницей интернет-магазина Sauce Demo.

    Атрибуты:
    driver (webdriver): Веб-драйвер Selenium.
        url (str): Адрес начальной страницы магазина.
        Локаторы элементов страницы:
            username (tuple): Поле ввода имени пользователя.
            password (tuple): Поле ввода пароля.
            login_button (tuple): Кнопка входа.
            backpack (tuple): Кнопка добавления рюкзака в корзину.
            tshirt (tuple): Кнопка добавления футболки в корзину.
            onesie (tuple): Кнопка добавления костюма в корзину.
            cart_button (tuple): Кнопка просмотра корзины.
            checkout_button (tuple): Кнопка начала оформления заказа.
            first_name (tuple): Поле ввода имени заказчика.
            last_name (tuple): Поле ввода фамилии заказчика.
            postal_code (tuple): Поле ввода почтового индекса.
            continue_button (tuple): Кнопка подтверждения ввода данных.
            total (tuple): Элемент отображающий итоговую сумму заказа.
    """
    def __init__(self, driver):
        """
        Инициализатор класса ShopPage.

        :param driver: Объект веб-драйвера Selenium.
        """
        self.driver = driver
        self.url = "https://www.saucedemo.com/"

     # Определение локаторов элементов страницы
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
        """
        Открывает страницу интернет-магазина.

        :return: None
        """
        self.driver.get(self.url)

    def login(self, username, password):
        """
        Производит авторизацию на сайте.

        :param username: str — имя пользователя.
        :param password: str  — пароль пользователя.
        :return: None
        """
        user_field = self.driver.find_element(*self.username)
        pass_field = self.driver.find_element(*self.password)
        login_btn = self.driver.find_element(*self.login_button)

        user_field.send_keys(username)
        pass_field.send_keys(password)
        login_btn.click()

    def add_to_cart(self):
        """
        Добавляет три товара в корзину.

        :return: None
        """
        # Добавляем рюкзак, футболку и костюм в корзину
        self.driver.find_element(*self.backpack).click()
        self.driver.find_element(*self.tshirt).click()
        self.driver.find_element(*self.onesie).click()

    def checkout(self, first_name, last_name, postal_code):
        """
        Начинает оформление заказа и вводит личные данные.

        :param first_name: str — имя покупателя.
        :param last_name: str — фамилия покупателя.
        :param postal_code: str — почтовый индекс.
        :return: None
        """
        # Пройдем в корзину и начнем оформление заказа
        self.driver.find_element(*self.cart_button).click()
        sleep(5)
        self.driver.find_element(*self.checkout_button).click()

        # Вводим персональные данные
        first_name_field = self.driver.find_element(*self.first_name)
        last_name_field = self.driver.find_element(*self.last_name)
        postal_code_field = self.driver.find_element(*self.postal_code)
        cont_btn = self.driver.find_element(*self.continue_button)

        first_name_field.send_keys(first_name)
        last_name_field.send_keys(last_name)
        postal_code_field.send_keys(postal_code)
        cont_btn.click()

    def get_total(self):
        """
        Возвращает итоговую сумму заказа.

        :return: str — текст итоговой суммы заказа.
        """
        total_element = self.driver.find_element(*self.total)
        return total_element.text