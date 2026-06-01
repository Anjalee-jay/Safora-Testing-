from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager
import time


driver = webdriver.Chrome(service=Service(ChromeDriverManager(version="148").install()))

try:
   
    driver.get("https://safora.se/en/contact.html")
    driver.maximize_window()
    time.sleep(3)

    
    name = driver.find_element(By.XPATH, "//input[@placeholder='Your Name']")
    name.send_keys("Anjalee Jay")
    print("✓ Name field filled")

    
    email = driver.find_element(By.XPATH, "//input[@placeholder='Email Address']")
    email.send_keys("anjaleejay@gmail.com")
    print("Email field filled")

 
    phone = driver.find_element(By.XPATH, "//input[@placeholder='Phone Number']")
    phone.send_keys("+94718888886")
    print("Phone field filled")

    message = driver.find_element(By.XPATH, "//textarea[@placeholder='Your Message']")
    message.send_keys("This is a test message from automation script.")
    print("Message field filled")

    time.sleep(2)


    print("\n Form populated successfully, but submission blocked by reCAPTCHA.")
    print("Test passed: All required form fields successfully located and filled.")

finally:
    # Close browser
    time.sleep(2)
    driver.quit()
