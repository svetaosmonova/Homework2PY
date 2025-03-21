from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


driver = webdriver.FireFox()
driver.get("http://the-internet.herokuapp.com/entry_ad")

try:

    wait = WebDriverWait(driver, 10)
    modal_window = wait.until(EC.visibility_of_element_located((By.ID, "modal")))


    close_button = modal_window.find_element(By.XPATH, "//p[contains(text(), 'Close')]")
    close_button.click()

finally:
    print("Кнопка close найдена и нажата!")
    driver.quit()
