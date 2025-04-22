import pytest
from selenium import webdriver
from Shop_class import ShopPage


@pytest.fixture
def chrome_browser():
    driver = webdriver.Chrome()
    yield driver
    driver.quit()


def test_shopping(chrome_browser):
    shopping_page = ShopPage(chrome_browser)
    shopping_page.open()
    shopping_page.login("standard_user", "secret_sauce")
    shopping_page.add_to_cart()
    shopping_page.checkout("Имя", "Фамилия", "12345")

    total = shopping_page.get_total()
    assert total == "Total: $58.29"