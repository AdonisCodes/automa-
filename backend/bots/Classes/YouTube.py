from typing import Optional, Union, Literal

class Youtube: """
    This class is used to interact with the YouTube, for getting data primarily. 

    Attributes:
        channelId: A string representing the channel ID, or the url of the channel.
        videoUrl: A string representing the video URL.
        searchQuery: A string representing the search query.
        shortUrl: A string representing the short URL.
        communityPostUrl: A string representing the community post URL.
        playlistUrl: A string representing the playlist URL.
        unsureUrl: A string representing the unsure URL.
    Methods:
        getChannelInfo: Gets channel info based off of the url.
        getVideoInfo: Gets video info based off of the url.
        makeSearchQuery: Searches for a query, and returns a structured output of the search query.
        getShortInfo: Gets the information from a specific short.
        playlistUrl: Gets data from a playlist, in a well structured format.
        queryUnsureUrl: Opens up a url, where you are not sure what the url entirely is, and returns formatted data.
    """
    def __init__(
        self, 
        channelId: Optional[str] = None, 
        videoUrl: Optional[str] = None, 
        searchQuery: Optional[str] = None,
        shortUrl: Optional[str] = None,
        communityPostUrl: Optional[str] = None,
        unsureUrl: Optional[str] = None,
        playlistUrl: Optional[str] = None,
    ):
        """
        The constructor for the Youtube class.

        Args:
            attribute1: value for attribute 1
        """
        # Initialize any necessary variables or resources
        self.videoUrl = videoUrl
        self.channelId = channelId
        self.searchQuery = searchQuery
        self.shortUrl = shortUrl
        self.communityPostUrl = communityPostUrl
        self.unsureUrl = unsureUrl 
        self.playlistUrl = playlistUrl 

    def getChannelInfo(
        self, 
        channelId: Optional[str] = None, 
        exportType: Union[Literal["json"], Literal["txt"], Literal["csv"]] = "json"
    ):
        """
        Gets channel info based off of the url.
        """
        # Fetch general information about the channel
        pass
    
# class YoutubeChannel:
#     def __init__(self, channel_id):
#         # Initialize with the channel ID
#     
#     def get_channel_info(self):
#         # Fetch general information about the channel
#         pass
#     
#     def get_videos(self):
#         # Fetch videos associated with the channel
#         pass
#     
#     def upload_video(self, video_data):
#         # Upload a video to this channel
#         pass
#
# class YoutubeVideo:
#     def __init__(self, video_id):
#         # Initialize with the video ID
#     
#     def get_video_info(self):
#         # Fetch general information about the video
#         pass
#     
#     def get_video_stats(self):
#         # Fetch statistics for the video
#         pass
