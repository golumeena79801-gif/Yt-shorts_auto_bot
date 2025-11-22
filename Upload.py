from googleapiclient.discovery import build
from googleapiclient.http import MediaFileUpload
import os

yt_key = os.getenv("YOUTUBE_API_KEY")

youtube = build("youtube", "v3", developerKey=yt_key)

request = youtube.videos().insert(
    part="snippet,status",
    body={
        "snippet": {
            "title": "10 मन उड़ाने वाले Psychological Facts 🤯 | #shorts",
            "description": "Daily Hindi Psychological Facts | #shorts #facts",
            "tags": ["facts", "psychology", "hindi shorts"],
            "categoryId": "22"
        },
        "status": {"privacyStatus": "public"}
    },
    media_body=MediaFileUpload("final_video.mp4")
)

request.execute()￼Enter
