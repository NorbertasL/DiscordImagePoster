import pystray
from pystray import MenuItem as item
from PIL import Image, ImageDraw
from threading import Thread
from pynput import keyboard
import pyautogui
import requests
import time
import os
import json


WEBHOOK_URL = ""
ROLE_ID = "123456789012345678"

def take_screenshot():
    filename = f"screenshot_{int(time.time())}.png"
    screenshot = pyautogui.screenshot()
    screenshot.save(filename)
    return filename

def send_to_discord(image_path):
    data = {
        "content": f"📸 New Screenshot! <@&{ROLE_ID}>",
        "allowed_mentions": {
            "roles": [ROLE_ID]
        }
    }
    with open(image_path, 'rb') as f:
        files = {'file': f}
        requests.post(WEBHOOK_URL, data={"payload_json": json.dumps(data)}, files=files, timeout=10)
    os.remove(image_path)

def on_press(key):
    if key == keyboard.Key.f8:
        filepath = take_screenshot()
        send_to_discord(filepath)

def listen_keyboard():
    with keyboard.Listener(on_press=on_press) as listener:
        listener.join()

def create_image():
    # Create a simple icon
    image = Image.new('RGB', (64, 64), color='black')
    draw = ImageDraw.Draw(image)
    draw.rectangle((16, 16, 48, 48), fill='white')
    return image

def on_quit(icon, item):
    icon.stop()
    os._exit(0)  # Ensure listener thread is terminated

def run_tray_icon():
    icon = pystray.Icon("ScreenshotBot")
    icon.icon = create_image()
    icon.menu = pystray.Menu(item('Quit', on_quit))
    icon.run()

# Run both tray and listener in separate threads
Thread(target=listen_keyboard, daemon=True).start()
run_tray_icon()
