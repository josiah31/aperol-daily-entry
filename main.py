from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
from datetime import datetime, date
import time

# Auto-stop after November 30, 2025
end_date = date(2025, 11, 30)
if date.today() > end_date:
    print("Automation period ended. No submission today.")
    exit()

def submit_form(contact):
    print(f"Submitting for {contact['email']}...")

    options = Options()
    options.add_argument('--headless')
    options.add_argument('--no-sandbox')
    options.add_argument('--disable-dev-shm-usage')

    driver = webdriver.Chrome(options=options)
    driver.get("https://promotions.aperol.com/venice/")

    time.sleep(3)  # wait for page to load

    driver.find_element(By.NAME, "firstName").send_keys(contact["first_name"])
    driver.find_element(By.NAME, "lastName").send_keys(contact["last_name"])
    driver.find_element(By.NAME, "email").send_keys(contact["email"])
    driver.find_element(By.NAME, "phone").send_keys(contact["phone"])
    driver.find_element(By.NAME, "zipCode").send_keys(contact["postcode"])

    driver.find_element(By.NAME, "terms").click()

    time.sleep(1)
    driver.find_element(By.CSS_SELECTOR, "button[type='submit']").click()

    time.sleep(2)  # wait after submission

    driver.quit()

def log_submission(contact):
    timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    with open("submission_log.txt", "a") as log:
        log.write(f"{timestamp} - Submitted for {contact['email']}, {contact['phone']}, {contact['postcode']}\n")

contact_list = [
    {
        "first_name": "Josiah",
        "last_name": "Leeke",
        "email": "josiahleeke97@gmail.com",
        "phone": "422258329",
        "postcode": "4565"
    },
    {
        "first_name": "Morgan",
        "last_name": "Leeke",
        "email": "leekejosiah@gmail.com",
        "phone": "0466965467",
        "postcode": "4565"
    }
]

for contact in contact_list:
    try:
        submit_form(contact)
        log_submission(contact)
        print(f"Success for {contact['email']}")
    except Exception as e:
        print(f"Failed for {contact['email']}: {e}")
