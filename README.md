# ⌨️ Python Keylogger (Educational Use Only)

This project is a **Python-based keylogger** that logs all keyboard inputs into a timestamped file. It uses the `pynput` library to monitor keystrokes and logs them with a timestamp for each entry.

>  **Disclaimer:** This script is provided **strictly for educational, ethical, and authorized purposes only**. Do **not** use this on devices or systems without proper consent, as it may violate privacy laws or computer misuse acts.

---

##  Features

- Captures every keypress including special keys
- Stores logs in a `keylogs/` directory
- Automatically creates log files with timestamps
- Uses the `pynput` library for real-time key capture

---

##  Requirements

- Python 3.x
- [pynput](https://pypi.org/project/pynput/)

Install dependencies using:

pip install pynput

---
###  How to Run

python keylogger.py
The script will:

Start listening to keyboard input

Save logs in the keylogs/ folder

Stop only when the Python process is manually terminated

---

###  Output Example
keylogs/
└── 2025-06-28_15-30-10.txt
Contents of log file:

vbnet
Copy
Edit
2025-06-28 15:30:11,823: Key a pressed.
2025-06-28 15:30:12,024: Key b pressed.
2025-06-28 15:30:13,146: Special Key Key.space pressed.

---

###  Legal & Ethical Use
This tool is intended for:

Cybersecurity students

Parental monitoring (with child awareness)

Personal productivity or usability testing

 Never use this script on public, workplace, or third-party systems without explicit permission.

---
###  Author
Fahim Akthar
B.Tech Cyber Security | Crescent Institute of Science and Technology
