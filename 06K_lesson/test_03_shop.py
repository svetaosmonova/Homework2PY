import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time


@pytest.fixture(scope="module")
def driver():

    driver = webdriver.Chrome()
    yield driver
    driver.quit()


def test_shopping_cart(driver):
    # Открытие сайта магазина
    driver.get("https://www.saucedemo.com/")



    # Авторизация
    username_input = driver.find_element(By.ID, "user-name")
    password_input = driver.find_element(By.ID, "password")
    login_button = driver.find_element(By.CLASS_NAME, "btn_action")

    username_input.send_keys("standard_user")
    password_input.send_keys("secret_sauce")
    login_button.click()


    # Добавление товаров в корзину
    backpack_add_button = driver.find_element(By.XPATH,
                                              "//div[contains(text(), 'Sauce Labs Backpack')]/ancestor::div[@class='inventory_item']/descendant::button")
    tshirt_add_button = driver.find_element(By.XPATH,
                                            "//div[contains(text(), 'Sauce Labs Bolt T-Shirt')]/ancestor::div[@class='inventory_item']/descendant::button")
    onesie_add_button = driver.find_element(By.XPATH,
                                            "//div[contains(text(), 'Sauce Labs Onesie')]/ancestor::div[@class='inventory_item']/descendant::button")

    backpack_add_button.click()
    tshirt_add_button.click()
    onesie_add_button.click()

    wait = WebDriverWait(driver, 20)


    # Переход в корзину
    cart_icon = driver.find_element(By.CLASS_NAME, "shopping_cart_link")
    cart_icon.click()

    # Нажатие кнопки Checkout
    checkout_button = driver.find_element(By.CLASS_NAME, "checkout_button")
    checkout_button.click()



    # Заполнение формы данными
    first_name_input = driver.find_element(By.ID, "first-name")
    last_name_input = driver.find_element(By.ID, "last-name")
    postal_code_input = driver.find_element(By.ID, "postal-code")

    first_name_input.send_keys("Имя")
    last_name_input.send_keys("Фамилия")
    postal_code_input.send_keys("123456")

    WebDriverWait(driver, 10).until(
        EC.element_to_be_clickable((
            By.CSS_SELECTOR, "#continue"))
    ).click()




    # Чтение итоговой стоимости
    total_cost = driver.find_element(By.CLASS_NAME, "summary_total_label").text



    assert total_cost == "Total: $58.29", f"Итоговая сумма не совпадает с ожидаемой. Ожидается: $58.29, Получено: ${total_cost}"

    # Закрытие браузера
    driver.quit()
