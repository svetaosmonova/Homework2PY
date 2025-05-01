import pytest
from selenium import webdriver
from Shop_class import ShopPage
import allure


@pytest.fixture
def chrome_browser():
    driver = webdriver.Chrome()
    yield driver
    driver.quit()


@allure.title("Процесс покупки товаров на сайте магазина")
@allure.description("Этот тест проверяет полный цикл покупки товаров на сайте магазина.")
@allure.feature("Покупка товаров")
@allure.severity(allure.severity_level.NORMAL)
def test_shopping(chrome_browser):
    shopping_page = ShopPage(chrome_browser)

    with allure.step("Открываем домашнюю страницу магазина"):
        shopping_page.open()

    with allure.step("Авторизируемся на сайте"):
        shopping_page.login("standard_user", "secret_sauce")

    with allure.step("Добавляем товары в корзину"):
        shopping_page.add_to_cart()

    with allure.step("Оформляем заказ с указанием личных данных"):
        shopping_page.checkout("Имя", "Фамилия", "12345")

    with allure.step("Получаем итоговую сумму заказа"):
        total = shopping_page.get_total()

    with allure.step("Проверяем общую стоимость"):
        assert total == "Total: $58.29", "Общая сумма отличается от ожидаемой."