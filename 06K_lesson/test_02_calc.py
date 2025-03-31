import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


@pytest.fixture(scope="module")
def driver():

    driver = webdriver.Chrome()
    yield driver
    driver.quit()


def test_shopping_cart(driver):

    driver.get(
        "https://bonigarcia.dev/selenium-webdriver-java/slow-calculator.html")

    delay_input = driver.find_element(
        By.CSS_SELECTOR, "#delay")
    delay_input.clear()
    delay_input.send_keys("45")

    driver.find_element(
        By.XPATH, '//span[text()="7"]').click()
    driver.find_element(
        By.XPATH, '//span[text()="+"]').click()
    driver.find_element(
        By.XPATH, '//span[text()="8"]').click()
    driver.find_element(
        By.XPATH, '//span[text()="="]').click()

    WebDriverWait(driver, 46).until(
        EC.text_to_be_present_in_element((
            By.CLASS_NAME, "screen"), "15"))

    result_text = driver.find_element(
        By.CLASS_NAME, "screen").text

    assert result_text == "15"

    driver.quit()
