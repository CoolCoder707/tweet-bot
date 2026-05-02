import os
import requests
from datetime import datetime

BOT_TOKEN = os.getenv("BOT_TOKEN")
CHAT_ID = os.getenv("CHAT_ID")

def send(msg):
    url = f"https://api.telegram.org/bot{BOT_TOKEN}/sendMessage"
    requests.post(url, data={"chat_id": CHAT_ID, "text": msg})

def is_elon_tweet(text):
    text = text.lower()
    return "elon" in text or "@elonmusk" in text

def analyze_message(text):
    if not is_elon_tweet(text):
        return None
    
    now = datetime.utcnow()

    return f"""
🚨 ELON ALERT 🚨

🕒 Time: {now}
📢 Detected Elon Musk tweet

⚡ Signal: HIGH IMPACT
🚀 Stay ready for market move
"""

# TEMP test (next step me real channel data aayega)
def main():
    sample = "Elon Musk tweeted: Doge to the moon 🚀"
    
    result = analyze_message(sample)
    
    if result:
        send(result)

if __name__ == "__main__":
    main()
