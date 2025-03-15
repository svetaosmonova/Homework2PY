from selenium import webdriver
from selenium.webdriver.common.by import By
import time



url = "http://the-internet.herokuapp.com/add_remove_elements/"
browser = webdriver.Chrome()
browser.get(url)


add_button = browser.find_element(By.XPATH, "//button[text()='Add Element']")
for _ in range(5):
    add_button.click()
    time.sleep(1)


delete_buttons = browser.find_elements(By.XPATH, "//button[text()='Delete']")


print(f"Количество кнопок Delete: {len(delete_buttons)}")


browser.quit()