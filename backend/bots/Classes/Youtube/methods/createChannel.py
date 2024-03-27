# Import necessary libraries
import undetected_chromedriver as uc
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import random
import json
import time
from dotenv import load_dotenv
import os

# Specify the path to the .env file
dotenvPath = '../../../../../.env'

# Load environment variables from the specified .env file
load_dotenv(dotenvPath)

# Function to create a YouTube channel
def createChannel():
    # URL for signing into YouTube
    signIntoYoutubeUrl = "https://youtube.com"
    
    # Retrieve email and password from environment variables
    email = os.getenv("TEST_EMAIL")
    password = os.getenv("TEST_PASSWORD")

    # Set up Chrome options
    options = uc.ChromeOptions()
    driver = uc.Chrome(options=options)
    
    # Open YouTube sign-in page
    driver.get(signIntoYoutubeUrl)
    
    # Click on the "Sign in" link
    driver.find_element(By.LINK_TEXT, "Sign in").click()
    time.sleep(0.5)  # Adjust sleep duration based on page load time
    
    # Enter email and proceed
    emailInput = driver.find_element(By.NAME, "identifier")
    emailInput.send_keys(email)
    emailInput.send_keys(Keys.ENTER)
    time.sleep(5)

    # Enter password and proceed
    passwordInput = driver.find_element(By.XPATH, "/html/body/div[1]/div[1]/div[2]/c-wiz/div/div[2]/div/div/div/form/span/section[2]/div/div/div[1]/div[1]/div/div/div/div/div[1]/div/div[1]/input")
    passwordInput.send_keys(password)
    passwordInput.send_keys(Keys.ENTER)
    
    time.sleep(15)  # Adjust sleep duration based on page load time

    # Once signed in, get cookies and quit the driver
    cookies = driver.get_cookies()
    driver.quit()

    # Convert cookies to JSON format
    cookies_str = str(cookies).replace("'", '"').replace("True", "true").replace("False", "false")
    cookies = json.loads(cookies_str)
    time.sleep(5)

    # Set up Chrome options again
    options = uc.ChromeOptions()
    driver = uc.Chrome(options=options)
    driver.get(signIntoYoutubeUrl)

    # Add cookies to the driver session
    for cookie in cookies:
        driver.add_cookie(cookie)

    # Refresh the page to apply cookies and quit the driver
    driver.refresh()
    driver.quit()

# Call the function to create a YouTube channel
createChannel()

# TODO: Make functionality to create Youtube channel, and return cookies and a success message - whether or not the channel creation was successful or not.
