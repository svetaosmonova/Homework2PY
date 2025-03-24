from selenium import webdriver
from selenium.webdriver.common.by import By


driver = webdriver.Chrome()
driver.get('http://uitestingplayground.com/textinput')


input_field = driver.find_element(By.ID, 'newButtonName')
input_field.send_keys('SkyPro')


button = driver.find_element(By.CSS_SELECTOR, '.btn.btn-primary')
button.click()


updated_button_text = button.text
print(updated_button_text)