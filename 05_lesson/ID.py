from selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()
driver.get("http://uitestingplayground.com/dynamicid")

# Используем класс для поиска кнопки
blue_button = driver.find_element(By.CLASS_NAME, "btn-primary")
blue_button.click()

print("Синяя кнопка найдена и нажата!")
driver.quit()