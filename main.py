import os
import requests

BOT_TOKEN = os.getenv("4acad418f87f623347a8ca83f3b168a9")
CHAT_ID = os.getenv("33911412")

if not BOT_TOKEN or not CHAT_ID:
    raise Exception("❌ BOT_TOKEN or CHAT_ID missing")

def send(msg):
    url = f"https://api.telegram.org/bot{BOT_TOKEN}/sendMessage"
    requests.post(url, data={"chat_id": CHAT_ID, "text": msg})

def main():
    send("✅ Bot is LIVE and working!")

if __name__ == "__main__":
    main()
