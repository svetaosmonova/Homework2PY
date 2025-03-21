from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time


driver = webdriver.FireFox()
driver.get("http://the-internet.herokuapp.com/inputs")


input_field = WebDriverWait(driver, 10).until(EC.visibility_of_element_located((By.TAG_NAME, "input")))


input_field.send_keys("1000")
time.sleep(5)

input_field.clear()


input_field.send_keys("999")


time.sleep(5)

print("Кнопка clear найдена и очищена!")
driver.quit()