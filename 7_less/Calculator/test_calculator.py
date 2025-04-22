import pytest
from selenium import webdriver
from Calc_class_test import Calculator


@pytest.fixture(scope="module")
def driver():

    driver = webdriver.Chrome()
    driver.implicitly_wait(3)
    driver.maximize_window()
    yield driver
    driver.quit()


def test_shopping_cart(driver):
    calculator = Calculator(driver)
    calculator.set_delay(1)
    calculator.click_button('7')
    calculator.click_button('+')
    calculator.click_button('8')
    calculator.click_button('=')

    calculator.wait_until_result_is("15")
    assert calculator.get_result_text() == "15"
