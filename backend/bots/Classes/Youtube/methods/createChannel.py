import undetected_chromedriver as uc
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import random
import time

def createChannel():
    signIntoYoutubeUrl = "https://youtube.com"
    email = "adonisdevelops@gmail.com"
    password = "Adonis2024"
    
    # Set up undetected_chromedriver
    options = uc.ChromeOptions()
    # options.add_argument("--headless")
    driver = uc.Chrome(options=options)
    
    driver.get(signIntoYoutubeUrl)
    
    # Wait for the page to load
    time.sleep(1.2)
    
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
    
    
    # Click on the "Next" button
    print("Done.")
    driver.quit()


createChannel()
