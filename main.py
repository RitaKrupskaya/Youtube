import os
import json

from googleapiclient.discovery import build


class Channel():
    def __init__(self, channel_id):
        self.channel_id = channel_id
        api_key: str = os.getenv('SKYPROAPIKEY')
        youtube = build('youtube', 'v3', developerKey=api_key)
        self.channel = channel_info = youtube.channels().list(id=channel_id, part='snippet,statistics').execute()

    def print_info(self):
        print(json.dumps(self.channel, indent=2, ensure_ascii=False))


a_pogovorit = Channel('UCp2J7GRxQ36QLqW4ReLLt5g')
a_pogovorit.print_info()
