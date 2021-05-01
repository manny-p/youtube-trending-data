class youTubeStats:

    def __init__(self, api_key, channel_id):
        self.api_key = api_key
        # assert isinstance(channel_id, object)
        self.channel_id = channel_id

    # noinspection PyTypeChecker
    def get_channel_stats(self) -> object:
        payload = 'snippet,statistics,status'
        channels = 'https://www.googleapis.com/youtube/v3/channels'
        url = f'{channels}?id={self.channel_id}&key={self.api_key}&part={payload}'
        print(url)

