from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from webdriver_manager.chrome import ChromeDriverManager


def test_safora_homepage():
    """Open the Safora website and verify the English homepage loads."""
    url = "https://safora.se/en/"

    service = Service(ChromeDriverManager().install())
    options = webdriver.ChromeOptions()
    options.add_argument("--headless=new")
    options.add_argument("--disable-gpu")
    options.add_argument("--no-sandbox")

    driver = webdriver.Chrome(service=service, options=options)
    driver.set_window_size(1920, 1080)

    try:
        driver.get(url)
        wait = WebDriverWait(driver, 15)

        # Confirm the page title contains Safora or the page's English path
        wait.until(EC.title_contains("Safora"))
        print("Title:", driver.title)

        # Confirm the English homepage content is present
        element = wait.until(
            EC.presence_of_element_located(
                (By.CSS_SELECTOR, "body")
            )
        )

        if "en" not in driver.current_url:
            raise AssertionError(f"Unexpected URL loaded: {driver.current_url}")

        print("Safora EN homepage loaded successfully.")
        print("Page length:", len(driver.page_source))

    finally:
        driver.quit()


if __name__ == "__main__":
    test_safora_homepage()
