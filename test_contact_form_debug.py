from selenium import webdriver
from selenium.webdriver.common.by import By
import time

print("[DEBUG] Starting Selenium contact form test...")

try:
    print("[DEBUG] Initializing Chrome WebDriver...")
    driver = webdriver.Chrome()
    print("[DEBUG] WebDriver initialized successfully")
    
    print("[DEBUG] Opening https://safora.se/en/contact.html...")
    driver.get("https://safora.se/en/contact.html")
    driver.maximize_window()
    print("[DEBUG] Waiting 3 seconds for page to load...")
    time.sleep(3)
    print("[DEBUG] Page loaded")

    print("[DEBUG] Finding name field...")
    name = driver.find_element(By.XPATH, "//input[@placeholder='Your Name']")
    print("[DEBUG] Name field found, filling with 'Anjalee Jay'...")
    name.send_keys("Anjalee Jay")
    print("Name field filled")

    print("[DEBUG] Finding email field...")
    email = driver.find_element(By.XPATH, "//input[@placeholder='Email Address']")
    print("[DEBUG] Email field found, filling with 'anjaleejay@gmail.com'...")
    email.send_keys("anjaleejay@gmail.com")
    print("Email field filled")

    print("[DEBUG] Finding phone field...")
    phone = driver.find_element(By.XPATH, "//input[@placeholder='Phone Number']")
    print("[DEBUG] Phone field found, filling with '+94718888886'...")
    phone.send_keys("+94718888886")
    print("Phone field filled")

    print("[DEBUG] Finding message field...")
    message = driver.find_element(By.XPATH, "//textarea[@placeholder='Your Message']")
    print("[DEBUG] Message field found, filling with test message...")
    message.send_keys("This is a test message from automation script.")
    print("Message field filled")

    time.sleep(2)

    print("\nSUCCESS: All form fields filled successfully!")
    print("⚠️  reCAPTCHA prevents automated submission, but form population test PASSED")

except Exception as e:
    print(f"\n ERROR: {str(e)}")
    import traceback
    traceback.print_exc()

finally:
    print("[DEBUG] Waiting 2 seconds before closing browser...")
    time.sleep(2)
    print("[DEBUG] Closing WebDriver...")
    driver.quit()
    print("[DEBUG] Test completed")
