import undetected_chromedriver as uc
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import json
import time
import os

def createChannel(
    thumbnailPath: str, 
    bannerPath: str, 
    videoWatermarkImagePath: str, 
    channelDescription: str, 
    contactEmailAddress: str, 
    links: list, 
    email: str, 
    password: str,
    channelHandle: str,
    channelName: str
):
    try:
        signIntoYoutubeUrl = "https://youtube.com"
        channelId = ""
        # Set up Chrome options
        options = uc.ChromeOptions()
        driver = uc.Chrome(options=options)

        # Open YouTube sign-in page
        driver.get(signIntoYoutubeUrl)
        time.sleep(1)

        # Sign in
        email_input = driver.find_element(By.NAME, "identifier")
        if email:
            email_input.send_keys(email)
            email_input.send_keys(Keys.ENTER)
            time.sleep(5)
        else:
            print("Error: Email is None")

        password_input = driver.find_element(By.XPATH, "//input[@name='password']")
        if password:
            password_input.send_keys(password)
            password_input.send_keys(Keys.ENTER)
            time.sleep(15)
        else:
            print("Error: Password is None")

        # Get cookies and quit the driver
        cookies = driver.get_cookies()
        driver.quit()

        # Convert cookies to JSON format
        cookiesStr = json.dumps(cookies)
        cookies = json.loads(cookiesStr)
        time.sleep(5)

        # Set up Chrome options again
        options = uc.ChromeOptions()
        driver = uc.Chrome(options=options)
        driver.get(signIntoYoutubeUrl)

        # Add cookies to the driver session
        for cookie in cookies:
            driver.add_cookie(cookie)

        driver.refresh()
        time.sleep(3)

        # Navigate to create channel page
        profileButton = driver.find_element(By.XPATH, '/html/body/ytd-app/div[1]/div/ytd-masthead/div[4]/div[3]/div[2]/ytd-topbar-menu-button-renderer[2]/button')
        profileButton.click()
        time.sleep(1.5)

        try:
            createChannelLink = driver.find_element(By.XPATH, "//a[text()='Create a channel']")
        except:
            createChannelLink = driver.find_element(By.CSS_SELECTOR, "a:contains('Create a channel')")
        createChannelLink.click()
        time.sleep(2)

        # Fill in channel details
        driver.find_element(By.XPATH, '/html/body/ytd-app/ytd-popup-container/tp-yt-paper-dialog/ytd-channel-creation-dialog-renderer/div/div[5]/div[1]/tp-yt-paper-input/tp-yt-paper-input-container/div[2]/div/iron-input/input').send_keys(Keys.CONTROL, 'a', Keys.BACKSPACE, channelName)
        driver.find_element(By.XPATH, '/html/body/ytd-app/ytd-popup-container/tp-yt-paper-dialog/ytd-channel-creation-dialog-renderer/div/div[5]/div[1]/ytd-channel-handle-input-renderer/tp-yt-paper-input/tp-yt-paper-input-container/div[2]/div/iron-input/input').send_keys(Keys.CONTROL, 'a', Keys.BACKSPACE, channelHandle)
        time.sleep(5)
        driver.find_element(By.XPATH, '/html/body/ytd-app/ytd-popup-container/tp-yt-paper-dialog/ytd-channel-creation-dialog-renderer/div/div[6]/ytd-button-renderer[2]/yt-button-shape/button').click() 
        time.sleep(15)
        # Get channel ID
        channelUrl = driver.current_url
        channelId = channelUrl.split('/')[-1]

        # Navigate to channel editing page
        driver.get(f"https://studio.youtube.com/channel/{channelId}/editing/images")
        time.sleep(3)

        # Upload thumbnail
        driver.find_element(By.CSS_SELECTOR, "input[type='file']").send_keys(os.path.abspath(thumbnailPath))
        time.sleep(3)
        driver.find_element(By.XPATH, "//ytcp-button[contains(text(),'Done')]").click()
        time.sleep(5)

        # Upload banner
        driver.find_element(By.CSS_SELECTOR, "input[type='file']").send_keys(os.path.abspath(bannerPath))
        time.sleep(3)
        driver.find_element(By.XPATH, "//ytcp-button[contains(text(),'Done')]").click()
        time.sleep(5)

        # Scroll to bottom and upload video watermark
        driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
        driver.find_element(By.CSS_SELECTOR, "input[type='file']").send_keys(os.path.abspath(videoWatermarkImagePath))
        time.sleep(3)
        driver.find_element(By.XPATH, "//ytcp-button[contains(text(),'Done')]").click()
        time.sleep(5)

        # Navigate to basic info page
        driver.find_element(By.XPATH, "//ytcp-tab[contains(text(),'Basic info')]").click()
        time.sleep(2)

        # Fill in channel description
        descriptionInput = driver.find_element(By.XPATH, "//div[@placeholder='Add description']")
        descriptionInput.send_keys(Keys.CONTROL, 'a', Keys.BACKSPACE)
        descriptionInput.send_keys(channelDescription)

        # Add links
        for link in links:
            driver.find_element(By.XPATH, "//ytcp-button[contains(text(),'Add link')]").click()
            time.sleep(1)
            driver.find_element(By.CSS_SELECTOR, "input[placeholder='Enter a title']").send_keys(link['title'])
            driver.find_element(By.CSS_SELECTOR, "input[placeholder='Enter a URL']").send_keys(link['link'])

        # Scroll to bottom and fill in contact email
        driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
        time.sleep(2)
        driver.find_element(By.CSS_SELECTOR, "input[placeholder='Email address']").send_keys(contactEmailAddress)

        # Save changes
        driver.find_element(By.XPATH, "//ytcp-button[contains(text(),'Publish')]").click()
        time.sleep(20)

        # Check if channel created successfully
        driver.get(f"https://www.youtube.com/channel/{channelId}")
        print("Channel created successfully")
        return {
            "channelId": channelId,
            "channelName": channelName,
            "channelHandle": channelHandle,
            "channelUrl": channelUrl,
            "cookies": cookies,
            "message": "Channel created successfully"
        }

    except Exception as e:
        print(e)
        print("Error occurred")
        return {
            "message": "Error creating Youtube channel",
            "error": str(e)
        }
