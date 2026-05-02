import os
import requests

# ===== GET SECRETS =====
- name: Run bot
  env:
    API_ID: ${{ secrets.API_ID }}
    API_HASH: ${{ secrets.API_HASH }}
    BOT_TOKEN: ${{ secrets.BOT_TOKEN }}
    CHAT_ID: ${{ secrets.CHAT_ID }}
  run: python main.py

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
