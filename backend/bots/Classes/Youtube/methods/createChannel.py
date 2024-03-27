import undetected_chromedriver as uc
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import random
import time

def createChannel():
    signIntoYoutubeUrl = "https://youtube.com"
    email = "willfv2@gmail.com"
    
    # Set up undetected_chromedriver
    options = uc.ChromeOptions()
    # options.add_argument("--headless")
    driver = uc.Chrome(options=options)
    
    driver.get(signIntoYoutubeUrl)
    
    # Wait for the page to load
    time.sleep(1.2)
    driver.save_screenshot("1_page_load.png")
    
    # Click on the "Sign in" button
    driver.find_element(By.LINK_TEXT, "Sign in").click()
    time.sleep(0.5)  # Adjust sleep duration based on page load time
    driver.save_screenshot("2_sign_in_clicked.png")
    
    # Simulate typing the email address
    email_input = driver.find_element(By.NAME, "identifier")
    for char in email:
        email_input.send_keys(char)
        time.sleep(random.uniform(0.1, 0.35))
    driver.save_screenshot("3_email_typed.png")
    time.sleep(550000)
    
    # Press Enter to submit the email
    email_input.send_keys(Keys.ENTER)
    time.sleep(0.5)  # Adjust sleep duration based on page load time
    # Click the element with the specified text using XPath
    text_to_click = "Try again"
    while driver.find_element(by="xpath", value=f"//*[text()='{text_to_click}']"):
        element = driver.find_element(by="xpath", value=f"//*[text()='{text_to_click}']")
        element.click()
    
    # Simulate typing the email address again (if necessary)
    for char in email:
        driver.send_keys(char)
        time.sleep(random.uniform(0.1, 0.35))
    driver.save_screenshot("5_email_typed_again.png")
    
    # Click on the "Next" button
    nextButton = driver.find_element(by="xpath", value=f"//*[text()='Next']")
    nextButton.click()
    time.sleep(0.5)  # Adjust sleep duration based on page load time
    driver.save_screenshot("6_next_button_clicked.png")
    
    print("Done.")
    driver.quit()
    time.sleep(5)

createChannel()
