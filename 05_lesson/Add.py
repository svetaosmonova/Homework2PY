from selenium import webdriver
from selenium.webdriver.common.by import By
import time


# Шаг 1: Открываем страницу
url = "http://the-internet.herokuapp.com/add_remove_elements/"
browser = webdriver.Chrome()  # Замените Chrome на нужный драйвер браузера
browser.get(url)

# Шаг 2: Пять раз кликаем на кнопку Add Element
add_button = browser.find_element(By.XPATH, "//button[text()='Add Element']")
for _ in range(5):
    add_button.click()
    time.sleep(1)  # Небольшая пауза между кликами

# Шаг 3: Собираем кнопки Delete
delete_buttons = browser.find_elements(By.XPATH, "//button[text()='Delete']")

# Шаг 4: Выводим размер списка кнопок Delete
print(f"Количество кнопок Delete: {len(delete_buttons)}")

# Закрытие браузера
browser.quit()