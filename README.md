# Flashbang

A fun little prank app for Windows.  
Every once in a while, your screen will flash white and a loud bang sound will play — like a flashbang going off.

---

## How it works
- Runs in the background once you start it  
- Randomly triggers a fullscreen white flash with a bang sound  
- That’s it. Nothing fancy.

---

## Download
Head over to **Releases** and grab the `Flashbang.exe` file.  
Run it on Windows — no need for Python or setup.

---

## Build it yourself
If you want to make your own build, run:

```powershell
python -m PyInstaller --onefile --noconsole --add-data "bang.wav;." Flashbang.py
