# Flashbang

A fun little prank app for Windows.  
Every once in a while, your screen will flash white and a loud bang sound will play — like a flashbang going off.

## Download
Go to **Releases** and grab `Flashbang.exe`.  
Just run it on Windows — no setup needed.

## Build it yourself
If you want to build it from source:

```powershell
python -m PyInstaller --onefile --noconsole --add-data "bang.wav;." Flashbang.py
