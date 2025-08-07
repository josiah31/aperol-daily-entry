from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
import time

def run():
    options = Options()
    options.add_argument('--headless')
    options.add_argument('--no-sandbox')
    options.add_argument('--disable-dev-shm-usage')

    driver = webdriver.Chrome(options=options)

    try:
        driver.get("https://promotions.aperol.com/venice/")
        time.sleep(3)  # Let the page load

        # Fill out form fields
        driver.find_element(By.NAME, "firstName").send_keys("Josiah")
        driver.find_element(By.NAME, "lastName").send_keys("Leeke")
        driver.find_element(By.NAME, "email").send_keys("josiahleeke97@gmail.com")
        driver.find_element(By.NAME, "phone").send_keys("0422258329")
        driver.find_element(By.NAME, "postcode").send_keys("4565")

        # Accept Terms & Conditions checkbox
        checkbox = driver.find_element(By.NAME, "terms")
        if not checkbox.is_selected():
            checkbox.click()

        time.sleep(1)
        # Click the submit button
        driver.find_element(By.XPATH, "//button[@type='submit']").click()

        print("Form submitted successfully.")

    except Exception as e:
        print("Error:", e)

    finally:
        driver.quit()

if __name__ == "__main__":
    run()
