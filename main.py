import os
import requests


def webhook(request):
    # Telegram sends updates as JSON in the body
    data = request.get_json(silent=True) or {}
    token = os.environ.get("TELEGRAM_TOKEN")
    if not token or not data:
        return "ok"
    message = data.get("message", {})
    new_members = message.get("new_chat_members", [])
    chat = message.get("chat", {})
    chat_id = chat.get("id")
    for member in new_members:
        first_name = member.get("first_name", "друг")
        text = f"Привет, {first_name}! Добро пожаловать в группу!"
        url = f"https://api.telegram.org/bot{token}/sendMessage"
        payload = {"chat_id": chat_id, "text": text}
        try:
            requests.post(url, json=payload, timeout=10)
        except Exception:
            pass
    return "ok"
