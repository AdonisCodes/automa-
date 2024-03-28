from dotenv import load_dotenv
import os
from dotenv import load_dotenv
from Classes.Youtube.Youtube import Youtube

# Load environment variables from the specified .env file
dotenvPath = '../../../../../.env'
load_dotenv(dotenvPath)

# Create Youtube Channel
thumbnailPath = "./thumbnail.png"
bannerPath = "./banner.png"
videoWatermarkImagePath = "./thumbnail.png" channelDescription = "Welcome to my channel!"
contactEmailAddress = "willfv2@gmail.com"
links = [
    {"title": "Title of link 1", "link": "https://www.google.com"},
    {"title": "Title of link 2", "link": "https://www.google.com"},
    {"title": "Title of link 3", "link": "https://www.google.com"},
    {"title": "Title of link 4", "link": "https://www.google.com"},
    {"title": "Title of link 5", "link": "https://www.google.com"},
]

# Retrieve email and password from environment variables
email = os.getenv("TEST_EMAIL") or ""
password = os.getenv("TEST_PASSWORD") or ""
channelName = "williamadonis"
channelHandle = ""

# Instantiate Youtube Class:
youtube = Youtube()

# Create Channel
createChannelResponse = youtube.createChannel(
    thumbnailPath,
    bannerPath,
    videoWatermarkImagePath,
    channelDescription,
    contactEmailAddress,
    links,
    email,
    password,
    channelHandle,
    channelName,
)

# Load environment variables from the specified .env file
dotenvPath = '../../../../../.env'
load_dotenv(dotenvPath)

# Create Youtube Channel
thumbnailPath = "./thumbnail.png"
bannerPath = "./banner.png"
videoWatermarkImagePath = "./thumbnail.png"
channelDescription = "Welcome to my channel!"
contactEmailAddress = "willfv2@gmail.com"
links = [
    {"title": "Title of link 1", "link": "https://www.google.com"},
    {"title": "Title of link 2", "link": "https://www.google.com"},
    {"title": "Title of link 3", "link": "https://www.google.com"},
    {"title": "Title of link 4", "link": "https://www.google.com"},
    {"title": "Title of link 5", "link": "https://www.google.com"},
]

# Retrieve email and password from environment variables
email = os.getenv("TEST_EMAIL") or ""
password = os.getenv("TEST_PASSWORD") or ""
channelName = "williamadonis"
channelHandle = ""

# Instantiate Youtube Class:
youtube = Youtube()

# Create Channel
createChannelResponse = youtube.createChannel(
    thumbnailPath,
    bannerPath,
    videoWatermarkImagePath,
    channelDescription,
    contactEmailAddress,
    links,
    email,
    password,
    channelHandle,
    channelName,
)

