from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

# Set up the WebDriver (example with Chrome)
driver = webdriver.Chrome()

# Open the webpage
driver.get("https://openinapp.com/")

# Implicit wait
driver.implicitly_wait(10)

try:
    # Print the HTML source of the page
    html = driver.page_source
    print(html)
    
    # Wait for the element to be present
    element = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.NAME, "url_input"))
    )
    # Now you can interact with the element
    element.send_keys("your text")
except Exception as e:
    print(f"Test Failed: {e}")
    driver.save_screenshot('screenshot.png')
finally:
    # Clean up
    driver.quit()
