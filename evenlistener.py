# keybinds.py
from pynput import keyboard
import pyautogui
import time
import os
import json
import requests


def send_to_discord(webhook_url, message, image_path):
    data = {
        "content": message
    }
    with open(image_path, 'rb') as f:
        files = {'file': f}
        requests.post(webhook_url, data={"payload_json": json.dumps(data)}, files=files, timeout=10)
    os.remove(image_path)


def handle_screenshot(message, webhook_url):
    filename = f"screenshot_{int(time.time())}.png"
    screenshot = pyautogui.screenshot()
    screenshot.save(filename)
    send_to_discord(webhook_url, message, filename)


def start_keybind_listener():
    message = "📸 Quick screenshot!"
    webhook_url = ""

    def on_press(key):
        if key == keyboard.Key.f8:
            handle_screenshot(message, webhook_url)

    with keyboard.Listener(on_press=on_press) as listener:
        listener.join()
