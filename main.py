import os
import requests
from datetime import datetime

BOT_TOKEN = os.getenv("BOT_TOKEN")
CHAT_ID = os.getenv("CHAT_ID")

def send(msg):
    url = f"https://api.telegram.org/bot{BOT_TOKEN}/sendMessage"
    requests.post(url, data={"chat_id": CHAT_ID, "text": msg})

def analyze():
    now = datetime.utcnow()

    # simple dummy logic (next upgrade me real data)
    hour = now.hour

    msg = f"""
📊 Tweet Activity Report

🕒 Hour: {hour}
🔥 Status: ACTIVE

🤖 Prediction:
High chance of tweets in next 1-2 hours

⚡ Signal:
Stay alert for meme coins 🚀
"""

    send(msg)

if __name__ == "__main__":
    analyze()
