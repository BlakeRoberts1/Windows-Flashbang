import os, sys, tkinter as tk
import threading, time, random, pygame
from pynput import mouse, keyboard

CHANCE = 1000
DISPLAY_TIME = 0.2
FADE_TIME = 2.0
SOUND_FILE = "bang.wav"
ENABLE_DEBUG_KEY = False

# Handle PyInstaller resource path
def resource_path(relative_path):
    if hasattr(sys, '_MEIPASS'):
        return os.path.join(sys._MEIPASS, relative_path)
    return os.path.join(os.path.abspath("."), relative_path)

pygame.mixer.init()
bang = pygame.mixer.Sound(resource_path(SOUND_FILE))

root = tk.Tk()
root.withdraw()

flash = tk.Toplevel(root)
flash.attributes("-fullscreen", True)
flash.configure(bg="white")
flash.attributes("-topmost", True)
flash.withdraw()

def flashbang():
    flash.deiconify()
    flash.lift()
    flash.attributes("-alpha", 1.0)
    bang.play()
    time.sleep(DISPLAY_TIME)
    for i in range(50):
        flash.attributes("-alpha", 1 - (i+1)/50)
        flash.update()
        time.sleep(FADE_TIME/50)
    flash.withdraw()

def on_click(x, y, button, pressed):
    if pressed and random.randint(1, CHANCE) == 1:
        threading.Thread(target=flashbang).start()

def on_press(key):
    try:
        if ENABLE_DEBUG_KEY and key == keyboard.Key.f9:
            threading.Thread(target=flashbang).start()
        elif key == keyboard.Key.f10:
            mouse_listener.stop()
            keyboard_listener.stop()
            root.quit()
    except AttributeError:
        pass

mouse_listener = mouse.Listener(on_click=on_click)
keyboard_listener = keyboard.Listener(on_press=on_press)
mouse_listener.start()
keyboard_listener.start()

try:
    root.mainloop()
except KeyboardInterrupt:
    mouse_listener.stop()
    keyboard_listener.stop()
