# Flashbang

**Flashbang** is a prank utility that simulates a “flashbang” effect on your Windows computer. When triggered, it briefly displays a **full-screen white flash** and plays a **loud sound**, creating the effect of a flashbang. The program can temporarily maximize your system volume to ensure the sound is loud, then restores it afterward.  

---

## Features

- Randomly triggers on **mouse clicks**.  
- Optional **debug key (F9)** to manually trigger the flash.  
- Safe exit with **F10**.  
- Works as a **Python script** or as a **standalone Windows `.exe`**.  
- Bundles the sound effect inside the `.exe` — no extra files required.

---

## How It Works

- Uses **Tkinter** for the full-screen white flash.  
- Uses **pygame** to play the flashbang sound.  
- Uses **PyCAW** to optionally force maximum system volume.  
- Uses **pynput** for global mouse and keyboard event listening.  
- Designed to run in the background without freezing your system.

---

## Usage

1. **Download the Windows `.exe`** from the GitHub releases (no Python installation required).  
2. Run the `.exe;` it will run in the background.  
3. Click randomly — with a small chance, a flash and sound will trigger.  
4. Press **F9** to test manually (if debug mode is enabled).  
5. Press **F10** to stop the program and exit safely.  

**Note:**  
- The `.exe` includes the sound file internally, so you do **not** need to keep `bang.wav` in the folder.  
- Compatible with **Windows 10 and 11**.

---

## Development

To build the `.exe` from source:

```powershell
python -m PyInstaller --onefile --add-data "bang.wav;." Flashbang.py
