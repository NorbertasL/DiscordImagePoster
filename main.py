# main.py
import threading
import os
from pystray import Icon, MenuItem as item, Menu
from PIL import Image, ImageDraw
from gui import main_config_gui
from evenlistener import start_keybind_listener


def create_tray_icon():
    # Simple icon
    image = Image.new('RGB', (64, 64), color='black')
    draw = ImageDraw.Draw(image)
    draw.rectangle((16, 16, 48, 48), fill='white')

    menu = Menu(
        item('Open Config', lambda icon, item: main_config_gui()),
        item('Quit', lambda icon, item: os._exit(0))
    )
    tray = Icon("ScreenshotBot", icon=image, menu=menu)
    tray.run()


if __name__ == '__main__':
    threading.Thread(target=start_keybind_listener, daemon=True).start()
    create_tray_icon()
