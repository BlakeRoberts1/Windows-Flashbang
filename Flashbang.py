import tkinter as tk
import threading, time, random, pygame, sys, os
from pynput import mouse, keyboard
from ctypes import cast, POINTER
from comtypes import CLSCTX_ALL
from pycaw.pycaw import AudioUtilities, IAudioEndpointVolume

CHANCE = 1000
DISPLAY_TIME = 0.2
FADE_TIME = 2.0
SOUND_FILE = "bang.wav"
FORCE_MAX_VOLUME = True
ENABLE_DEBUG_KEY = False

# Helper to get resource path (works in PyInstaller --onefile)
def resource_path(relative_path):
    if hasattr(sys, "_MEIPASS"):
        return os.path.join(sys._MEIPASS, relative_path)
    return os.path.join(os.path.abspath("."), relative_path)

# Initialize pygame mixer and load sound
pygame.mixer.init()
bang = pygame.mixer.Sound(resource_path(SOUND_FILE))

# Tkinter setup
root = tk.Tk()
root.withdraw()

flash = tk.Toplevel(root)
flash.attributes("-fullscreen", True)
flash.configure(bg="white")
flash.attributes("-topmost", True)
flash.withdraw()

# Volume control
if FORCE_MAX_VOLUME:
    devices = AudioUtilities.GetSpeakers()
    interface = devices.Activate(IAudioEndpointVolume._iid_, CLSCTX_ALL, None)
    volume = cast(interface, POINTER(IAudioEndpointVolume))
    def get_volume(): return volume.GetMasterVolumeLevelScalar()
    def set_volume(level): volume.SetMasterVolumeLevelScalar(level, None)
else:
    def get_volume(): return 0.5
    def set_volume(level): pass

# Flashbang effect
def flashbang():
    prev_vol = get_volume()
    if FORCE_MAX_VOLUME: set_volume(1.0)
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
    if FORCE_MAX_VOLUME: set_volume(prev_vol)

# Mouse click handler
def on_click(x, y, button, pressed):
    if pressed and random.randint(1, CHANCE) == 1:
        threading.Thread(target=flashbang).start()

# Keyboard handler
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
