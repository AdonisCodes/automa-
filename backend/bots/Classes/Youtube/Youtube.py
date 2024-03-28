from multiprocessing import Array
from typing import Optional
import Classes.Youtube.methods as methods

class Youtube:
    def __init__(
        self,
        channelCookie=None,
        channelEmail=None,
        channelPassword=None,
        browserProfile=None,
        channelId=None,
    ):
        self.channelCookie = channelCookie
        self.channelEmail = channelEmail
        self.channelPassword = channelPassword
        self.browserProfile = browserProfile
        self.channel = None
        self.channelId = None

    def createChannel(
        self,
        thumbnailPath: str, 
        bannerPath: str, 
        videoWatermarkImagePath: str, 
        channelDescription: str, 
        contactEmailAddress: str, 
        links: list, 
        email: str, 
        password: str,
        channelHandle: str,
        channelName: str,
    ):
        methods.createChannel(
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
