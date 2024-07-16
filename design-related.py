from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

driver = webdriver.Chrome()

driver.get("https://openinapp.com/")


# 1. Check for Broken Links
def check_broken_links():
    links = driver.find_elements(By.TAG_NAME, 'a')
    for link in links:
        url = link.get_attribute('href')
        if url is not None:
            driver.get(url)
            if driver.title == "404 Not Found":
                print(f"Broken link found: {url}")

# 2. Check for Missing Alt Text in Images
def check_missing_alt_text():
    images = driver.find_elements(By.TAG_NAME, 'img')
    for img in images:
        alt_text = img.get_attribute('alt')
        if not alt_text:
            print("Missing alt text in image:", img.get_attribute('src'))

# 3. Check for Text Overlapping
def check_text_overlapping():
    elements = driver.find_elements(By.XPATH, "//*[contains(text(), '')]")
    for element in elements:
        try:
            if element.size['height'] < 20:  # Example condition for overlapping text
                print(f"Possible text overlap in element: {element.text}")
        except Exception as e:
            print(e)

# Call the functions
check_broken_links()
check_missing_alt_text()
check_text_overlapping()

# Close the WebDriver
driver.quit()
