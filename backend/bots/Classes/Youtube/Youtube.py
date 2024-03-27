import methods
from typing import Optional


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
        channelName: str,
        email: str,
        password: str,
        channelUsername: Optional[str],
        profilePicture=None,
        channelBio=None,
        channelLinks=None,
    ):
        # TODO: Create a new channel.
        methods.createChannel(
            channelName, email, password, channelUsername, profilePicture, channelBio
        )
