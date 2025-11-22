from moviepy.editor import *
import textwrap

facts = open("facts.txt", "r", encoding="utf-8").read()

# Background
clip = ColorClip(size=(1080, 1920), color=(0, 0, 0), duration=20)

# Convert text
wrapped = "\n".join(textwrap.wrap(facts, 40))

txt = TextClip(
    wrapped,
    fontsize=70,
    color="yellow",
    font="Arial-Bold",
    method="caption",
    size=(900, None)
).set_position("center").set_duration(20)

audio = AudioFileClip("voice.mp3")

final = CompositeVideoClip([clip, txt]).set_audio(audio)

final.write_videofile("final_video.mp4", fps=30)
