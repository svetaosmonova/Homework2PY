from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


driver = webdriver.Chrome()
driver.get(
    "https://bonigarcia.dev/selenium-webdriver-java/loading-images.html")

wait = WebDriverWait(driver, 10)


images = wait.until(
    EC.visibility_of_all_elements_located((
        By.TAG_NAME, 'img'
    ))
)


if len(images) >= 4:
    print("Все изображения загружены.")
else:
    print("Не все изображения загружены.")


try:
    wait.until(
        EC.visibility_of_element_located((
            By.ID, "doneMessage"))
    )
    print("Надпись 'Done!' появилась.")
except Exception as e:
    print(f"Надпись 'Done!' не появилась: {e}")


src_value = images[-1].get_attribute("src")
print(f"Ссылка на последнее изображение: {src_value}")

driver.quit()
