# 🦖 Google Dinosaur Game Bot (No Internet Game Automation)

This project is an automation bot for the classic Google Chrome **Dinosaur Game** (played when you're offline). The script uses **Python**, **PyAutoGUI**, **PIL**, and **NumPy** to detect obstacles and automatically jump over them — allowing the dino to survive endlessly (until speed kills it!).

---

## 📄 Project Description

The bot works by:
- Asking you to place your cursor near the dinosaur.
- Capturing a region in front of the dinosaur.
- Detecting obstacles using grayscale image analysis.
- Simulating spacebar presses to make the dinosaur jump.

> ⚠️ This project automates keyboard inputs and screen capture. Make sure the game is visible on your screen and you're focused on the correct window.

---

## 🧰 Technologies Used

- Python 3.x
- [`PyAutoGUI`](https://pypi.org/project/pyautogui/) – simulate key presses
- [`Pillow`](https://pypi.org/project/Pillow/) – capture screenshots and convert to grayscale
- [`NumPy`](https://pypi.org/project/numpy/) – for pixel array manipulation
- Built-in `logging` module

---

## 🚀 How to Run

### 1. Install Dependencies
```bash
pip install pyautogui pillow numpy
