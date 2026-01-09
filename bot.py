import requests
import time
import os

TOKEN = os.getenv("BOT1")
URL = f"https://api.telegram.org/bot{TOKEN}/"

def get_updates(offset=None):
    url = URL + "getUpdates"
    params = {"timeout": 100, "offset": offset}
    response = requests.get(url, params=params)
    return response.json()

def send_message(chat_id, text):
    url = URL + "sendMessage"
    params = {"chat_id": chat_id, "text": text}
    requests.post(url, params=params)

def main():
    print("✅ Bot is running on Railway...")
    last_update_id = None

    while True:
        updates = get_updates(last_update_id)

        if "result" in updates:
            for update in updates["result"]:
                last_update_id = update["update_id"] + 1

                if "message" in update and "text" in update["message"]:
                    chat_id = update["message"]["chat"]["id"]
                    text = update["message"]["text"]

                    if text == "/start":
                        send_message(chat_id, "مرحباً 👋 أنا بوت يعمل على Railway")
                    elif text == "/help":
                        send_message(chat_id, "الأوامر:\n/start\n/help\n/about")
                    elif text == "/about":
                        send_message(chat_id, "بوت Python يعمل 24/24 🚀")
                    else:
                        send_message(chat_id, f"📩 أرسلت: {text}")

        time.sleep(1)

if __name__ == "__main__":
    main()
