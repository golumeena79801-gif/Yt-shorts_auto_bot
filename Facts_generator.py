import openai
import os

openai.api_key = os.getenv("OPENAI_API_KEY")

prompt = """
10 VIRAL psychological facts Hindi me generate karo.
Har fact ek line ka ho, catchy ho, and mind-blowing.
YouTube Shorts style me do.
"""

res = openai.ChatCompletion.create(
    model="gpt-4o-mini",
    messages=[{"role": "user", "content": prompt}]
)

facts = res.choices[0].message["content"]

with open("facts.txt", "w", encoding="utf-8") as f:
    f.write(facts)
