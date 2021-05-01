from youtube_statistics import youTubeStats
from config import API_KEY


channel_id0: str = 'UCvtRTOMP2TqYqu51xNrqAzg'

youtube = youTubeStats(API_KEY, channel_id0)
youtube.get_channel_stats()

