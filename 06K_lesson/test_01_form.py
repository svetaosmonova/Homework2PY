import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By


@pytest.fixture(scope="module")
def driver():

    driver = webdriver.Chrome()
    yield driver
    driver.quit()


def test_shopping_cart(driver):

    driver.get(
        "https://bonigarcia.dev/selenium-webdriver-java/data-types.html")

    driver.execute_script(
        "window.scrollTo(0, document.body.scrollHeight);")

    first_name_field = driver.find_element(
        By.NAME, 'first-name')
    last_name_field = driver.find_element(
        By.NAME, 'last-name')
    address_field = driver.find_element(
        By.NAME, 'address')
    email_field = driver.find_element(
        By.NAME, 'e-mail')
    phone_number_field = driver.find_element(
        By.NAME, 'phone')
    city_field = driver.find_element(
        By.NAME, 'city')
    country_field = driver.find_element(
        By.NAME, 'country')
    job_position_field = driver.find_element(
        By.NAME, 'job-position')
    company_field = driver.find_element(
        By.NAME, 'company')

    first_name_field.send_keys('Иван')
    last_name_field.send_keys('Петров')
    address_field.send_keys('Ленина, 55-3')
    email_field.send_keys('test@skypro.com')
    phone_number_field.send_keys('+7985899998787')
    city_field.send_keys('Москва')
    country_field.send_keys('Россия')
    job_position_field.send_keys('QA')
    company_field.send_keys('SkyPro')

    submit_button = driver.find_element(
        By.XPATH, '//button[contains(text(), "Submit")]'
    )
    submit_button.click()

    assert "danger" in driver.find_element(
        By.ID, "zip-code").get_attribute("class")
    assert "success" in driver.find_element(
        By.ID, "first-name").get_attribute("class")
    assert "success" in driver.find_element(
        By.ID, "last-name").get_attribute("class")
    assert "success" in driver.find_element(
        By.ID, "address").get_attribute("class")
    assert "success" in driver.find_element(
        By.ID, "e-mail").get_attribute("class")
    assert "success" in driver.find_element(
        By.ID, "phone").get_attribute("class")
    assert "success" in driver.find_element(
        By.ID, "city").get_attribute("class")
    assert "success" in driver.find_element(
        By.ID, "country").get_attribute("class")
    assert "success" in driver.find_element(
        By.ID, "job-position").get_attribute("class")
    assert "success" in driver.find_element(
        By.ID, "company").get_attribute("class")
