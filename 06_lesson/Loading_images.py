from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


driver = webdriver.Chrome()
driver.get("https://bonigarcia.dev/selenium-webdriver-java/loading-images.html")

wait = WebDriverWait(driver, 10)
images = wait.until(
    EC.visibility_of_all_elements_located((By.TAG_NAME, 'img'))
)

wait = WebDriverWait(driver, 30)
order = wait.until(EC.presence_of_element_located((By.ID, "award")))


src_value = order.get_attribute("src")


print(src_value)

р
driver.quit()