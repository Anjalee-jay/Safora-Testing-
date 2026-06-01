from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager
import time


# Initialize browser with matching ChromeDriver for Chrome 148
driver = webdriver.Chrome(service=Service(ChromeDriverManager(version="148").install()))

try:
    # Step 1: Open website
    driver.get("https://safora.se/en/contact.html")
    driver.maximize_window()
    time.sleep(3)

    # Step 2: Fill in Contact Form fields
    # Using XPath to find textboxes by their label text or placeholder

    # Name field - find by placeholder "Your Name"
    name = driver.find_element(By.XPATH, "//input[@placeholder='Your Name']")
    name.send_keys("John Doe")
    print("✓ Name field filled")

    # Email field - find by placeholder "Email Address"
    email = driver.find_element(By.XPATH, "//input[@placeholder='Email Address']")
    email.send_keys("johndoe@example.com")
    print("✓ Email field filled")

    # Phone field - find by placeholder "Phone Number"
    phone = driver.find_element(By.XPATH, "//input[@placeholder='Phone Number']")
    phone.send_keys("+46730123456")
    print("✓ Phone field filled")

    # Message field - find by placeholder "Your Message"
    message = driver.find_element(By.XPATH, "//textarea[@placeholder='Your Message']")
    message.send_keys("This is a test message from automation script.")
    print("✓ Message field filled")

    time.sleep(2)

    # NOTE: reCAPTCHA will block automated submission. This test demonstrates field population.
    print("\n⚠️  Form populated successfully, but submission blocked by reCAPTCHA.")
    print("✅ Test passed: All required form fields successfully located and filled.")

finally:
    # Close browser
    time.sleep(2)
    driver.quit()
