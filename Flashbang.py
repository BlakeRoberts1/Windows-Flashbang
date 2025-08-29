import tkinter as tk
import threading, time, random, pygame, sys, os
from pynput import mouse, keyboard
from ctypes import cast, POINTER
from comtypes import CLSCTX_ALL
from pycaw.pycaw import AudioUtilities, IAudioEndpointVolume

CHANCE = 1000
DISPLAY_TIME = 0.2
FADE_TIME = 2.0
ENABLE_DEBUG_KEY = True

if getattr(sys, 'frozen', False):
    base_path = sys._MEIPASS
else:
    base_path = os.path.dirname(__file__)

SOUND_FILE = os.path.join(base_path, "bang.wav")

pygame.mixer.init()
bang = pygame.mixer.Sound(SOUND_FILE)

root = tk.Tk()
root.withdraw()

flash = tk.Toplevel(root)
flash.attributes("-fullscreen", True)
flash.configure(bg="white")
flash.attributes("-topmost", True)
flash.withdraw()

devices = AudioUtilities.GetSpeakers()
interface = devices.Activate(IAudioEndpointVolume._iid_, CLSCTX_ALL, None)
volume = cast(interface, POINTER(IAudioEndpointVolume))

def get_volume():
    return volume.GetMasterVolumeLevelScalar()

def set_volume(level):
    volume.SetMasterVolumeLevelScalar(level, None)

def set_all_app_volumes(level):
    sessions = AudioUtilities.GetAllSessions()
    for session in sessions:
        vol = session.SimpleAudioVolume
        vol.SetMasterVolume(level, None)

def flashbang():
    prev_vol = get_volume()
    set_volume(1.0)
    set_all_app_volumes(1.0)
    flash.deiconify()
    flash.lift()
    flash.attributes("-alpha", 1.0)
    bang.play()
    time.sleep(DISPLAY_TIME)
    for i in range(50):
        flash.attributes("-alpha", 1 - (i + 1) / 50)
        flash.update()
        time.sleep(FADE_TIME / 50)
    flash.withdraw()
    set_volume(prev_vol)

def on_click(x, y, button, pressed):
    if pressed and random.randint(1, CHANCE) == 1:
        threading.Thread(target=flashbang).start()

def on_press(key):
    if ENABLE_DEBUG_KEY and key == keyboard.Key.f9:
        threading.Thread(target=flashbang).start()

mouse_listener = mouse.Listener(on_click=on_click)
keyboard_listener = keyboard.Listener(on_press=on_press)
mouse_listener.start()
keyboard_listener.start()

try:
    root.mainloop()
except KeyboardInterrupt:
    mouse_listener.stop()
    keyboard_listener.stop()
