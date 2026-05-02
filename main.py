import os
import requests
import json
from datetime import datetime, timedelta

BOT_TOKEN = os.getenv("BOT_TOKEN")
CHAT_ID = os.getenv("CHAT_ID")

DATA_FILE = "data.json"

def send(msg):
    url = f"https://api.telegram.org/bot{BOT_TOKEN}/sendMessage"
    requests.post(url, data={"chat_id": CHAT_ID, "text": msg})

def load_data():
    try:
        with open(DATA_FILE, "r") as f:
            return json.load(f)
    except:
        return []

def save_data(data):
    with open(DATA_FILE, "w") as f:
        json.dump(data, f)

def fetch_messages():
    url = f"https://api.telegram.org/bot{BOT_TOKEN}/getUpdates"
    res = requests.get(url).json()

    messages = []
    for item in res.get("result", []):
        if "message" in item and "text" in item["message"]:
            messages.append(item["message"]["text"])
    return messages

def is_elon(text):
    text = text.lower()
    return "elon" in text or "@elonmusk" in text

def update_counts(messages, data):
    today = datetime.utcnow().strftime("%Y-%m-%d")

    count = sum(1 for m in messages if is_elon(m))

    data.append({"date": today, "count": count})
    return data

def analyze(data):
    # last 7 days
    last7 = data[-7:]
    total = sum(d["count"] for d in last7)

    avg = total / len(last7) if last7 else 0

    prediction = int(avg * 7)

    msg = f"""
📊 Elon Tweet Analysis

📅 Last 7 days total: {total}
📈 Daily avg: {avg:.2f}

🔮 Next week prediction:
👉 {prediction} tweets

🧠 Strategy:
{"High activity expected" if avg > 5 else "Normal activity"}
"""
    send(msg)

def main():
    data = load_data()
    messages = fetch_messages()

    data = update_counts(messages, data)
    save_data(data)

    analyze(data)

if __name__ == "__main__":
    main()
