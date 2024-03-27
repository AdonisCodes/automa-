import json
import time
from selenium import webdriver

# Initialize WebDriver
driver = webdriver.Chrome()

# Read cookies from cookies.txt, and convert into json
with open('cookies.txt', 'r') as file:
    cookies_str = file.read()

# Replace single quotes with double quotes
cookies_str = cookies_str.replace("'", '"').replace("True", "true").replace("False", "false")

# Ensure proper formatting
# cookies_str = cookies_str.replace(", {", "}, {")

print(cookies_str)

# Load the JSON
cookies = json.loads(cookies_str)

print(cookies)

driver.get("https://www.youtube.com/")

for cookie in cookies:
    driver.add_cookie(cookie)

driver.refresh()
# Navigate to YouTube
time.sleep(5000)
# Close the browser when done
driver.quit()
