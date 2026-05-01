import os
import requests

# ===== GET SECRETS =====
API_ID = os.getenv("33911412")
API_HASH = os.getenv("4acad418f87f623347a8ca83f3b168a9")
BOT_TOKEN = os.getenv("8790935199:AAHTjA6v2G4FHVmbgb-EnkxHLgTIyivZ1Kg")
CHAT_ID = os.getenv("7171044211")

# ===== CHECK =====
if not BOT_TOKEN or not CHAT_ID:
    raise Exception("❌ BOT_TOKEN or CHAT_ID missing in secrets")

# ===== SEND TELEGRAM =====
def send(msg):
    url = f"https://api.telegram.org/bot{BOT_TOKEN}/sendMessage"
    requests.post(url, data={"chat_id": CHAT_ID, "text": msg})

# ===== MAIN =====
def main():
    send("✅ Bot is running on GitHub successfully!")

if __name__ == "__main__":
    main()
