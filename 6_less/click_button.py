from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

driver = webdriver.Chrome()
driver.get('http://uitestingplayground.com/ajax')



WebDriverWait(driver, 10).until(
    EC.element_to_be_clickable((
        By.CSS_SELECTOR, "#ajaxButton"))
).click()


# Исправлен локатор
text_area = WebDriverWait(driver, 20).until(
    EC.visibility_of_element_located((By.CLASS_NAME, 'bg-success'))
)

print(text_area.text)
driver.quit()