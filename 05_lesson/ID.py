from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


def click_blue_button():

    driver = webdriver.Chrome()
    driver.get("http://uitestingplayground.com/dynamicid")


    try:

        WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.ID, "button0"))
        )


        blue_button = driver.find_element(By.ID, "button0")
        blue_button.click()

        print("Синяя кнопка найдена и нажата!")
    except Exception as e:
        print(f"Произошла ошибка: {str(e)}")
    finally:

        driver.quit()


if __name__ == "__main__":
    click_blue_button()
