from selenium import webdriver
from selenium.webdriver.common.by import By

# Шаг 1: Открываем страницу
driver = webdriver.Chrome()
driver.get("http://the-internet.herokuapp.com/add_remove_elements/")

# Шаг 2: Пять раз кликаем на кнопку Add Element
add_button = driver.find_element(By.CSS_SELECTOR, "#content > div > button")
for _ in range(5):
    add_button.click()

# Шаг 3: Собираем список кнопок Delete
delete_buttons = driver.find_elements(By.XPATH, "//button[text()='Delete']")

# Шаг 4: Выводим на экран размер списка
print(f"Количество кнопок 'Delete': {len(delete_buttons)}")

# Закрытие браузера (необязательно)
driver.quit()