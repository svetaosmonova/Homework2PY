from selenium import webdriver
from selenium.webdriver.common.by import By




driver = webdriver.FireFox()
driver.get("http://the-internet.herokuapp.com/login")

try:

    username_input = driver.find_element(By.ID, "username")
    username_input.send_keys("tomsmith")

    password_input = driver.find_element(By.ID, "password")
    password_input.send_keys("SuperSecretPassword!")


    login_button = driver.find_element(By.CSS_SELECTOR, ".radius")
    login_button.click()


finally:
    print("Кнопка  Login найдена и нажата!")
    driver.quit()