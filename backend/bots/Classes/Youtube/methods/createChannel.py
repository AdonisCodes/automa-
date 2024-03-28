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
    channelName = "williamfernsishere"
    channelHandle = "williamfernsishere12523"
    channelId = ""
    thumbnailPath = "./thumbnail.png"
    bannerPatth = "./banner.png"
    channelDescription = "Welcome to my channel!"
    contactEmailAddress = "willfv2@gmail.com"
    links = [
        {
            "title": "Title of link 1",
            "link": "https://www.google.com"
        },
        {
            "title": "Title of link 1",
            "link": "https://www.google.com"
        },
        {
            "title": "Title of link 1",
            "link": "https://www.google.com"
        },
        {
            "title": "Title of link 1",
            "link": "https://www.google.com"
        },
        {
            "title": "Title of link 1",
            "link": "https://www.google.com"
        },
    ]

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
    cookiesStr = str(cookies).replace("'", '"').replace("True", "true").replace("False", "false")
    cookies = json.loads(cookiesStr)
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
# TODO: Make functionality to create Youtube channel, and return cookies and a success message - whether or not the channel creation was successful or not.
    time.sleep(5000000)

    profileButton = driver.find_element(By.ID, 'avatar-btn')
    profileButton.click()

    # Find the anchor tag by its text using XPath
    xpath = "//a[contains(text(),'Create a channel')]"
    createChannelLink = driver.find_element(By.XPATH, xpath)
    # Click the anchor tag
    createChannelLink.click()

    nameInput = driver.find_element(By.XPATH, '/html/body/ytd-app/ytd-popup-container/tp-yt-paper-dialog/ytd-channel-creation-dialog-renderer/div/div[5]/div[1]/tp-yt-paper-input/tp-yt-paper-input-container/div[2]/div/iron-input/input')
    nameInput.click()

    # Simulate pressing Ctrl+A (or Command+A on macOS) to select all text
    nameInput.send_keys(Keys.CONTROL, 'a')

    # Simulate pressing the Backspace key to delete the selected text
    nameInput.send_keys(Keys.BACKSPACE)
    nameInput.send_keys(channelName)

    channelHandleInput = driver.find_element(By.XPATH, '/html/body/ytd-app/ytd-popup-container/tp-yt-paper-dialog/ytd-channel-creation-dialog-renderer/div/div[5]/div[1]/ytd-channel-handle-input-renderer/tp-yt-paper-input/tp-yt-paper-input-container/div[2]/div/iron-input/input')
    channelHandleInput.click()
    channelHandleInput.send_keys(Keys.CONTROL, 'a')
    channelHandleInput.send_keys(Keys.BACKSPACE)
    channelHandleInput.send_keys(channelHandle)

    # Just waiting for youtube to check if the handle is valid
    time.sleep(5)

    createChannelButton = driver.find_element(By.XPATH, '/html/body/ytd-app/ytd-popup-container/tp-yt-paper-dialog/ytd-channel-creation-dialog-renderer/div/div[6]/ytd-button-renderer[2]/yt-button-shape/button')
    createChannelButton.click()

    # Waiting for channel to create
    time.sleep(15)

    # Getting current url, this is the channel url
    channelUrl = driver.current_url
    channelId = channelUrl.split('/')[-1]
    print("Channel ID", channelId)

    # Go to the editing page.
    driver.get(f"https://studio.youtube.com/channel/{channelId}/editing/images")

    uploadThumbnailInput = driver.find_element(By.XPATH, "/html/body/ytcp-app/ytcp-entity-page/div/div/main/div/ytcp-animatable[6]/ytcp-channel-editing-section/iron-pages/div[2]/ytcp-channel-editing-images-tab/div/section[1]/ytcp-profile-image-upload/div/div[3]/div[2]/div[2]/input")
    uploadThumbnailInput.send_keys(os.path.abspath(thumbnailPath))
    doneButton = driver.find_element(By.XPATH, "/html/body/ytcp-profile-image-editor/ytcp-dialog/tp-yt-paper-dialog/div[3]/div/ytcp-button[2]")
    doneButton.click()
    time.sleep(5)

    uploadBannerInput = driver.find_element(By.XPATH, "/html/body/ytcp-app/ytcp-entity-page/div/div/main/div/ytcp-animatable[6]/ytcp-channel-editing-section/iron-pages/div[2]/ytcp-channel-editing-images-tab/div/section[2]/ytcp-banner-upload/div/div[3]/div[2]/div[2]/input")
    uploadBannerInput.send_keys(os.path.abspath(bannerPatth))
    doneButton = driver.find_element(By.XPATH, "/html/body/ytcp-banner-editor/ytcp-dialog/tp-yt-paper-dialog/div[3]/div/ytcp-button[2]")
    doneButton.click()
    time.sleep(5)

    # Go to basic info page:
    driver.get(f"https://studio.youtube.com/channel/{channelId}/editing/details")

    # Just filling in description, as name and tag was already set above.
    descriptionInput = driver.find_element(By.XPATH, "/html/body/ytcp-app/ytcp-entity-page/div/div/main/div/ytcp-animatable[6]/ytcp-channel-editing-section/iron-pages/div[3]/ytcp-channel-editing-details-tab/div/section[1]/ytcp-social-suggestions-textbox/ytcp-form-input-container/div[1]/div[2]/div/ytcp-social-suggestion-input/div")
    try:
        descriptionInput.send_keys(channelDescription)
    except Exception as e:
        print("Error", e)
        # Execute JavaScript to change the text content of the element
        driver.execute_script(f"arguments[0].textContent = '{channelDescription}'", descriptionInput)
    driver.quit()

    for link in links:
        # Add links:
        addLinkButton = driver.find_element(By.XPATH, "/html/body/ytcp-app/ytcp-entity-page/div/div/main/div/ytcp-animatable[6]/ytcp-channel-editing-section/iron-pages/div[3]/ytcp-channel-editing-details-tab/div/ytcp-channel-links/div/ytcp-button")
        addLinkButton.click()

        # Find all input fields by their placeholder attribute
        linkTitleInputs = driver.find_elements(By.CSS_SELECTOR, "input[placeholder='Enter a title']")

        # Iterate through each input field
        for linkTitleInput in linkTitleInputs:
            # Check if the input field is empty by examining its text content
            if not linkTitleInput.get_attribute("value") and not linkTitleInput.text:
                linkTitleInput.click()
                linkTitleInput.send_keys(link['title'])

        # Find all input fields by their placeholder attribute
        linkUrlInputs = driver.find_elements(By.CSS_SELECTOR, "input[placeholder='Enter a URL']")

        # Iterate through each input field
        for linkUrlInput in linkUrlInputs:
            # Check if the input field is empty by examining its text content
            if not linkUrlInput.get_attribute("value") and not linkUrlInput.text:
                linkUrlInput.click()
                linkUrlInput.send_keys(link['link'])
    
    contactInfoInput = driver.find_element(By.CSS_SELECTOR, "input[placeholder'Email address']")
    contactInfoInput.click()
    contactInfoInput.send_keys(contactEmailAddress)

    # Save the changes
    publishButton = driver.find_element(By.XPATH, "/html/body/ytcp-app/ytcp-entity-page/div/div/main/div/ytcp-animatable[6]/ytcp-channel-editing-section/ytcp-sticky-header/ytcp-primary-action-bar/div/div[2]/ytcp-button[3]")
    publishButton.click()

    # Wait to publish
    time.sleep(20)

# Click
# Call the function to create a YouTube channel
createChannel()
