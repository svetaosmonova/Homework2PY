from Shop_class import LoginPage
from Shop_class import MainPage
from Shop_class import CartPage
from Shop_class import CheckoutPage
import pytest
from selenium import webdriver

@pytest.fixture(scope="module")
def driver():

    driver = webdriver.Chrome()
    driver.implicitly_wait(3)
    driver.maximize_window()
    yield driver
    driver.quit()

def  test_shopping_cart(driver):
    # Инициализация объектов страниц
    login_page = LoginPage(driver)
    main_page = MainPage(driver)
    cart_page = CartPage(driver)
    checkout_page = CheckoutPage(driver)

    # Открытие сайта магазина
    driver.get("https://www.saucedemo.com/")

    # Авторизация
    login_page.enter_username("standard_user")
    login_page.enter_password("secret_sauce")
    login_page.click_login_button()

    # Добавление товаров в корзину
    main_page.add_item_to_cart("backpack")
    main_page.add_item_to_cart("t-shirt")
    main_page.add_item_to_cart("onesie")

    # Переход в корзину
    main_page.go_to_cart()

    # Нажатие кнопки Checkout
    cart_page.click_checkout_button()

    # Заполнение формы данными
    checkout_page.fill_form("Имя", "Фамилия", "123456")

    # Получение итоговой стоимости
    total_cost = checkout_page.get_total_cost()

    # Проверка итоговой суммы
    assert float(total_cost.replace("$", "")) == 58.29, \
        f"Итоговая сумма не совпадает с ожидаемой. Ожидается: $58.29, Получено: {total_cost}"

    # Закрытие браузера
    driver.quit()