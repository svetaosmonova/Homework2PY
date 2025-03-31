from selenium import webdriver
from selenium.webdriver.common.by import By

def click_blue_button():
    driver = webdriver.Chrome()
    driver.get("http://uitestingplayground.com/classattr")


    blue_button = driver.find_element(By.CLASS_NAME, "btn-primary")
    blue_button.click()

    print("Синяя кнопка найдена и нажата!")
    driver.quit()


click_blue_button()