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


class Calculator:

    def __init__(self, driver):
        self.driver = driver
        self.driver.get(
        "https://bonigarcia.dev/selenium-webdriver-java/slow-calculator.html")

    def set_delay(self, delay):
        delay_input = self.driver.find_element(By.CSS_SELECTOR, "#delay")
        delay_input.clear()
        delay_input.send_keys(delay)

    def click_button(self, button):
        self.driver.find_element(By.XPATH, f"//span[text()='{button}']").click()

    def get_result_text(self):
        screen = self.driver.find_element(By.CLASS_NAME, "screen")
        return screen.text

    def wait_until_result_is(self, expected_result):
        WebDriverWait(self.driver, 20).until(
            EC.text_to_be_present_in_element((By.CLASS_NAME, "screen"), expected_result)
        )
