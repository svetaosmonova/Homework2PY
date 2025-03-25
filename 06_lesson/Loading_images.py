from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


driver = webdriver.Chrome()
driver.get("https://bonigarcia.dev/selenium-webdriver-java/loading-images.html")

from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

wait = WebDriverWait(driver, 10)  # Ожидание в течение 10 секунд
order = wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, "#award")))



order = driver.find_element(By.ID, "award")

# Получение атрибута "src" у найденного элемента
src_value = order.get_attribute("src")

# Вывод значения атрибута "src" в консоль
print(src_value)

# Закрытие браузера
driver.quit()

