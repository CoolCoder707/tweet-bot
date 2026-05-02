import os
import requests
import xml.etree.ElementTree as ET
from datetime import datetime

BOT_TOKEN = os.getenv("BOT_TOKEN")
CHAT_ID = os.getenv("CHAT_ID")

def send(msg):
    url = f"https://api.telegram.org/bot{BOT_TOKEN}/sendMessage"
    requests.post(url, data={"chat_id": CHAT_ID, "text": msg})

def fetch_tweets():
    url = "https://nitter.net/elonmusk/rss"
    res = requests.get(url)

    root = ET.fromstring(res.content)

    tweets = []
    for item in root.findall(".//item"):
        title = item.find("title").text
        pub = item.find("pubDate").text
        tweets.append((title, pub))

    return tweets

def analyze(tweets):
    now = datetime.utcnow()

    # last 24h count
    count = len(tweets)

    # simple prediction
    prediction = count * 7

    msg = f"""
📊 Elon Tweet Analysis

🕒 Last fetch tweets: {count}

📈 Estimated weekly tweets:
👉 {prediction}

🧠 Insight:
{"High activity week" if count > 5 else "Normal activity"}
"""
    send(msg)

def main():
    tweets = fetch_tweets()
    analyze(tweets)

if __name__ == "__main__":
    main()
