import undetected_chromedriver as uc
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import random
import json
import time
from dotenv import load_dotenv
import os

# Specify the path to the .env file
dotenv_path = '../../../../../.env'

# Load environment variables from the specified .env file
load_dotenv(dotenv_path)

def createChannel():
    signIntoYoutubeUrl = "https://youtube.com"
    email = os.getenv("TEST_EMAIL")
    password = os.getenv("TEST_PASSWORD")
    print(email)    
    print(password)
    # Set up undetected_chromedriver
    options = uc.ChromeOptions()
    # options.add_argument("--headless")
    driver = uc.Chrome(options=options)
    
    driver.get(signIntoYoutubeUrl)
    
    # Wait for the page to load time.sleep(1.2)
    
    # Click on the "Sign in" button
    driver.find_element(By.LINK_TEXT, "Sign in").click()
    time.sleep(0.5)  # Adjust sleep duration based on page load time
    
    # Simulate typing the email address
    emailInput = driver.find_element(By.NAME, "identifier")
    emailInput.send_keys(email)
    
    # Press Enter to submit the email
    emailInput.send_keys(Keys.ENTER)
    time.sleep(5)
    # Find the password input with type="password"
    passwordInput = driver.find_element(By.XPATH, "/html/body/div[1]/div[1]/div[2]/c-wiz/div/div[2]/div/div/div/form/span/section[2]/div/div/div[1]/div[1]/div/div/div/div/div[1]/div/div[1]/input")
    passwordInput.send_keys(password)
    passwordInput.send_keys(Keys.ENTER)
    
    time.sleep(15)    
    # Once signed in, get cookies
    cookies = driver.get_cookies()
    driver.quit()
    # Print cookies
    print(cookies)

    # Replace single quotes with double quotes

    cookies_str = str(cookies).replace("'", '"').replace("True", "true").replace("False", "false")

    # Ensure proper formatting
    # cookies_str = cookies_str.replace(", {", "}, {")

    # Load the JSON
    cookies = json.loads(cookies_str)
    time.sleep(5)

    options = uc.ChromeOptions()
    driver = uc.Chrome(options=options)
    driver.get(signIntoYoutubeUrl)

    for cookie in cookies:
        driver.add_cookie(cookie)

    driver.refresh()
    # Close the browser when done
    driver.quit()


createChannel()
