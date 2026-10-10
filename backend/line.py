import urllib.request
import json
import os

def send_line(msg):
    token = os.getenv("LINE_TOKEN")
    url = "https://api.line.me/v2/bot/message/broadcast"
    data = json.dumps({"messages": [{"type": "text", "text": msg}]}, ensure_ascii=False).encode("utf-8")
    headers = {
        "Content-Type": "application/json",
        "Authorization": f"Bearer {token}"
    }
    req = urllib.request.Request(url, data=data, headers=headers)
    urllib.request.urlopen(req)