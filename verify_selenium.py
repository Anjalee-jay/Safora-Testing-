#!/usr/bin/env python
"""Minimal Selenium test to verify installation."""

print("=" * 60)
print("SAFORA SELENIUM VERIFICATION TEST")
print("=" * 60)

print("\n[1/5] Checking Python version...")
import sys
print(f"  Python: {sys.version}")

print("\n[2/5] Testing Selenium import...")
try:
    from selenium import webdriver
    print("  ✓ Selenium imported successfully")
except ImportError as e:
    print(f"  ✗ Failed to import Selenium: {e}")
    sys.exit(1)

print("\n[3/5] Testing WebDriver Manager...")
try:
    from webdriver_manager.chrome import ChromeDriverManager
    print("  ✓ WebDriver Manager imported successfully")
except ImportError as e:
    print(f"  ✗ Failed to import WebDriver Manager: {e}")
    sys.exit(1)

print("\n[4/5] Preparing ChromeDriver...")
try:
    from selenium.webdriver.chrome.service import Service
    driver_path = ChromeDriverManager().install()
    print(f"  ✓ ChromeDriver prepared at: {driver_path}")
except Exception as e:
    print(f"  ✗ Failed to prepare ChromeDriver: {e}")
    sys.exit(1)

print("\n[5/5] Testing WebDriver initialization...")
try:
    options = webdriver.ChromeOptions()
    options.add_argument("--headless=new")
    options.add_argument("--disable-gpu")
    options.add_argument("--no-sandbox")
    
    service = Service(driver_path)
    driver = webdriver.Chrome(service=service, options=options)
    print("  ✓ WebDriver initialized successfully")
    
    print("\n  Testing URL navigation...")
    driver.get("https://httpbin.org/status/200")
    print(f"  ✓ URL accessed successfully")
    print(f"  ✓ Current URL: {driver.current_url}")
    print(f"  ✓ Page title: {driver.title}")
    
    driver.quit()
    print("  ✓ WebDriver closed successfully")
    
except Exception as e:
    print(f"  ✗ WebDriver error: {e}")
    sys.exit(1)

print("\n" + "=" * 60)
print("✓ ALL TESTS PASSED - SELENIUM IS WORKING!")
print("=" * 60)
print("\nYou can now run:")
print("  - python test_safora.py")
print("  - python test_contact_form.py")
print("  - python run_all_tests.py")
