import requests
import os

API_KEY = os.getenv("ELEVEN_API_KEY")
voice_id = "EXAVITQu4vr4xnSDxMaL"

text = open("facts.txt", "r", encoding="utf-8").read()

audio = requests.post(
    f"https://api.elevenlabs.io/v1/text-to-speech/{voice_id}",
    json={"text": text},
    headers={"xi-api-key": API_KEY},
)

with open("voice.mp3", "wb") as f:
    f.write(audio.content)
