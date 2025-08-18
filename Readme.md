# 🎨 Color Detection Project

This project detects specific colors (**Red, Green, Blue, Yellow**) in real-time using OpenCV.  
You can detect individual colors or multiple colors at the same time.

---

## ✨ Features

- Detect **Red, Green, Blue, Yellow** colors in a video stream.
- Option to detect **all supported colors simultaneously**.
- Works with **webcam feed** or **other camera source(http)**.
- Highlights detected regions using binary masks.
- Clean, modular code for easy extension to other colors.

---

## 🛠 Requirements

- Python
- OpenCV
- NumPy

Install dependencies:

```bash
pip install opencv-python numpy
```

Usage:

```bash
python3 main.py --camera <value> --color <value | values>
```

**--camera:** 0(default) | link to other camera source(usually http).

**--color:** red(default) | any color out of {"red", "blue","green","yellow"} or its combination.
